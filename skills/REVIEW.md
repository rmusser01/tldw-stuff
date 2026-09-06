# Official skill repository review — 2026-09-05

## Scope and selection

Reviewed the official catalogs for tasks relevant to Chatbook, tldw_server,
and this optional content library. Selected 12 compact skills with identifiable
redistribution terms, complete supporting files, and practical writing,
research, media, or development uses. The selection totals 303,617 source bytes
including license copies; metadata and collection documentation add a little more.

| Official repository | Pinned revision | Selected |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f) | `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` | 4 |
| [openai/skills](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431) | `49f948faa9258a0c61caceaf225e179651397431` | 4 |
| [openclaw/openclaw](https://github.com/openclaw/openclaw/tree/047587a542ce205ee78354fbd88ba8ec05c07844) | `047587a542ce205ee78354fbd88ba8ec05c07844` | 4 |

The fetched `openclaw/skills` endpoint returned 404. OpenClaw’s bundled skills
were available under `openclaw/openclaw/skills`; that is the source used here.
A third-party/community registry listing is not treated as an official OpenClaw
license grant. This is a first selection, not a complete mirror or certification
of every skill in these repositories.

## Why these skills

- Anthropic: frontend design and internal communications are small reusable workflows; MCP building and browser testing provide supporting developer references and helpers.
- OpenAI: PDF work and notebooks fit research artifacts; threat modeling is a focused developer reference; API transcription complements local transcription.
- OpenClaw: diagrams, Whisper, video frames, and summarize.sh fit knowledge and media workflows with explicit external tool requirements.

## Deferred or linked only

- Anthropic’s [docx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/docx/LICENSE.txt), [pdf](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/pdf/LICENSE.txt), [pptx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/pptx/LICENSE.txt), and [xlsx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/xlsx/LICENSE.txt) carry separate source-available terms with copying/distribution restrictions. They are linked here and not redistributed. OpenAI’s explicitly Apache-licensed PDF skill is included instead.
- Anthropic’s [doc-coauthoring](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/doc-coauthoring) is a useful candidate, but has no per-skill license file or frontmatter license at this revision, and the repository has no root license. The README’s statement that many skills are Apache-licensed does not identify this skill’s terms. Deferred pending a specific license grant.
- Large art/font collections, duplicate skill-authoring systems, vendor branding, deployment tools, workplace connectors, device control, and account-management skills remain upstream for this initial collection. They can be evaluated individually later; attribution alone does not settle licensing or compatibility.

## Attribution and preservation

Each selected folder contains a byte-identical source snapshot, its applicable
license, publisher/contributor credit, source/history links, a full commit SHA,
and per-file checksums. The OpenClaw root MIT license is copied into each
selected skill. Original copyright notices remain unchanged; no individual
copyright ownership is inferred from commit authorship. Publisher names identify
provenance and do not imply endorsement.

## Verification scope

[Native import and helper results](verification.json) record exactly what ran.
The copied instructions and shipped helpers were inspected as content; they did
not become repository-maintenance instructions. Import left the skills untrusted.
The review identifies dependencies and data-transfer requirements; it is not an
exhaustive security audit or evaluation of LLM behavior. Upstream model names,
commands, and documentation references are pinned examples that may age.

Three upstream trailing-whitespace lines are retained to preserve exact source
hashes; they are listed in the verification report. New collection documentation
and attribution files pass the whitespace check.
