"""Negative checks must reject bad planes even with refreshed file metadata."""

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_codec_collection as codec
from PIL import Image


class CodecValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.pack = self.root / "character-packs" / "default-assistant"
        shutil.copytree(codec.ROOT / "character-packs" / "default-assistant", self.pack)
        self.inventory = self.pack / "codec" / "inventory.json"

    def refresh_metadata(self):
        inventory = json.loads(self.inventory.read_text())
        for role, entry in inventory["frames"].items():
            raw = (self.pack / "codec" / (role + ".png")).read_bytes()
            entry.update(sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw))
        self.inventory.write_text(json.dumps(inventory))

    def test_different_open_eyes_rejected_after_hash_refresh(self):
        frame = self.pack / "codec" / "open.png"
        recipe = json.loads(self.inventory.read_text())["recipe"]
        with Image.open(frame) as original:
            image = original.convert("RGBA")
        eye = recipe["left_eye"]
        image.putpixel((eye["x"] + 4, eye["y"] + 4), (255, 0, 0, 255))
        image.save(frame)
        self.refresh_metadata()
        with (
            patch.object(codec, "ROOT", self.root),
            self.assertRaisesRegex(AssertionError, "open eyes"),
        ):
            codec.check_pack("default-assistant")

    def test_total_set_budget_rejected_when_individual_frames_fit(self):
        for frame in (self.pack / "codec").glob("*.png"):
            raw = frame.read_bytes()
            frame.write_bytes(raw + b"\0" * (3 * 1024 * 1024 - len(raw)))
        self.refresh_metadata()
        with patch.object(codec, "ROOT", self.root), self.assertRaises(AssertionError):
            codec.check_pack("default-assistant")


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.catalog = self.root / "character-packs" / "codec-catalog.json"
        self.catalog.parent.mkdir()
        self.data = json.loads(
            (codec.ROOT / "character-packs" / "codec-catalog.json").read_text()
        )
        for source in (codec.ROOT / "buddy-packs").glob("*/*.tldw-persona-vpack"):
            target = self.root / source.relative_to(codec.ROOT)
            target.parent.mkdir(parents=True)
            target.touch()

    def test_omitted_buddy_rejected(self):
        self.data["entries"] = [e for e in self.data["entries"] if e["id"] != "cat"]
        self.catalog.write_text(json.dumps(self.data))
        with (
            patch.object(codec, "ROOT", self.root),
            self.assertRaisesRegex(AssertionError, "roster coverage"),
        ):
            codec.check_catalog()

    def test_card_path_cannot_escape_its_pack(self):
        self.data["entries"][0]["card"] = "../outside.character.json"
        self.catalog.write_text(json.dumps(self.data))
        with (
            patch.object(codec, "ROOT", self.root),
            self.assertRaisesRegex(AssertionError, "card path escapes pack"),
        ):
            codec.check_catalog()


if __name__ == "__main__":
    unittest.main()
