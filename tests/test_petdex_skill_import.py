"""Full bundle retention through Chatbook's directory and URL/ZIP installers."""

import asyncio
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import AsyncMock, patch

from tldw_chatbook.Skills_Interop.local_skills_service import LocalSkillsService

BUNDLE = Path(__file__).resolve().parents[1] / "skills/chatbook/petdex-install"


class SkillImportTests(unittest.IsolatedAsyncioTestCase):
    async def test_directory_retains_bundle_and_installed_helper_runs(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            service = LocalSkillsService(store_dir=root / "store")
            result = await service.import_skill_directory(
                BUNDLE, name="petdex-install", trust_approved=False
            )
            self.assertEqual(result["trust_status"], "trust_locked")
            self.assertEqual(result["validation_status"], "valid")
            installed = service.skills_dir / "petdex-install"
            self.assert_files(installed)
            from PIL import Image

            source = root / "source"
            source.mkdir()
            (source / "pet.json").write_text(
                '{"name":"Installed helper fixture","spriteVersionNumber":1}'
            )
            with Image.new("RGBA", (96, 117), "cyan") as image:
                image.save(source / "spritesheet.png")
            command = [
                sys.executable,
                str(installed / "scripts/prepare_pet.py"),
                "--local",
                str(source),
                "--output",
                str(root / "output"),
            ]
            run = await asyncio.to_thread(
                subprocess.run,
                command,
                check=False,
                capture_output=True,
                text=True,
                env=os.environ.copy(),
                timeout=30,
            )
            self.assertEqual(run.returncode, 0, run.stderr[-1000:])
            self.assertEqual(json.loads(run.stdout)["status"], "prepared")

    async def test_github_tree_url_retains_full_bundle_without_trust(self):
        import httpx
        from tldw_chatbook.Skills_Interop.skill_remote_fetch import (
            install_skill_from_url,
        )
        from tldw_chatbook.Skills_Interop.skills_scope_service import SkillsScopeService

        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as archive:
            for path in self.bundle_files():
                info = zipfile.ZipInfo(
                    "tldw-stuff-main/skills/chatbook/petdex-install/"
                    + path.relative_to(BUNDLE).as_posix()
                )
                info.create_system = 3
                info.external_attr = path.stat().st_mode << 16
                archive.writestr(info, path.read_bytes())
        seen = []

        def respond(request):
            seen.append(str(request.url))
            return httpx.Response(
                200,
                content=data.getvalue(),
                headers={"content-type": "application/zip"},
            )

        with tempfile.TemporaryDirectory() as folder:
            service = LocalSkillsService(store_dir=Path(folder).resolve() / "store")
            with patch(
                "tldw_chatbook.Utils.github_api_client.GitHubAPIClient.get_branches",
                new=AsyncMock(return_value=["main"]),
            ):
                result = await install_skill_from_url(
                    "https://github.com/rmusser01/tldw-stuff/tree/main/skills/chatbook/petdex-install",
                    scope_service=SkillsScopeService(local_service=service),
                    transport=httpx.MockTransport(respond),
                    resolver=lambda host: ["93.184.216.34"],
                )
            self.assertEqual(result["trust_status"], "trust_locked")
            self.assert_files(service.skills_dir / "petdex-install")
            self.assertTrue(seen)

    def bundle_files(self):
        return [
            p
            for p in BUNDLE.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
        ]

    def assert_files(self, installed):
        for path in self.bundle_files():
            relative = path.relative_to(BUNDLE)
            self.assertTrue((installed / relative).is_file(), str(relative))
            self.assertEqual(
                bool((installed / relative).stat().st_mode & 0o100),
                bool(path.stat().st_mode & 0o100),
                str(relative),
            )
            self.assertEqual(
                (installed / relative).read_bytes(), path.read_bytes(), str(relative)
            )


if __name__ == "__main__":
    unittest.main()
