# Official skill repository review — 2026-09-05

## Scope and selection

The collection contains 69 skills: 64 publisher packs (two with documented
reference-link relocations), two Chatbook note adaptations and three original
Chatbook Office workflows. The publisher/adaptation payloads total 2,765,384 bytes,
including licenses; original Office files and collection metadata add more.

| Repository | Pinned revision | Distributed items |
| --- | --- | --- |
| anthropics/skills | `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` | 7 unchanged |
| openai/skills | `49f948faa9258a0c61caceaf225e179651397431` | 3 unchanged; 2 Chatbook adaptations of Notion Labs skills |
| openclaw/openclaw | `047587a542ce205ee78354fbd88ba8ec05c07844` | 3 unchanged |
| NousResearch/hermes-agent | `245e48008fa814b3251f50755eb656bd9fb86cb1` | 42 of 60 bundled defaults |

The fetched `openclaw/skills` endpoint returned 404. OpenClaw’s bundled skills
were available under `openclaw/openclaw/skills`; that is the source used here.
A third-party/community registry listing is not treated as an official OpenClaw
license grant. This is a first selection, not a complete mirror or certification
of every skill in these repositories.

## Why these skills

- Anthropic: frontend design and internal communications are small reusable workflows; MCP building and browser testing provide supporting developer references and helpers. The requested web-artifacts-builder adds project setup and single-file HTML bundling, with Apache-2.0 skill files and MIT shadcn/ui component notices. The selected skill-creator adds skill drafting, evaluation, and packaging; its automated evaluation is Claude-specific.
- OpenAI: notebooks support research artifacts; threat modeling is a focused developer reference. The selected gh-address-comments adds PR-feedback handling, with pinned helper limitations documented in its README.
- OpenClaw: diagrams and video-frame extraction support knowledge and media workflows; gog adds the selected Google Workspace CLI integration.
- Hermes: the selected default collection covers office files, meeting follow-up, weekly review, research, creative work and integrations. Its DOCX, PowerPoint and XLSX skills carry explicit Nous Research MIT notices. The collection preserves host-specific requirements rather than claiming automatic portability.
- Chatbook adaptations: the selected Notion meeting-preparation and knowledge-capture workflows now use Chatbook notes. Notion Labs remains credited as the original author; OpenAI is the source repository, not the inferred copyright owner.
- Anthropic theme-factory: the selected palette/font themes and PDF showcase complement artifact creation.

## Deferred or linked only

- Anthropic’s [docx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/docx/LICENSE.txt), [pdf](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/pdf/LICENSE.txt), [pptx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/pptx/LICENSE.txt), and [xlsx](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/xlsx/LICENSE.txt) carry separate source-available terms with copying/distribution restrictions. They are linked here and not redistributed.
- Anthropic’s [doc-coauthoring](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/doc-coauthoring) is a useful candidate, but has no per-skill license file or frontmatter license at this revision, and the repository has no root license. The README’s statement that many skills are Apache-licensed does not identify this skill’s terms. Deferred pending a specific license grant.
- Remaining candidates can be evaluated individually. Publisher branding, host dependencies and runtime behavior require per-item review; attribution alone does not settle licensing or compatibility.

## Attribution and preservation

Unmodified publisher folders contain byte-identical source files, applicable
licenses, publisher/contributor credit, source/history links, full commit SHAs,
and per-file checksums. Chatbook adaptations identify changed files and original
source hashes. OpenClaw and Hermes root MIT notices are copied into each selected
skill, alongside more specific notices where present. Original copyright notices
remain unchanged; no individual
copyright ownership is inferred from commit authorship. Publisher names identify
provenance and do not imply endorsement.

## Verification scope

[Native import and helper results](verification.json) record exactly what ran.
The copied instructions and shipped helpers were inspected as content; they did
not become repository-maintenance instructions. Import left the skills untrusted.
The review identifies dependencies and data-transfer requirements; it is not an
exhaustive security audit or evaluation of LLM behavior. Upstream model names,
commands, and documentation references are pinned examples that may age.

