---
name: chatbook-xlsx
description: Create, edit and analyze Excel .xlsx workbooks from supplied tables or Chatbook material, preserving formulas and distinguishing calculated results from cached values.
license: Apache-2.0
metadata:
  author: tldw-project
  version: "1.0.0"
---

# Excel workbooks

Produce an editable `.xlsx` with traceable inputs and inspectable calculations.
Use openpyxl through available authorized Python execution. The skill is
standalone: no account or Hermes installation is required. Local execution and
filesystem access must actually be available; otherwise provide the table/model
specification and state that a workbook has not been generated.

## Understand the data

Determine the intended question, units, currency, date range and source tables
from the request. Retrieve full relevant Chatbook passages when notes are the
source. Keep missing values distinct from zero, preserve identifiers with leading
zeros, and retain source links or IDs. Do not turn estimates into observations.

For existing workbooks, inventory sheets, formulas, tables, names, charts,
merged ranges and relevant formatting before editing. Load with formulas retained
for any workbook you intend to save. Keep a separate output unless replacement
was requested. Macro-enabled or complex feature-heavy workbooks need explicit
preservation planning; the bundled example targets ordinary `.xlsx` files.

## Build a useful model

Separate assumptions/inputs from derived values, using sheets when that improves
clarity. Prefer formulas for relationships the user should be able to change.
Label units, style input cells consistently, choose appropriate date/currency/
percentage formats, and use frozen headers and filters for larger tables.
Distinguish an empty cell, an unavailable observation and a computed zero.

[The runnable example](scripts/create_workbook.py) builds a small fictional cost
model with formulas, validation and a chart. Replace its data for real work.
Resolve its path from the skill directory. Use
[editing and calculation guidance](references/editing.md) for existing files,
CSV input, structural edits and recalculation.

For analysis, inspect data types, missingness, duplicates and grouping assumptions
before calculating results. Write transformations and assumptions into a notes
sheet when they affect interpretation. Choose charts that expose the relevant
comparison; include units and avoid a misleading axis or unsupported precision.

## Check calculations and presentation

Reopen with `data_only=False` and confirm values, formulas, ranges and changed
cells. Independently calculate a few representative totals from the source,
including a boundary case such as a blank input or zero quantity. This checks the
model's intended arithmetic, not execution of Excel formulas.

openpyxl writes formulas but does not evaluate them. Setting recalculation-on-open
is a request to an application, not evidence that the results exist. If Excel or
LibreOffice is available, recalculate a separate copy, check cached values and
error cells, and compare the formulas/features preserved by the round trip.
Otherwise state that recalculation is pending; do not invent cached results.

Inspect column widths, number formats, headers and print areas. When a spreadsheet
viewer or rendered preview is available, check the affected sheets visually.
Structural read-back cannot prove that every cell displays without clipping.

Deliver the workbook path, relevant findings/assumptions and the exact verification
limits. Import does not install dependencies, execute macros, publish files or
write notes automatically.
