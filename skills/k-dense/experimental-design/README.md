# experimental-design

Plan study designs and generate seeded allocation schedules and DOE matrices.

Example request: “Propose a blocked experiment and produce a reproducible allocation schedule for this synthetic study.”

## Source and license

- Author/publisher: **K-Dense Inc.**.
- [Original source](https://github.com/K-Dense-AI/scientific-agent-skills/tree/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/experimental-design) and [history/contributors](https://github.com/K-Dense-AI/scientific-agent-skills/commits/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/experimental-design).
- Pinned revision: `1e5eeffbdad3749125afe7ab48a39694e27f181c`, retrieved **2026-09-05**.
- License: [MIT](LICENSE.txt). The upstream content retains MIT, including the original copyright notice. The repository Apache default does not replace that license.
- Upstream instructions, supporting files and file modes are unchanged. No endorsement is implied.
- [UPSTREAM.json](UPSTREAM.json) records source paths and hashes; [SHA256SUMS](SHA256SUMS) checks the copied payload and license.

This collection README is original repository documentation under the
[Apache-2.0 default](../../../LICENSE). It does not relicense the upstream files.

## Import and requirements

Follow the [directory import guide](../../IMPORT.md). Select this exact directory
or its [SKILL.md](SKILL.md), preserving all accompanying files. Import does not
install packages, approve scripts, supply accounts or execute skill instructions.

Guidance works from supplied context. Bundled Python helpers need Python 3.10+, numpy and pandas; DOE matrices also require pyDOE3. Upstream recommends uv for installation, which import does not run. Script execution and file output require authorized local tools. Related scientific skills and live experiment infrastructure are not installed.

## Verification and updates

Content version: **1.0.0 collection snapshot**. See [verification.json](../../verification.json)
for the exact Chatbook commit and native import/checksum results. The UI and
other-host imports were not exercised. Source files are treated as content during
maintenance, not instructions to run tools or contact external services.

Bundled evaluation cases, where present, are upstream fixtures; no live LLM
evaluation was run. Helper runtime checks, if any, are listed explicitly in the
verification report; import success does not certify host compatibility or output
quality.

For updates, review the pinned source diff and licenses, copy the selected
complete directory, refresh manifests/checksums, repeat import and relevant
helper checks, and record observed limits. Do not silently rewrite upstream text.