Upstream trailing-whitespace lines are retained to preserve exact source
hashes; they are listed in the verification report. New collection documentation
and attribution files pass the whitespace check.

## Office and note verification

All 46 additions were exercised through native Chatbook directory import.
Hermes google-workspace and grounded-citations each lose a required underscore-led
helper in that importer; their collection READMEs direct script users to the
complete repository bundles. Other new bundles preserve every file.

35 Python files parsed and five shell scripts passed Bash syntax checks. Real
Office helper create/read smoke checks and Chatbook note-tool calls used isolated
fixtures; no user database, live service, scheduler or account was touched.
Six adapter behavior scenarios are included for future LLM evaluation and have
not been represented as executed model tests.

## Original Office equivalents

The requested Word, PowerPoint and Excel equivalents are independently authored
Apache-2.0 Chatbook workflows using public Python library APIs. Each includes a
small runnable creation example and targeted editing/verification guidance.
The Nous Research Hermes Office skills were consulted as capability references;
no helpers are duplicated and no proprietary Anthropic Office text is adapted.
Original packs record that distinction and their references in PROVENANCE.json.

All three imported with every file preserved. The imported examples passed
creation, read-back and overwrite-protection checks; targeted edits exercised
DOCX comments/run formatting, PPTX titles/notes and XLSX formulas/charts/validation.
Python arithmetic checked workbook expectations without asserting that an Excel
engine had evaluated the formulas. Rendering, spreadsheet-engine recalculation
and LLM workflow behavior remain untested. These workflows are practical
alternatives, not a claim of complete feature parity.

## Selected community skills

The user selected these nine following the hub/collection review:

- [property-based-testing](trailofbits/property-based-testing/COLLECTION.md) — Trail of Bits, CC-BY-SA-4.0; source `trailofbits/skills@d3323cefbcf645678b8dc481de204b02ad3d02dc`.
- [customer-research](corey-haines/customer-research/README.md) — Corey Haines, MIT; source `coreyhaines31/marketingskills@5b2c0007766c6a1cf1d53fd8fc73e979e0821022`.
- [content-strategy](corey-haines/content-strategy/README.md) — Corey Haines, MIT; source `coreyhaines31/marketingskills@5b2c0007766c6a1cf1d53fd8fc73e979e0821022`.
- [copy-editing](corey-haines/copy-editing/README.md) — Corey Haines, MIT; source `coreyhaines31/marketingskills@5b2c0007766c6a1cf1d53fd8fc73e979e0821022`.
- [teach](matt-pocock/teach/README.md) — Matt Pocock, MIT; source `mattpocock/skills@3cca18b368ae95cdbdebbff572ccafa662551015`.
- [grilling](matt-pocock/grilling/README.md) — Matt Pocock, MIT; source `mattpocock/skills@3cca18b368ae95cdbdebbff572ccafa662551015`.
- [scientific-critical-thinking](k-dense/scientific-critical-thinking/README.md) — K-Dense Inc., MIT; source `K-Dense-AI/scientific-agent-skills@1e5eeffbdad3749125afe7ab48a39694e27f181c`.
- [experimental-design](k-dense/experimental-design/README.md) — K-Dense Inc., MIT; source `K-Dense-AI/scientific-agent-skills@1e5eeffbdad3749125afe7ab48a39694e27f181c`.
- [statistical-analysis](k-dense/statistical-analysis/README.md) — K-Dense Inc., MIT; source `K-Dense-AI/scientific-agent-skills@1e5eeffbdad3749125afe7ab48a39694e27f181c`.

The property-based-testing pack retains its original README and logo, with a
separate COLLECTION.md for import information. Customer-research and
content-strategy each referenced guides outside their skill directory; those
guides are now bundled unchanged and only the relative-link paths were adjusted.
All SKILL.md files are unchanged. Imported files and source/output checksums were
verified; helper/evaluation limits are recorded in verification.json.
