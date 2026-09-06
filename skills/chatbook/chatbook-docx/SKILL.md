---
name: chatbook-docx
description: Create, edit and review Word .docx documents from supplied material or Chatbook notes, preserving document structure and checking the delivered file.
license: Apache-2.0
metadata:
  author: tldw-stuff contributors
  version: "1.0.0"
---

# Word documents

Produce an editable `.docx` that carries the user's content and intended structure.
Use supplied material first. If the user selects Chatbook notes or retrieved
sources, obtain their full relevant content through available authorized tools;
search snippets alone are insufficient for an attributed report. Keep source IDs,
links and dates with the claims they support. Missing owners or dates stay unresolved.

## Choose the operation

- **New document:** establish the audience and purpose from the request. Draft the
  argument or outline, then implement with python-docx. A short brief usually
  needs a recommendation, supporting evidence, alternatives and next actions;
  use the user's structure when supplied.
- **Existing document:** inspect headings, tables, sections, headers, footers and
  the specific text to change before editing. Keep its styles and page setup.
  Save a separate output unless the user requested replacement.
- **Review:** separate proposed edits from source text. Native comments are an
  option with python-docx 1.2+. Tracked revisions need a tool that actually
  supports them; a rewritten paragraph is not a tracked change.

Use [the working example](scripts/create_report.py) for a small heading/table
report, and [editing and review guidance](references/editing.md) when modifying
an existing document. The example contains fictional data: replace it for real work.
Resolve bundled paths from this skill's directory, not the workspace directory.

## Execute in the available environment

Use an authorized local Python execution capability with python-docx. Do not
assume a tool named `terminal`, a package installer, or filesystem access exists.
When execution is unavailable, return the drafted content and proposed filename;
do not claim an attachment was created. Local file creation needs no external
account. Network access is only needed for requested sources or dependency setup.
Importing the skill does not install dependencies or authorize execution.

## Compose and check

Use named paragraph styles for headings, body and lists so the document remains
navigable. Set sensible margins and a consistent type scale; reuse a supplied
brand template. Use tables for comparable records, explicit units for measurements,
and captions/source text for evidence. Keep headings with the following paragraph;
avoid blank-line padding and unnecessary forced page breaks.

Reopen the output with python-docx and compare the required sections, table
records, numbers and changed text with the source. After edits, check retained
formatting and content outside the changed passage. This verifies structure and
content, not pagination.

When a renderer and image inspection are available, export a PDF into a fresh
output directory, inspect every page, and fix clipped tables, orphan headings,
font substitutions and excessive whitespace. LibreOffice can render `.docx`;
python-docx cannot. Page-number and contents fields require a document engine to
update their results. If rendering is unavailable, report the precise unchecked
layout aspects instead of declaring visual approval.

Deliver the actual `.docx` path, a brief account of the change and any unresolved
source or verification limits. Exporting a file does not publish it or update
Chatbook notes automatically.
