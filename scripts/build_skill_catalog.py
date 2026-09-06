# SPDX-License-Identifier: Apache-2.0
"""Build the local skill index; this command does not install or download skills."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/rmusser01/tldw-stuff"


def build_catalog() -> dict:
    entries = []
    names = set()
    for skill_file in sorted((ROOT / "skills").glob("*/*/SKILL.md")):
        folder = skill_file.parent
        if folder.name in names:
            raise ValueError(f"Ambiguous skill name: {folder.name}")
        names.add(folder.name)
        manifest_path = folder / "UPSTREAM.json"
        if not manifest_path.exists():
            manifest_path = folder / "PROVENANCE.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        relative = folder.relative_to(ROOT).as_posix()
        readme = "COLLECTION.md" if (folder / "COLLECTION.md").exists() else "README.md"
        if not (folder / readme).is_file():
            raise ValueError(f"Missing collection README: {relative}")
        entries.append(
            {
                "id": folder.relative_to(ROOT / "skills").as_posix(),
                "name": folder.name,
                "path": relative,
                "readme": f"{relative}/{readme}",
                "license": manifest["license"],
                "authors": manifest["authors"],
                "install_url": f"{REPOSITORY}/tree/main/{relative}",
                "skill_sha256": hashlib.sha256(skill_file.read_bytes()).hexdigest(),
                "manifest": f"{relative}/{manifest_path.name}",
                "manifest_sha256": hashlib.sha256(
                    manifest_path.read_bytes()
                ).hexdigest(),
            }
        )
    return {
        "schema_version": 1,
        "repository": REPOSITORY,
        "ref": "main",
        "install_guide": "INSTALL.md",
        "revision_policy": "Resolve main to a commit before a reproducible install; load this catalog and the selected bundle from that same revision.",
        "skills": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Fail if the checked-in catalog is stale"
    )
    args = parser.parse_args()
    output = ROOT / "skills" / "catalog.json"
    catalog = build_catalog()
    text = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != text:
            raise SystemExit(
                "Skill catalog is stale; run scripts/build_skill_catalog.py"
            )
    else:
        output.write_text(text, encoding="utf-8")
    print(f"Catalog contains {len(catalog['skills'])} skills")


if __name__ == "__main__":
    main()
