#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 tldw-project
"""Prepare a native Buddy archive with installed Chatbook APIs; never publish it."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path
from tempfile import TemporaryDirectory

MAX_REVIEW_BYTES = 64 * 1024
REQUIRED = ("idle", "thinking", "error", "listening", "speaking")
DEFAULTS = dict(zip(REQUIRED, ("idle", "review", "failed", "waiting", "speaking")))


class PreparationError(ValueError):
    """An actionable error without source-controlled text."""


def _json(value: object) -> bytes:
    return (
        json.dumps(value, indent=2, ensure_ascii=True, allow_nan=False) + "\n"
    ).encode()


def _review(path: Path, source, state_type, read_metadata) -> tuple:
    with path.open("rb") as stream:
        data = stream.read(MAX_REVIEW_BYTES + 1)
    if len(data) > MAX_REVIEW_BYTES:
        raise PreparationError("Review file exceeds 64 KiB.")
    review = read_metadata(data).get("review")
    if type(review) is not dict or set(review) != {
        "source_sha256",
        "states",
        "mappings",
    }:
        raise PreparationError(
            "Use an inspection report with a complete review object."
        )
    if review["source_sha256"] != source.source_sha256:
        raise PreparationError(
            "Source changed since review. Inspect and review the current source again."
        )
    raw = review["states"]
    if type(raw) is not list or not 1 <= len(raw) <= 11:
        raise PreparationError(
            "Review needs explicit state rows, frame counts and timing."
        )
    states = tuple(state_type(**item) for item in raw)
    # The actual native conversion boundary validates every state and mapping.
    return states, review["mappings"]


def _write_new_output(output: Path, archive: bytes, report: dict, source) -> None:
    """Claim a fresh directory; clean only exact files created by this invocation."""
    if not source.is_current():
        raise PreparationError(
            "Source changed during preparation. Start a fresh review."
        )
    output.mkdir(mode=0o700)
    directory_id = (output.stat().st_dev, output.stat().st_ino)
    owned = []
    try:
        for name, data in (
            ("buddy.tldw-persona-vpack", archive),
            ("review.json", _json(report)),
        ):
            target = output / name
            with target.open("xb") as stream:
                os.fchmod(stream.fileno(), 0o600)
                info = os.fstat(stream.fileno())
                owned.append((target, (info.st_dev, info.st_ino)))
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
        if not source.is_current():
            raise PreparationError(
                "Source changed during preparation. Start a fresh review."
            )
    except BaseException:
        # Do not delete a concurrently replaced file or anyone else's new file.
        if (
            not output.is_symlink()
            and (output.stat().st_dev, output.stat().st_ino) == directory_id
        ):
            for target, identity in owned:
                try:
                    info = target.lstat()
                    if (info.st_dev, info.st_ino) == identity:
                        target.unlink()
                except FileNotFoundError:
                    pass
            try:
                output.rmdir()
            except OSError:
                pass
        raise


def prepare(args: argparse.Namespace) -> tuple[int, dict]:
    """Acquire one source, inspect/map it, and optionally prepare verified bytes."""
    output = Path(args.output).absolute() if args.output else None
    if output is not None and (output.exists() or output.is_symlink()):
        raise PreparationError(
            "Output already exists. Choose a new directory; nothing was replaced."
        )
    if output is not None and not output.parent.is_dir():
        raise PreparationError("The output parent directory must already exist.")
    from tldw_chatbook.Petdex.conversion import (
        PetdexState,
        build_petdex_archive,
        inspect_petdex,
    )
    from tldw_chatbook.Petdex.network import PetdexNetworkError
    from tldw_chatbook.Petdex.registry import fetch_petdex_source
    from tldw_chatbook.Petdex.sources import read_local_package, read_metadata

    try:
        source = (
            fetch_petdex_source(args.pet)
            if args.pet
            else read_local_package(args.local)
        )
    except PetdexNetworkError as exc:
        raise PreparationError(
            f"Petdex fetch failed: {exc.category}. No pack installed."
        ) from None
    inspection = inspect_petdex(source)
    states = inspection.states
    names = {state.name for state in states}
    mappings = {
        key: value if value in names else None for key, value in DEFAULTS.items()
    }
    if args.review:
        states, mappings = _review(
            Path(args.review), source, PetdexState, read_metadata
        )
    report = {
        "status": "inspected" if states else "needs_mapping",
        "installed": False,
        "title": source.title,
        "artwork": dict(source.artwork),
        "atlas": {
            "version": inspection.version,
            "rows": inspection.rows,
            "cell_width": inspection.cell_width,
            "cell_height": inspection.cell_height,
        },
        "mapping_source": "user-reviewed" if args.review else inspection.mapping_source,
        "review": {
            "source_sha256": source.source_sha256,
            "states": [asdict(state) for state in states],
            "mappings": mappings,
        },
        "warnings": [
            f"{key} uses the idle fallback."
            for key, value in mappings.items()
            if key != "idle" and value is None
        ]
        if isinstance(mappings, dict)
        else [],
    }
    if not states:
        report["warnings"].append(
            "This atlas needs explicit state rows, frame counts and timing; no archive was prepared."
        )
    if args.inspect:
        return 0, report
    if not states:
        return 3, report
    archive = build_petdex_archive(
        source, states=states if args.review else None, mappings=mappings
    )
    report.update(
        status="prepared",
        archive_path=str(output / "buddy.tldw-persona-vpack"),
        archive_sha256=hashlib.sha256(archive).hexdigest(),
        archive_bytes=len(archive),
    )
    _write_new_output(output, archive, report, source)
    return 0, report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--pet", help="Exact Petdex slug or https://petdex.dev/pets/... URL"
    )
    source.add_argument("--local", help="Downloaded folder, pet.json or ZIP path")
    parser.add_argument(
        "--inspect",
        action="store_true",
        help="Print review JSON without creating files",
    )
    parser.add_argument(
        "--output", help="New output directory inside an existing writable parent"
    )
    parser.add_argument(
        "--review", help="Edited inspection report; requires matching source digest"
    )
    args = parser.parse_args(argv)
    if args.inspect and (args.output or args.review):
        parser.error("--inspect cannot be combined with --output or --review")
    if not args.inspect and not args.output:
        parser.error("preparation requires --output")
    try:
        code, report = prepare(args)
        sys.stdout.write(_json(report).decode())
        return code
    except ImportError:
        message = (
            "Chatbook Petdex support or its dependencies are unavailable in this Python environment. "
            "Use a compatible Chatbook build (tested at b4e460f75), or its Petdex UI. No pack installed."
        )
    except PreparationError as exc:
        message = str(exc)
    except (ValueError, TypeError, KeyError):
        message = "Petdex source or review validation failed. Check the exact source, version, state rows and mappings. No pack installed."
    except OSError:
        message = "Could not read the source or write the new output directory. Check access and retry with a fresh output path. No pack installed."
    print(message, file=sys.stderr)
    return 2


def cli() -> int:
    """Keep Chatbook import-time configuration writes inside a disposable profile."""
    # This entry point is a separate process, never the running Chatbook host.
    with TemporaryDirectory(prefix="petdex-preparation-config-") as directory:
        root = Path(directory).resolve()
        data = root / "data"
        data.mkdir(mode=0o700)
        config = root / "config.toml"
        config.write_text("[paths]\ndata_dir = " + json.dumps(str(data)) + "\n")
        config.chmod(0o600)
        previous = os.environ.get("TLDW_CONFIG_PATH")
        os.environ["TLDW_CONFIG_PATH"] = str(config)
        try:
            return main()
        finally:
            if previous is None:
                os.environ.pop("TLDW_CONFIG_PATH", None)
            else:
                os.environ["TLDW_CONFIG_PATH"] = previous


if __name__ == "__main__":
    raise SystemExit(cli())
