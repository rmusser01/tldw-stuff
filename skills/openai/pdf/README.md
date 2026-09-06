# pdf

Create and inspect PDFs with a render-and-review workflow.

## Attribution and files

- Author/publisher: **OpenAI and upstream contributors**.
- Original source: [openai/skills / skills/.curated/pdf](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf).
- Revision: `49f948faa9258a0c61caceaf225e179651397431` (retrieved 2026-09-05).
- License: [Apache-2.0](LICENSE.txt). All original copyright and attribution notices are retained.
- [Upstream contributors and file history](https://github.com/openai/skills/commits/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf).
- [SKILL.md](SKILL.md) and all its upstream supporting files are copied unchanged.
- [UPSTREAM.json](UPSTREAM.json) records every source path, byte count, hash, and executable flag; [SHA256SUMS](SHA256SUMS) verifies copied files.

This collection adds this README, attribution metadata, and checksums.
The original per-skill LICENSE.txt is included unchanged.
These additions do not imply upstream endorsement. Collection-authored documentation uses the repository’s [Apache-2.0 default](../../../LICENSE); imported files retain the license above.

## Requirements and permissions

Python packages reportlab, pdfplumber, and pypdf; Poppler for rendering; file access and an image viewer. No required cloud API.

## Import or use

Follow the [collection import guide](../../IMPORT.md). Select this exact directory,
`skills/openai/pdf`, or its `SKILL.md` in Chatbook’s local Skills library.
Keep the entire directory, including licenses, references, scripts, and assets.
Import does not install dependencies or authorize execution. Host-specific tool
names and paths remain upstream originals; see the guide before running them.

Example request: “Create a two-page reference guide and check its rendered pages.”

## Verification and updates

Content version: **1.0.0**, pinned to the revision above. Directory import and
file-preservation results are recorded in [verification.json](../../verification.json).
Runtime task outcomes, live LLM/API calls, and server/Codex/Claude/OpenClaw host
imports are untested unless that report explicitly says otherwise.

Updates are manual: compare upstream at a new commit, recheck its license and
dependencies, refresh attribution and checksums, and repeat the import check.
Keep customized copies separately so an update does not overwrite them.
