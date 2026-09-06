# statistical-analysis

Choose statistical methods, check assumptions and report effects and uncertainty.

Example request: “Review this analysis plan and check assumptions on the supplied synthetic dataset.”

## Source and license

- Author/publisher: **K-Dense Inc.**.
- [Original source](https://github.com/K-Dense-AI/scientific-agent-skills/tree/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/statistical-analysis) and [history/contributors](https://github.com/K-Dense-AI/scientific-agent-skills/commits/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/statistical-analysis).
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

The assumption-check helper imports numpy, pandas, scipy, matplotlib and seaborn; some diagnostics use statsmodels. Other examples require pingouin, PyMC or ArviZ with the upstream-described versions. Use an authorized Python environment; dependencies are not installed by import. Source compatibility claims are upstream claims, not local runtime verification. This snapshot includes simplified statistical rules and examples; import checks do not validate their scientific correctness.

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
