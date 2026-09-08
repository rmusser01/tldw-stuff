"""Exercise the optional helper with real Chatbook Petdex/native validators."""

import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

HELPER = (
    Path(__file__).resolve().parents[1]
    / "skills/chatbook/petdex-install/scripts/prepare_pet.py"
)
spec = importlib.util.spec_from_file_location("petdex_prepare", HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class PrepareTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.package = self.root / "pet"
        self.package.mkdir()
        self.metadata = {
            "name": "Sentinel",
            "spriteVersionNumber": 1,
            "creator": "Original Artist",
            "license": "Original terms",
            "spritesheetPath": "spritesheet.png",
        }
        self.write_package()
        self.output = self.root / "prepared"

    def tearDown(self):
        self.temp.cleanup()

    def write_package(self, version=1):
        self.metadata["spriteVersionNumber"] = version
        (self.package / "pet.json").write_text(json.dumps(self.metadata))
        with Image.new("RGBA", (96, 13 * (9 if version == 1 else 11)), "cyan") as image:
            image.save(self.package / "spritesheet.png")
        (self.package / "NOTICE").write_text("Keep this exact notice.\n")

    def run_helper(self, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch("sys.stdout", stdout), patch("sys.stderr", stderr):
            result = helper.main(list(args))
        return result, stdout.getvalue(), stderr.getvalue()

    def test_classic_archive_is_native_and_preserves_credits(self):
        from tldw_chatbook.Persona_Visual.snapshot import read_buddy_archive

        code, output, error = self.run_helper(
            "--local", str(self.package), "--output", str(self.output)
        )
        self.assertEqual((code, error), (0, ""))
        report = json.loads(output)
        self.assertEqual(report["status"], "prepared")
        self.assertFalse(report["installed"])
        snapshot = read_buddy_archive(self.output / "buddy.tldw-persona-vpack")
        self.assertEqual(snapshot.artwork["creator"], "Original Artist")
        self.assertIn("Keep this exact notice.", snapshot.artwork["notices"])
        self.assertEqual(
            snapshot.assets[0].data, (self.package / "spritesheet.png").read_bytes()
        )
        self.assertEqual(json.loads((self.output / "review.json").read_text()), report)
        self.assertEqual(report["review"]["mappings"]["speaking"], None)

    def test_output_collision_does_not_overwrite_or_fetch(self):
        self.output.mkdir()
        retained = self.output / "keep.txt"
        retained.write_text("existing")
        with patch("tldw_chatbook.Petdex.registry.fetch_petdex_source") as fetch:
            code, _, _ = self.run_helper(
                "--pet", "example", "--output", str(self.output)
            )
        self.assertNotEqual(code, 0)
        self.assertEqual(retained.read_text(), "existing")
        fetch.assert_not_called()

    def test_v2_inspection_requires_review_and_accepts_explicit_rows(self):
        self.write_package(2)
        code, text, _ = self.run_helper("--local", str(self.package), "--inspect")
        self.assertEqual(code, 0)
        report = json.loads(text)
        self.assertEqual(report["status"], "needs_mapping")
        self.assertEqual(report["review"]["states"], [])
        self.assertFalse(self.output.exists())
        code, _, _ = self.run_helper(
            "--local", str(self.package), "--output", str(self.output)
        )
        self.assertEqual(code, 3)
        self.assertFalse(self.output.exists())
        report["review"]["states"] = [
            {"name": "idle", "row": 10, "frames": 2, "duration_ms": 240, "loop": True}
        ]
        report["review"]["mappings"]["idle"] = "idle"
        review_file = self.root / "review.json"
        review_file.write_text(json.dumps(report))
        code, _, error = self.run_helper(
            "--local",
            str(self.package),
            "--review",
            str(review_file),
            "--output",
            str(self.output),
        )
        self.assertEqual((code, error), (0, ""))
        from tldw_chatbook.Persona_Visual.snapshot import read_buddy_archive

        manifest = json.loads(
            read_buddy_archive(self.output / "buddy.tldw-persona-vpack").manifest_json
        )
        self.assertEqual(
            manifest["animations"]["idle"]["frames"][0]["region"]["y"], 130
        )

    def test_changed_source_cannot_use_prior_review(self):
        _, text, _ = self.run_helper("--local", str(self.package), "--inspect")
        review = self.root / "review.json"
        review.write_text(text)
        (self.package / "NOTICE").write_text("Changed terms")
        code, _, error = self.run_helper(
            "--local",
            str(self.package),
            "--review",
            str(review),
            "--output",
            str(self.output),
        )
        self.assertEqual(code, 2)
        self.assertIn("changed", error.lower())
        self.assertFalse(self.output.exists())

    def test_failed_write_cleans_only_created_output(self):
        original = Path.open

        def failing(path, *args, **kwargs):
            if path.name == "review.json" and "x" in str(
                args[0] if args else kwargs.get("mode", "r")
            ):
                raise OSError("injected")
            return original(path, *args, **kwargs)

        with patch.object(Path, "open", failing):
            code, _, _ = self.run_helper(
                "--local", str(self.package), "--output", str(self.output)
            )
        self.assertEqual(code, 2)
        self.assertFalse(self.output.exists())
        self.assertTrue((self.package / "pet.json").is_file())

    def test_cli_keeps_selected_profile_unchanged(self):
        import os
        import subprocess
        import sys

        profile = self.root / "existing-profile.toml"
        profile.write_text('[general]\nusers_name = "Keep me"\n')
        original = profile.stat()
        env = {**os.environ, "TLDW_CONFIG_PATH": str(profile)}
        result = subprocess.run(
            [
                sys.executable,
                str(HELPER),
                "--local",
                str(self.package),
                "--output",
                str(self.output),
            ],
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr[-1500:])
        self.assertEqual(json.loads(result.stdout)["status"], "prepared")
        self.assertEqual(profile.read_text(), '[general]\nusers_name = "Keep me"\n')
        self.assertEqual(profile.stat().st_mtime_ns, original.st_mtime_ns)

    def test_duplicate_review_keys_and_invalid_states_are_rejected(self):
        _, text, _ = self.run_helper("--local", str(self.package), "--inspect")
        report = json.loads(text)
        report["review"]["states"][0]["frames"] = 9
        review = self.root / "review.json"
        review.write_text(json.dumps(report))
        code, _, _ = self.run_helper(
            "--local",
            str(self.package),
            "--review",
            str(review),
            "--output",
            str(self.output),
        )
        self.assertEqual(code, 2)
        self.assertFalse(self.output.exists())
        review.write_text('{"review":{},"review":{}}')
        code, _, _ = self.run_helper(
            "--local",
            str(self.package),
            "--review",
            str(review),
            "--output",
            str(self.output),
        )
        self.assertEqual(code, 2)
        self.assertFalse(self.output.exists())

    def test_missing_chatbook_reports_capability_and_writes_nothing(self):
        import builtins

        original = builtins.__import__

        def unavailable(name, *args, **kwargs):
            if name.startswith("tldw_chatbook.Petdex"):
                raise ModuleNotFoundError(name)
            return original(name, *args, **kwargs)

        with patch("builtins.__import__", unavailable):
            code, _, error = self.run_helper(
                "--pet", "example", "--output", str(self.output)
            )
        self.assertEqual(code, 2)
        self.assertIn("unavailable", error)
        self.assertFalse(self.output.exists())

    def test_remote_failure_retains_actionable_category(self):
        from tldw_chatbook.Petdex.network import PetdexNetworkError

        with patch(
            "tldw_chatbook.Petdex.registry.fetch_petdex_source",
            side_effect=PetdexNetworkError("rate limited", status_code=429),
        ):
            code, _, error = self.run_helper(
                "--pet", "example", "--output", str(self.output)
            )
        self.assertEqual(code, 2)
        self.assertIn("rate limited", error)
        self.assertFalse(self.output.exists())

    def test_remote_source_uses_native_transport_adapter(self):
        from tldw_chatbook.Petdex.sources import read_local_package

        source = read_local_package(self.package)
        with patch(
            "tldw_chatbook.Petdex.registry.fetch_petdex_source", return_value=source
        ) as fetch:
            code, _, _ = self.run_helper(
                "--pet",
                "https://petdex.dev/pets/exact-slug",
                "--output",
                str(self.output),
            )
        self.assertEqual(code, 0)
        fetch.assert_called_once_with("https://petdex.dev/pets/exact-slug")


if __name__ == "__main__":
    unittest.main()
