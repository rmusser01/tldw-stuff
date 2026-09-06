# chatbook-knowledge-capture

Chatbook note adaptation of **notion-knowledge-capture**, published in OpenAI's skills repository
and authored by **Notion Labs, Inc.** It retains the workflow's purpose while
using Chatbook note operations and Markdown content.

## Attribution and changes

- [Original source](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/notion-knowledge-capture) and [history/contributors](https://github.com/openai/skills/commits/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/notion-knowledge-capture).
- Upstream revision: `49f948faa9258a0c61caceaf225e179651397431`, retrieved 2026-09-05.
- Original and adapted skill content: [MIT](LICENSE.txt), with the Notion Labs copyright notice preserved.
- Adaptations by tldw-stuff contributors: tool mapping, workflow and template changes, behavior fixtures, and update fallback.
- [UPSTREAM.json](UPSTREAM.json) records original source hashes and changed output hashes. [SHA256SUMS](SHA256SUMS) checks the distributed content.

The adapter removes Notion authentication/setup, database property writes,
Notion page mentions and branding. Knowledge metadata is ordinary note text.
Collection documentation follows the repository's [Apache-2.0 default](../../../LICENSE).
No endorsement by Notion, OpenAI or Chatbook's upstream authors is implied.

## Import and requirements

Use the [directory import guide](../../IMPORT.md). Select this exact directory
or its [SKILL.md](SKILL.md). No Notion account or MCP service is needed.

An LLM and supplied source content suffice for drafting. Reading or saving library
notes requires enabled, authorized Chatbook `search_notes`, `expand_document`,
`create_note`, or `update_note` tools as appropriate. The adapter targets local
database notes; it does not configure File Notes, server note scopes, note sync,
sharing or scheduled actions. [Tool details](reference/chatbook-notes.md) describe
the observed version/read limitations and fallback to a draft.

## Verification and updates

Content version: **1.0.0**. Tested against the Chatbook revision and native import
results in [verification.json](../../verification.json). Behavioral cases in
[evaluations/cases.json](evaluations/cases.json) are review scenarios, not a claim
that an LLM passed them. No live LLM, user database, account, sharing operation or
other-host import was exercised. See the report for any isolated note-tool checks.

When updating, compare upstream workflow/template changes, preserve the MIT
notice, review Chatbook's real tool schemas, refresh the provenance hashes, and
repeat import and relevant behavior checks.
