# tldw-stuff setup plan

**Goal:** Publish a small optional-content repository under rmusser01/tldw-stuff.

**Architecture:** Category READMEs index self-contained packs in native formats.
Use manual import and selective downloads, with no runtime or automatic installer.

**Tech stack:** Markdown, Git, and GitHub; no runtime dependencies.

**Spec:** [Repository design](../../repository-design.md).

## Constraints

Keep existing application repositories unchanged. Preserve provenance and
per-item licenses. Do not claim unverified cross-app compatibility. Start with
templates and empty collections rather than copying existing application data.

## Setup

- [x] Write root documentation, collection indexes, contribution and pack templates.
- [x] Check local Markdown links, whitespace, file sizes, and license presence.
- [ ] Initialize main, create the public GitHub repository, and push the scaffold.
- [ ] Verify the published branch and clean local checkout.
