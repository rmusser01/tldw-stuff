"""Build native Buddy packs and previews from the collection's reviewed artwork.

Requires Pillow and the documented Chatbook development APIs. Run as a separate
process; application imports are isolated from the user's configuration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image

LOOPS = {
    "idle": ([0, 1, 0, 2, 0], [1500, 220, 1300, 140, 1000], True),
    "thinking": ([4, 5], [1100, 900], True),
    "speaking": ([6, 7], [180, 220], True),
    "listening": ([8], [1000], False),
    "sleepy": ([9], [1000], False),
    "error": ([10], [1000], False),
    "confused": ([11], [1000], False),
    "wave": ([12, 0, 12, 0], [250, 180, 250, 800], False),
    "happy": ([13], [1000], False),
    "celebrate": ([14, 13, 14], [400, 300, 800], False),
    "love": ([15], [1000], False),
}

STATE_ANIMATIONS = {
    "idle": "idle",
    "wake_armed": "listening",
    "listening": "listening",
    "thinking": "thinking",
    "speaking": "speaking",
    "tool_running": "thinking",
    "approval_needed": "confused",
    "error": "error",
    "offline": "sleepy",
    "reaction.greeting": "wave",
    "reaction.happy": "happy",
    "reaction.success": "celebrate",
    "mood.neutral": "idle",
    "mood.thinking": "thinking",
    "mood.sleepy": "sleepy",
    "mood.confused": "confused",
    "mood.happy": "happy",
    "mood.love": "love",
}


def manifest() -> dict:
    """Return the shared reaction mapping for the reviewed sixteen-pose atlas."""
    animations = {}
    for name, (indices, durations, loop) in LOOPS.items():
        animations[name] = {
            "frames": [
                {
                    "asset_id": "atlas",
                    "duration_ms": duration,
                    "region": {
                        "x": (index % 4) * 128,
                        "y": (index // 4) * 128,
                        "width": 128,
                        "height": 128,
                    },
                }
                for index, duration in zip(indices, durations, strict=True)
            ],
            "loop": loop,
            "preview_frame": 0,
            "alignment": {"x": 0.5, "y": 1.0},
        }
    return {
        "renderer_type": "sprite_frames",
        "manifest_version": 1,
        "states": {
            name: {"animation_id": animation}
            for name, animation in STATE_ANIMATIONS.items()
        },
        "animations": animations,
        "fallbacks": {},
        "state_catalog": {
            state: {"kind": state.split(".")[0], "label": state.split(".")[1].title()}
            for state in STATE_ANIMATIONS
            if "." in state
        },
        "authored_triggers": [],
    }


def build(folder: Path) -> dict:
    """Validate the atlas, build its native archive, and render real pack previews."""
    from tldw_chatbook.Persona_Visual.assets import PersonaVisualAssetMetadata
    from tldw_chatbook.Persona_Visual.export import build_native_buddy_archive
    from tldw_chatbook.Persona_Visual.snapshot import BuddyAssetSnapshot, BuddySnapshot

    recipe = json.loads((folder / "recipe.json").read_text())
    sheet_data = (folder / "source.png").read_bytes()
    sheet = Image.open(BytesIO(sheet_data))
    if sheet.mode != "RGBA" or sheet.size != (512, 512):
        raise ValueError(f"Expected reviewed 512x512 RGBA atlas: {folder.name}")
    if sheet.getchannel("A").getextrema() != (0, 255):
        raise ValueError(
            f"Atlas must contain transparent and opaque pixels: {folder.name}"
        )
    digest = hashlib.sha256(sheet_data).hexdigest()
    metadata = PersonaVisualAssetMetadata(
        asset_key="atlas",
        role="sprite_sheet",
        mime_type="image/png",
        byte_count=len(sheet_data),
        sha256=digest,
        width=512,
        height=512,
        frame_count=1,
        duration_ms=None,
    )
    artwork = {
        "version": 1,
        "creator": "tldw-project",
        "license": "Apache-2.0",
        "source_url": f"https://github.com/rmusser01/tldw-stuff/tree/main/buddy-packs/{folder.name}",
        "notices": (
            "Copyright 2026 tldw-project. Licensed under Apache-2.0.\n"
            "AI-assisted original artwork, generated with OpenAI image generation, "
            "then reviewed and prepared for this collection.\n"
            "Style references: the collection's existing 2D Buddy artwork. "
            "No existing Buddy image pixels are included in this atlas.\n\n"
            + (folder / "LICENSE.txt").read_text()
        ),
    }
    document = manifest()
    snapshot = BuddySnapshot(
        recipe["title"],
        json.dumps(document, sort_keys=True),
        (BuddyAssetSnapshot(metadata, sheet_data),),
        artwork,
        digest,
        lambda: (
            hashlib.sha256((folder / "source.png").read_bytes()).hexdigest() == digest
        ),
    )
    archive = build_native_buddy_archive(snapshot)
    archive_name = folder.name + ".tldw-persona-vpack"
    (folder / archive_name).write_bytes(archive)
    (folder / "manifest.json").write_text(json.dumps(document, indent=2) + "\n")
    frames = [
        sheet.crop(
            ((i % 4) * 128, (i // 4) * 128, (i % 4 + 1) * 128, (i // 4 + 1) * 128)
        )
        for i in range(16)
    ]
    frames[0].save(folder / "preview.png", optimize=True)
    # GIF gallery preview uses a dark matte; the actual archive retains alpha.
    # This avoids GIF's one-bit transparency producing colored edge halos.
    preview_frames, preview_durations = [], []
    for name in ("idle", "thinking", "speaking", "wave", "happy", "celebrate", "love"):
        indices, durations, _ = LOOPS[name]
        for index, duration in zip(indices, durations, strict=True):
            canvas = Image.new("RGBA", (128, 128), "#20242b")
            canvas.alpha_composite(frames[index])
            preview_frames.append(canvas.convert("RGB"))
            preview_durations.append(duration)
    preview_frames[0].save(
        folder / "preview.gif",
        save_all=True,
        append_images=preview_frames[1:],
        duration=preview_durations,
        loop=0,
        disposal=2,
        optimize=False,
    )
    files = [
        "source.png",
        archive_name,
        "preview.png",
        "preview.gif",
        "manifest.json",
        "recipe.json",
        "PROVENANCE.json",
        "PROMPT.txt",
        "LICENSE.txt",
    ]
    (folder / "SHA256SUMS").write_text(
        "".join(
            f"{hashlib.sha256((folder / name).read_bytes()).hexdigest()}  {name}\n"
            for name in files
        )
    )
    return {
        "id": folder.name,
        "title": recipe["title"],
        "bytes": len(archive),
        "sha256": hashlib.sha256(archive).hexdigest(),
        "assets": 1,
        "poses": 16,
        "states": len(STATE_ANIMATIONS),
        "source_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packs", nargs="+", type=Path)
    args = parser.parse_args()
    with TemporaryDirectory(prefix="buddy-collection-build-") as temporary:
        root = Path(temporary).resolve()
        (root / "data").mkdir(mode=0o700)
        config = root / "config.toml"
        config.write_text(
            "[paths]\ndata_dir = " + json.dumps(str(root / "data")) + "\n"
        )
        config.chmod(0o600)
        os.environ["TLDW_CONFIG_PATH"] = str(config)
        results = [build(folder.resolve()) for folder in args.packs]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
