---
name: chatbook-pptx
description: Build and revise editable PowerPoint .pptx presentations from a brief or Chatbook sources, with an audience-focused narrative and content and visual checks.
license: Apache-2.0
metadata:
  author: tldw-project
  version: "1.0.0"
---

# PowerPoint presentations

Build an editable `.pptx` around the audience's question or decision. Establish
purpose, audience, approximate presentation length and any supplied template
from the user's request. Use reasonable defaults when they do not affect the
message; ask only for missing information that changes the result materially.

## Shape the story

Extract the claims and evidence from the supplied material or full relevant
Chatbook source passages. Distinguish measured results, plans and assumptions.
Keep source links or IDs beside the evidence or in speaker notes. Never invent
measurements to make a chart or populate an example deck.

Choose an order that makes the conclusion understandable: for example, situation,
evidence, recommendation, tradeoffs and requested action. Use takeaway titles
and one main point per slide. Put supporting detail in notes or an appendix when
it distracts from the argument. Match the user's intended length instead of
forcing a fixed slide count.

## Author or edit

Use python-pptx through an available authorized execution tool. For new slides,
start with [the runnable example](scripts/create_deck.py) or a supplied template.
The example's data is fictional; adapt it before delivering user work. Bundled
paths are relative to the skill directory. No Hermes installation is required.

Use editable text, tables and native charts where practical. For charts, include
units, time period and honest axes; choose a form that answers the comparison.
Use images when they contribute information and preserve their aspect ratio.
Use a restrained font/color system, clear hierarchy and sufficient contrast.
Split crowded slides instead of shrinking everything to unreadable text.

For existing decks, first inspect slide dimensions, masters/layouts, placeholders,
notes and the affected shapes. Preserve the existing brand and content outside
the requested change. Layout indices differ by template. Read
[editing and verification](references/editing.md) before replacing text or charts.

## Verify and deliver

Reopen the output and inspect the slide count, title order, required text,
speaker notes and chart values. Check that shapes intended to be visible are
inside slide bounds; bounds alone cannot detect text overflow or unwanted overlap.

When available, render the deck to PDF/slide images and inspect every slide for
cropping, overlaps, font substitutions and legibility. python-pptx does not
render. If no renderer or visual inspection tool is available, give the editable
deck and state that visual validation remains outstanding. Do not treat a
successful save as a successful presentation review.

Return the actual `.pptx` path with a short description and verification limits.
If no execution capability exists, provide the slide outline and notes without
claiming a file was created. Importing this skill does not install Python
packages, grant tool permissions, publish the deck or alter Chatbook notes.
