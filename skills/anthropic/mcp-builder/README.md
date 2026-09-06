# mcp-builder

Design and evaluate MCP servers and tools.

## Attribution and files

- Author/publisher: **Anthropic, PBC and upstream contributors**.
- Original source: [anthropics/skills / skills/mcp-builder](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/mcp-builder).
- Revision: `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` (retrieved 2026-09-05).
- License: [Apache-2.0](LICENSE.txt). All original copyright and attribution notices are retained.
- [Upstream contributors and file history](https://github.com/anthropics/skills/commits/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/mcp-builder).
- [SKILL.md](SKILL.md) and all its upstream supporting files are copied unchanged.
- [UPSTREAM.json](UPSTREAM.json) records every source path, byte count, hash, and executable flag; [SHA256SUMS](SHA256SUMS) verifies copied files.

This collection adds this README, attribution metadata, and checksums.
The original per-skill LICENSE.txt is included unchanged.
These additions do not imply upstream endorsement. Collection-authored documentation uses the repository’s [Apache-2.0 default](../../../LICENSE); imported files retain the license above.

## Requirements and permissions

Python or Node.js, an MCP SDK, and documentation access. The optional Python evaluation harness requires scripts/requirements.txt, an Anthropic API key, and access to the selected MCP server; it can execute tools and send their results to Anthropic. Pass a currently available model with --model; the unchanged upstream default is historical.

## Import or use

Follow the [collection import guide](../../IMPORT.md). Select this exact directory,
`skills/anthropic/mcp-builder`, or its `SKILL.md` in Chatbook’s local Skills library.
Keep the entire directory, including licenses, references, scripts, and assets.
Import does not install dependencies or authorize execution. Host-specific tool
names and paths remain upstream originals; see the guide before running them.

Example request: “Help design MCP tools for a read-only document search service.”

## Verification and updates

Content version: **1.0.0**, pinned to the revision above. Directory import and
file-preservation results are recorded in [verification.json](../../verification.json).
Runtime task outcomes, live LLM/API calls, and server/Codex/Claude/OpenClaw host
imports are untested unless that report explicitly says otherwise.

Updates are manual: compare upstream at a new commit, recheck its license and
dependencies, refresh attribution and checksums, and repeat the import check.
Keep customized copies separately so an update does not overwrite them.
