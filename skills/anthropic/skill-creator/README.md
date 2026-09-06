# Skill Creator

Anthropic’s workflow for drafting, testing, reviewing, and improving skills,
with evaluation agents, benchmark helpers, an HTML review viewer, and a packager.

## Attribution and files

- Author/publisher: **Anthropic, PBC and upstream contributors**.
- Source: [anthropics/skills — skill-creator](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/skill-creator).
- Revision: `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`; retrieved 2026-09-05.
- [Upstream history and contributors](https://github.com/anthropics/skills/commits/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/skill-creator).
- License: [Apache-2.0](LICENSE.txt); original notices preserved.
- [SKILL.md](SKILL.md) and included upstream supporting files retain native paths and bytes; only the empty scripts/__init__.py marker is omitted for import compatibility.
- [UPSTREAM.json](UPSTREAM.json) lists included source files, checksums and executable flags, and records the omitted empty marker; [SHA256SUMS](SHA256SUMS) verifies the snapshot.

This collection adds documentation, attribution metadata, and checksums. No
upstream endorsement is implied. Collection documentation follows the
repository’s [Apache-2.0 default](../../../LICENSE).

## Requirements and behavior

Python 3.10+ and PyYAML are needed for the Python helpers and validator/packager.
Automated evaluation and description optimization require an authenticated Claude
CLI (`claude -p`), network access, and model usage. They create temporary command
files under a project’s `.claude/commands/` directory. Importing into Chatbook
does not supply Claude, agent orchestration, or equivalent runtime tools.

The review viewer reads evaluation outputs and can write feedback. Its default
server mode attempts to terminate an existing listener on the chosen port
(default 3117) before binding localhost. Prefer `--static /path/to/review.html`
when only an HTML review file is needed. The HTML references Google Fonts and
SheetJS on external hosts; opening it may make network requests.

Run module-based helpers from the skill directory, for example
`python -m scripts.package_skill /path/to/my-skill /path/to/output`.
The upstream packager’s `utils/package_skill.py` usage examples are stale;
the preserved implementation lives under `scripts/`. Its validator checks basic
frontmatter; it is not a complete Chatbook compatibility or safety validator.
Package only the intended skill directory and put output outside that directory.

## Import and use

Follow the [Chatbook directory import guide](../../IMPORT.md), selecting this
exact directory or its SKILL.md. The empty `scripts/__init__.py` marker is omitted
so the complete distributed bundle passes directory and ZIP import. Python 3
namespace-package execution (`python -m scripts.package_skill`) is verified.
All included files are preserved and the skill remains pending trust review.
Import does not install dependencies or grant execution permissions.

Example request: “Help me improve a draft skill, create representative test prompts, and package the reviewed version.”

## Verification and updates

Content version: **1.0.1**. See [verification.json](../../verification.json) for
the tested Chatbook revision and results. Validator accepted a valid fixture and rejected missing-description frontmatter; the packager preserved fixture file bytes and omitted cache files. Python syntax and native Chatbook directory import were checked. Claude evaluations, browser rendering, and viewer server mode were not run.
Other-host imports were not tested.

Keep customized copies separately. To update, review a new upstream revision,
refresh source files, licenses, attribution and checksums, and repeat import
verification.
