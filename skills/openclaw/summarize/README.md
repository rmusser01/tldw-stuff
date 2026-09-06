# summarize

Summarize articles, files, videos, and podcasts through summarize.sh.

## Attribution and files

- Author/publisher: **OpenClaw Foundation and upstream contributors**.
- Original source: [openclaw/openclaw / skills/summarize](https://github.com/openclaw/openclaw/tree/047587a542ce205ee78354fbd88ba8ec05c07844/skills/summarize).
- Revision: `047587a542ce205ee78354fbd88ba8ec05c07844` (retrieved 2026-09-05).
- License: [MIT](LICENSE.txt). All original copyright and attribution notices are retained.
- [Upstream contributors and file history](https://github.com/openclaw/openclaw/commits/047587a542ce205ee78354fbd88ba8ec05c07844/skills/summarize).
- [SKILL.md](SKILL.md) and all its upstream supporting files are copied unchanged.
- [UPSTREAM.json](UPSTREAM.json) records every source path, byte count, hash, and executable flag; [SHA256SUMS](SHA256SUMS) verifies copied files.

This collection adds this README, attribution metadata, and checksums.
The upstream root MIT license is also copied here as LICENSE.txt.
These additions do not imply upstream endorsement. Collection-authored documentation uses the repository’s [Apache-2.0 default](../../../LICENSE); imported files retain the license above.

## Requirements and permissions

The external summarize CLI. Fetching URLs needs network access; LLM summaries require provider configuration and may send source content to that provider. Firecrawl and Apify are optional external services. This is separate from tldw_server’s ingestion API.

## Import or use

Follow the [collection import guide](../../IMPORT.md). Select this exact directory,
`skills/openclaw/summarize`, or its `SKILL.md` in Chatbook’s local Skills library.
Keep the entire directory, including licenses, references, scripts, and assets.
Import does not install dependencies or authorize execution. Host-specific tool
names and paths remain upstream originals; see the guide before running them.

Example request: “Summarize an article URL or extract a YouTube transcript.”

## Verification and updates

Content version: **1.0.0**, pinned to the revision above. Directory import and
file-preservation results are recorded in [verification.json](../../verification.json).
Runtime task outcomes, live LLM/API calls, and server/Codex/Claude/OpenClaw host
imports are untested unless that report explicitly says otherwise.

Updates are manual: compare upstream at a new commit, recheck its license and
dependencies, refresh attribution and checksums, and repeat the import check.
Keep customized copies separately so an update does not overwrite them.
