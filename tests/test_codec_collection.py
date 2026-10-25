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


if __name__ == "__main__":
    unittest.main()
