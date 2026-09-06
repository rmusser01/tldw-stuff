# chatbook-docx

Create, edit and review Word .docx documents from supplied material or Chatbook notes, preserving document structure and checking the delivered file.

Example request: “Turn these project notes into a Word decision brief with a recommendation, evidence, open questions and an action table.”

## Use and requirements

Use the [directory import guide](../../IMPORT.md) and select this directory or
its [SKILL.md](SKILL.md). Content version: **1.0.0**.

Requires an LLM, authorized local Python/file execution and **Python 3.10+ with
python-docx**. No account, network call or other skill is required to create
local files. Optional source retrieval and package installation require their own
available permissions. LibreOffice and a suitable PDF/image viewer are optional
for rendering; workbook formula recalculation requires a spreadsheet engine.
Import does not install these dependencies or approve execution.

The [example](scripts/create_report.py) is a small runnable starting point with
fictional data, not a universal converter or completed user deliverable. From
this skill directory, in an environment with the dependency already installed:

```bash
python scripts/create_report.py example.docx
```

The output directory must exist. The example refuses to overwrite an existing
file. Adapt its content or write a task-specific script for real work.
[Editing guidance](references/editing.md) covers existing files and verification.

## Authorship and license

Original workflows, guidance and example code by **tldw-stuff contributors**,
licensed [Apache-2.0](LICENSE.txt). These are independently authored Office
workflows; no Anthropic proprietary Office skill text or code is distributed.
No claim of complete feature parity or endorsement is made.

The existing [Nous Research Hermes docx pack](../../hermes/docx/README.md)
was consulted as a capability reference. Its MIT-licensed helpers remain in their
original optional pack; none are copied or required here. Public library APIs
were checked against the sources recorded in [PROVENANCE.json](PROVENANCE.json).
Library implementations and documentation are not bundled or relicensed.
[SHA256SUMS](SHA256SUMS) records the distributed files.

## Verification and maintenance

See [verification.json](../../verification.json) for the exact Chatbook revision,
native import result, installed library versions and executed example/edit checks.
No live LLM evaluation, Office UI interaction, other-host import, visual rendering
or spreadsheet-engine recalculation has been tested. Content checks and pending
layout/calculation checks are distinguished in the skill itself.

When updating, review the public APIs, exercise the example and relevant edit
cases, repeat the native import, and refresh provenance checksums and the report.
