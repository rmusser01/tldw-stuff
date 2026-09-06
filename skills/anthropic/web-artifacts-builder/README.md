# Web Artifacts Builder

Anthropic’s skill for creating React/TypeScript interfaces and bundling them into
a single HTML artifact. It supplies project setup and bundling helpers, beyond
the visual guidance in the separate frontend-design skill.

## Attribution and files

- Author/publisher: **Anthropic, PBC and upstream contributors**.
- Source: [anthropics/skills — web-artifacts-builder](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/web-artifacts-builder).
- Revision: `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`; retrieved 2026-09-05.
- [Upstream history and contributors](https://github.com/anthropics/skills/commits/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/web-artifacts-builder).
- Anthropic skill files: [Apache-2.0](LICENSE.txt), copied unchanged.
- Bundled shadcn/ui components: [MIT](SHADCN_LICENSE.txt); see [third-party attribution](THIRD_PARTY_NOTICES.md).
- [SKILL.md](SKILL.md), [setup script](scripts/init-artifact.sh), [bundler](scripts/bundle-artifact.sh), and [component archive](scripts/shadcn-components.tar.gz) retain their native paths and bytes.
- [UPSTREAM.json](UPSTREAM.json) records source paths, revisions, hashes, and executable flags. [SHA256SUMS](SHA256SUMS) verifies copied files.

This collection adds documentation, attribution metadata, checksums, and a copy
of shadcn/ui’s MIT notice. No upstream endorsement is implied. New collection
documentation follows the repository’s [Apache-2.0 default](../../../LICENSE).

## Requirements and behavior

Requires Bash, Node.js, npm/pnpm, a writable project directory, package-registry
network access, and a browser for viewing the HTML output. Upstream documents
Node 18+, but uses moving package versions; those dependency combinations have
not been build-tested here.

The setup script can install pnpm globally when it is absent, downloads project
dependencies, and writes a React/Vite project. The bundler installs more packages
and removes `dist/` and `bundle.html` in its working directory before rebuilding.
Run it only in the intended artifact project. Review the scripts before execution.
Its Claude artifact-display step does not register an artifact with Chatbook;
viewing or serving the output requires the appropriate host/browser workflow.

## Import and use

Follow the [Chatbook directory import guide](../../IMPORT.md), selecting this
exact directory or its SKILL.md. Import preserves files and leaves the skill
untrusted; it does not install dependencies or grant execution permissions.
Follow the original skill’s setup and bundling instructions after reviewing them.

Example request: “Build an interactive comparison tool and bundle it as a single
HTML file I can open in a browser.”

## Verification and updates

Content version: **1.0.0**. Native Chatbook import, stored byte preservation,
archive-member safety, and Bash syntax results are in
[verification.json](../../verification.json). No package installation, full build,
visual preview, live LLM workflow, or other-host import was exercised.

Keep customized copies separately. To update, compare a new upstream revision,
review dependency and license changes, refresh attribution/checksums, and repeat
import verification.
