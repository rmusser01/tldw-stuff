"""Check distributed codec files without importing or modifying an app profile."""

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PACKS = (
    "switch",
    "patch",
    "pulse",
    "vector",
    "default-assistant",
    "samira",
    "pixel-migu",
)
ROLES = ("rest", "small", "open", "blink_rest", "blink_small", "blink_open")


def same(a, b):
    return all(high == 0 for _, high in ImageChops.difference(a, b).getextrema())


def check_pack(slug):
    pack = ROOT / "character-packs" / slug
    directory = pack / "codec"
    inventory = json.loads((directory / "inventory.json").read_text())
    assert set(inventory["frames"]) == set(ROLES), slug
    images = {}
    for role in ROLES:
        entry = inventory["frames"][role]
        assert entry["file"] == role + ".png", (slug, role)
        raw = (directory / entry["file"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == entry["sha256"], (slug, role, "hash")
        assert len(raw) == entry["bytes"] <= 4 * 1024 * 1024
        with Image.open(directory / entry["file"]) as image:
            assert image.format == "PNG" and getattr(image, "n_frames", 1) == 1
            assert image.size == (entry["width"], entry["height"])
            assert image.width * image.height <= 1_048_576
            images[role] = image.convert("RGBA")
    assert len({im.size for im in images.values()}) == 1
    assert (
        sum(entry["bytes"] for entry in inventory["frames"].values())
        <= 16 * 1024 * 1024
    )
    assert max(base_size for im in images.values() for base_size in im.size) <= 4096
    assert len({hashlib.sha256(im.tobytes()).digest() for im in images.values()}) == 6
    recipe = inventory["recipe"]
    base = images["rest"]
    assert base.size == (recipe["width"], recipe["height"])
    header = (
        b"tldw-portrait-base-rgba-v1\0"
        + base.width.to_bytes(4, "big")
        + base.height.to_bytes(4, "big")
    )
    assert (
        hashlib.sha256(header + base.tobytes()).hexdigest()
        == recipe["base_pixel_sha256"]
    )
    masks = {}
    for name in ("left_eye", "right_eye", "mouth"):
        r = recipe[name]
        assert all(type(r[k]) is int for k in ("x", "y", "width", "height"))
        x, y, w, h = (r[k] for k in ("x", "y", "width", "height"))
        assert 0 <= x < x + w <= base.width and 0 <= y < y + h <= base.height
        mask = Image.new("L", base.size)
        ImageDraw.Draw(mask).rectangle((x, y, x + w - 1, y + h - 1), fill=255)
        masks[name] = mask
    assert all(
        ImageChops.multiply(masks[a], masks[b]).getbbox() is None
        for a, b in (
            ("left_eye", "right_eye"),
            ("left_eye", "mouth"),
            ("right_eye", "mouth"),
        )
    )
    eyes = ImageChops.lighter(masks["left_eye"], masks["right_eye"])
    support = ImageChops.lighter(eyes, masks["mouth"])
    for role, image in images.items():
        assert same(Image.composite(base, image, support), base), (
            slug,
            role,
            "outside",
        )
        assert image.getchannel("A").tobytes() == base.getchannel("A").tobytes()
    for mouth in ("rest", "small", "open"):
        assert same(Image.composite(base, images[mouth], masks["mouth"]), base), (
            slug,
            mouth,
            "open eyes",
        )
        assert same(
            Image.composite(base, images[mouth], eyes),
            Image.composite(base, images["blink_" + mouth], eyes),
        ), (slug, mouth, "mouth pair")
        assert same(
            Image.composite(images["blink_rest"], images["blink_" + mouth], eyes),
            images["blink_" + mouth],
        ), (slug, mouth, "blink plane")
    assert same(Image.composite(base, images["blink_rest"], eyes), base), (
        slug,
        "blink outside",
    )
    for line in (pack / "CODEC_SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert name.startswith("codec/") and ".." not in Path(name).parts
        assert hashlib.sha256((pack / name).read_bytes()).hexdigest() == digest
    if slug in PACKS[:4]:
        card = json.loads((pack / (slug + ".character.json")).read_text())
        assert card["spec"] == "chara_card_v2" and card["spec_version"] == "2.0"
        assert all(
            card["data"][field].strip()
            for field in (
                "name",
                "description",
                "personality",
                "first_mes",
                "system_prompt",
            )
        )
        assert card["data"]["creator"] == "tldw-project"
        assert (pack / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes()
    return sum(entry["bytes"] for entry in inventory["frames"].values())


if __name__ == "__main__":
    total = sum(check_pack(slug) for slug in PACKS)
    print(
        f"PASS: {len(PACKS)} sets, 42 PNGs, {total:,} bytes; hashes, native budgets, exact pairs and unchanged outside pixels."
    )
