# GitHub Address Comments

OpenAI’s workflow for inspecting a pull request’s review feedback and addressing
selected comments, with a Python helper that fetches GitHub comments and threads.

## Attribution and files

- Author/publisher: **OpenAI and upstream contributors**.
- Source: [openai/skills — gh-address-comments](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-address-comments).
- Revision: `49f948faa9258a0c61caceaf225e179651397431`; retrieved 2026-09-05.
- [Upstream history and contributors](https://github.com/openai/skills/commits/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-address-comments).
- License: [Apache-2.0](LICENSE.txt); original notices preserved.
- [SKILL.md](SKILL.md) and all upstream supporting files retain native paths and bytes.
- [UPSTREAM.json](UPSTREAM.json) lists every source file, checksum, and executable flag; [SHA256SUMS](SHA256SUMS) verifies the snapshot.

This collection adds documentation, attribution metadata, and checksums. No
upstream endorsement is implied. Collection documentation follows the
repository’s [Apache-2.0 default](../../../LICENSE).

## Requirements and behavior

Python 3.10+, Git, an authenticated GitHub CLI (`gh`), network access to GitHub,
and a checkout whose current branch has an associated PR. Resolve the helper
relative to the imported skill directory, then run it from the target checkout.
The helper reads PR content and prints JSON; it does not itself post comments or
edit code. The surrounding workflow can make code changes using host tools.

Upstream instructions mention Codex sandbox escalation and credential scopes.
These are host-specific guidance, not permission grants through Chatbook.
`agents/openai.yaml` and the GitHub icons are preserved as upstream host metadata.

Known limitations in this pinned helper, confirmed with offline fixtures:

- PR lookup uses the head repository instead of the base repository, so fork PRs
  can be queried against the wrong repository.
- Connections that finish paginating reset their cursor while other connections
  continue; previously fetched comments or reviews can be duplicated.
- Each inline thread requests only its first 100 comments, without pagination.

Verify the PR’s base repository and completeness of retrieved feedback before
acting on it. The source is preserved unchanged; import verification does not
certify that the helper retrieves every comment.

## Import and use

Follow the [Chatbook directory import guide](../../IMPORT.md), selecting this
exact directory or its SKILL.md. Import preserves files and leaves the skill
untrusted; it does not install dependencies or grant execution permissions.

Example request: “Inspect the review threads on this branch’s PR and help me address the selected feedback.”

## Verification and updates

Content version: **1.0.0**. See [verification.json](../../verification.json) for
the tested Chatbook revision and results. Python syntax, native Chatbook directory import, and offline helper fixtures were checked. Fixtures covered basic retrieval and demonstrated the fork and pagination limitations above. No live GitHub helper run, comment posting, or code-fixing workflow was exercised.
Other-host imports were not tested.

Keep customized copies separately. To update, review a new upstream revision,
refresh source files, licenses, attribution and checksums, and repeat import
verification.
