"""Verify optional companions using actual application importers.

Run with --host chatbook or --host server in that application's Python environment.
Only temporary profiles, configuration and SQLite databases are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]


def registration_checks(frame: Image.Image, name: str, index: int) -> None:
    """Reject displaced cells before running application import checks."""
    opaque = frame.getchannel("A").point(lambda value: 255 if value >= 128 else 0)
    if name == "dipsy":
        # Flippers and the asymmetrical tail move. The cream belly is the
        # reviewed vertical landmark, independent of those appendages.
        belly = opaque
        for channel, threshold in (("R", 150), ("G", 190), ("B", 190)):
            selected = frame.getchannel(channel).point(
                lambda value, threshold=threshold: 255 if value > threshold else 0
            )
            belly = ImageChops.darker(belly, selected)
        box = belly.getbbox()
        assert box and box[3] == 114, (name, index, "belly baseline", box)
        return
    box = opaque.getbbox()
    assert box and box[3] == 118, (name, index, "baseline", box)
    support = opaque.crop((0, 110, 128, 118)).getbbox()
    assert support and abs((support[0] + support[2]) / 2 - 64) <= 0.5, (
        name,
        index,
        "horizontal anchor",
        support,
    )


def artifact_checks(folder: Path) -> None:
    for line in (folder / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert hashlib.sha256((folder / name).read_bytes()).hexdigest() == digest, name
    sheet = Image.open(folder / "source.png")
    assert sheet.mode == "RGBA" and sheet.size == (512, 512)
    assert sheet.getchannel("A").getextrema() == (0, 255)
    for i in range(16):
        frame = sheet.crop(
            ((i % 4) * 128, (i // 4) * 128, (i % 4 + 1) * 128, (i // 4 + 1) * 128)
        )
        registration_checks(frame, folder.name, i)
        box = frame.getbbox()
        assert box and min(box[0], box[1], 128 - box[2], 128 - box[3]) >= 2, (
            folder.name,
            i,
            box,
        )
    assert (
        Image.open(folder / "preview.png").tobytes()
        == sheet.crop((0, 0, 128, 128)).tobytes()
    )
    with Image.open(folder / "preview.gif") as gif:
        assert gif.n_frames >= 10 and gif.info["loop"] == 0
    provenance = json.loads((folder / "PROVENANCE.json").read_text())
    assert provenance["creator"] == "tldw-project"
    assert provenance["license"] == "Apache-2.0"
    assert (
        provenance["source_sha256"]
        == hashlib.sha256((folder / "source.png").read_bytes()).hexdigest()
    )
    if reference := provenance.get("reference"):
        notice = (folder / "NOTICE.txt").read_text()
        assert reference["creator"] in notice and reference["url"] in notice


def chatbook_checks(folder: Path, root: Path) -> dict:
    from tldw_chatbook.Character_Chat.buddy_conversion import (
        convert_buddy,
        publish_buddy_character,
    )
    from tldw_chatbook.Character_Chat.local_character_persona_service import (
        LocalCharacterPersonaService,
    )
    from tldw_chatbook.DB.ChaChaNotes_DB import CharactersRAGDB
    from tldw_chatbook.DB.VisualIdentity_DB import VisualIdentityRepository
    from tldw_chatbook.Persona_Visual.authoring import (
        persona_visual_draft_publication_snapshot,
    )
    from tldw_chatbook.Persona_Visual.contracts import resolve_manifest_state
    from tldw_chatbook.Persona_Visual.export import export_persona_visual_archive
    from tldw_chatbook.Persona_Visual.importer import (
        cleanup_persona_visual_import_review,
        import_persona_visual_pack,
        persona_visual_import_source_root,
    )
    from tldw_chatbook.Persona_Visual.publication import publish_persona_visual
    from tldw_chatbook.Persona_Visual.repository import PersonaVisualRepository
    from tldw_chatbook.Persona_Visual.snapshot import (
        read_buddy_archive,
        read_saved_buddy,
    )

    root.mkdir(mode=0o700)
    profile, staging = root / "profile", root / "staging"
    profile.mkdir(mode=0o700)
    staging.mkdir(mode=0o700)
    archive = folder / (folder.name + ".tldw-persona-vpack")
    original = read_buddy_archive(archive)
    if (folder / "NOTICE.txt").is_file():
        assert (folder / "NOTICE.txt").read_text() in original.artwork["notices"]
    db = CharactersRAGDB(root / "characters.db", client_id="collection-verification")
    try:
        repository = PersonaVisualRepository(db)
        local = LocalCharacterPersonaService(
            db, persona_store_path=profile / "personas.json"
        )
        review = import_persona_visual_pack(
            archive,
            staging_root=staging,
            persona_id=folder.name,
            persona_revision=1,
            expected_identity=None,
        )
        assert review.asset_count == 1 and review.state_count == 18
        result = publish_persona_visual(
            repository,
            persona_visual_draft_publication_snapshot(review.draft),
            source_root=persona_visual_import_source_root(review, staging_root=staging),
            profile_root=profile,
            authority_guard=lambda: True,
        )
        graph = repository.get_active_persona_pack(folder.name)
        assert graph.identity == result.new_identity
        for state in ("idle", "thinking", "speaking"):
            selected = resolve_manifest_state(graph.version.manifest, state)
            assert selected.animate and selected.static.frame_index == 0
            assert len(selected.animation.frames) >= 2
        saved = read_saved_buddy(repository, folder.name, profile)
        assert saved.assets == original.assets and saved.artwork == original.artwork
        assert saved.artwork["creator"] == "tldw-project"
        assert saved.artwork["license"] == "Apache-2.0"
        exported = root / "roundtrip.tldw-persona-vpack"
        exported.write_bytes(
            export_persona_visual_archive(repository, folder.name, profile)
        )
        reloaded = read_buddy_archive(exported)
        assert reloaded.assets == saved.assets and reloaded.artwork == saved.artwork
        converted = convert_buddy(saved)
        assert len(converted.expressions) == 18
        animated = {
            item.source_state: Image.open(BytesIO(item.data)).n_frames
            for item in converted.expressions
        }
        assert all(animated[name] > 1 for name in ("idle", "thinking", "speaking"))
        character = publish_buddy_character(
            converted,
            name=original.title,
            db=db,
            local_service=local,
            profile_root=profile,
            authority_guard=lambda: True,
        )
        active = VisualIdentityRepository(db).get_active_actor_pack(
            "character", character.local_actor_id
        )
        assert active and len(active["assets"]) >= 18
        assert json.loads(active["pack"]["source_context_json"])[
            "tldw/artwork"
        ] == dict(saved.artwork)
        assert cleanup_persona_visual_import_review(review, staging_root=staging)
        return {
            "id": folder.name,
            "host": "chatbook",
            "result": "passed",
            "checks": [
                "native import",
                "publication",
                "reload",
                "export roundtrip",
                "motion/static selection",
                "animated character conversion",
                "independent character publication",
                "attribution retention",
            ],
        }
    finally:
        db.close_connection()


def server_checks(folder: Path, root: Path) -> dict:
    from unittest.mock import patch

    from tldw_Server_API.app.core.DB_Management.ChaChaNotes_DB import CharactersRAGDB
    from tldw_Server_API.app.core.DB_Management.PersonaVisualPortability_DB import (
        PersonaVisualPortabilityRepository,
    )
    from tldw_Server_API.app.core.Persona.visual_portability.importer import (
        PersonaVisualPackImporter,
    )
    from tldw_Server_API.app.core.Persona.visual_portability.preview import (
        PersonaVisualPackImportPreviewer,
    )
    from tldw_Server_API.app.core.Persona.visual_service import DatabasePaths
    from tldw_Server_API.app.core.Persona.visuals import validate_visual_manifest

    root.mkdir(mode=0o700)
    archive = folder / (folder.name + ".tldw-persona-vpack")
    db = CharactersRAGDB(root / "server.db", "collection-verification")
    try:
        repo = PersonaVisualPortabilityRepository.initialized(db)
        persona = db.create_persona_profile({"user_id": "1", "name": folder.name})
        result = PersonaVisualPackImportPreviewer().create_preview(
            archive_path=archive,
            owner_user_id="1",
            target_persona_id=persona,
        )
        preview = repo.create_import_preview(
            owner_user_id="1",
            job_id="collection-" + folder.name,
            status="completed",
            stage="completed",
            archive_path=str(archive),
            target_persona_id=persona,
            **{
                key: result[key]
                for key in [
                    "archive_sha256",
                    "canonical_payload_fingerprint",
                    "schema_version",
                    "bundle_summary",
                    "proposed_plan",
                    "required_choices",
                ]
            },
        )
        with patch.object(
            DatabasePaths, "get_user_persona_visuals_dir", return_value=root / "assets"
        ):
            imported = PersonaVisualPackImporter(
                db=db, repo=repo, user_id="1"
            ).import_preview(
                preview_id=str(preview["id"]),
                target_persona_id=persona,
                trust_mode="untrusted_import",
            )
        pack = db.get_persona_visual_pack(
            pack_id=imported["pack_id"], persona_id=persona, user_id="1"
        )
        assets = db.list_persona_visual_assets(
            pack_id=imported["pack_id"], persona_id=persona, user_id="1"
        )
        assert imported["status"] == "imported" and pack["status"] == "draft"
        assert len(assets) == 1 and len(pack["manifest"]["states"]) == 18
        assert (
            assets[0]["checksum_sha256"]
            == hashlib.sha256((folder / "source.png").read_bytes()).hexdigest()
        )
        validate_visual_manifest(
            pack["manifest"],
            available_asset_ids={a["id"] for a in assets},
            available_asset_dimensions={
                a["id"]: (a["width"], a["height"]) for a in assets
            },
            require_activatable=True,
        )
        return {
            "id": folder.name,
            "host": "server",
            "result": "passed",
            "checks": [
                "native preview",
                "committed inactive draft",
                "asset checksum",
                "activatable manifest",
            ],
        }
    finally:
        db.close_connection()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True, choices=("chatbook", "server"))
    parser.add_argument("--pack", action="append")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    names = (
        args.pack
        or json.loads((ROOT / "buddy-packs/companions.json").read_text())["packs"]
    )
    with TemporaryDirectory(prefix="buddy-collection-check-") as temporary:
        root = Path(temporary).resolve()
        (root / "data").mkdir(mode=0o700)
        config = root / ("config.toml" if args.host == "chatbook" else "config.txt")
        config.write_text(
            "[paths]\ndata_dir = " + json.dumps(str(root / "data")) + "\n"
            if args.host == "chatbook"
            else "[Database]\n"
        )
        config.chmod(0o600)
        os.environ["TLDW_CONFIG_PATH"] = str(config)
        os.environ["TLDW_CONFIG_FILE"] = str(config)
        os.environ["AUTO_DOWNLOAD_MODELS"] = "false"
        check = chatbook_checks if args.host == "chatbook" else server_checks
        results = []
        for name in names:
            folder = ROOT / "buddy-packs" / name
            artifact_checks(folder)
            results.append(check(folder, root / name))
            print(name, args.host, "passed", flush=True)
    if args.report:
        args.report.write_text(json.dumps(results, indent=2) + "\n")
    print(f"All {len(results)} packs passed for {args.host}.")


if __name__ == "__main__":
    main()
