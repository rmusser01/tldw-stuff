# Editing, CSV input and calculation

## Keep formulas when editing

Use `load_workbook(path, data_only=False)` for edits. A separate
`load_workbook(path, data_only=True)` exposes saved formula results where present;
never save that values-only view over the working formula file. Results can be
absent or stale until a spreadsheet engine saves the workbook.

```python
from openpyxl import load_workbook

workbook = load_workbook("source.xlsx", data_only=False)
sheet = workbook["Costs"]
assert sheet["B2"].value == 2
assert sheet["D2"].value == "=B2*C2"
sheet["B2"] = 4
workbook.save("reviewed.xlsx")
```

This example expects the bundled starter. Identify the actual target range and
check existing content before applying it to a user workbook.

Inserting/deleting rows or columns with openpyxl does not automatically maintain
all dependent formulas, tables, charts or defined names. Plan the reference
changes, inspect dependents across sheets, and verify them afterward. Do not
promise a spreadsheet-app-style structural edit from a simple insert_rows call.

Normal charts can survive supported openpyxl round trips; it is incorrect to
assume every chart will always be dropped. Unsupported shapes/features can be
lost. Preserve the original and compare the features relevant to the user's file.
For `.xlsm`, retaining VBA requires the appropriate loading/saving options and
extension, and does not mean macros were understood, executed or verified.

## CSV and literal text

Read CSV with an explicit encoding and delimiter. Decide which columns are
identifiers, numbers, dates and text before converting; keep account codes and
other identifiers as strings. Imported text beginning with `=` should not
silently become a formula. For a cell that is intended to contain literal text:

```python
cell = sheet["A5"]
cell.value = "=not a formula"
cell.data_type = "s"
```

Apply this only to text fields; preserve intentionally authored formulas.
CSV itself has no reliable type metadata: spreadsheet applications can reinterpret
leading `=`, `+`, `-` or `@`. If exporting externally supplied text for a
spreadsheet app, choose and document a literal-text convention compatible with
that consumer, or provide typed `.xlsx` instead. A leading apostrophe changes
the stored CSV text and should not be added silently to authoritative source data.

## Formula and result checks

Excel formula names use the workbook formula syntax, which may differ from the
user's localized UI. Inspect resulting formulas after edits, especially quoted
sheet names, absolute references, ranges and inserted/deleted rows.

Recalculation flags do not evaluate formulas. Use an available spreadsheet engine
on an isolated output copy, inspect its diagnostics and ensure the output was
actually produced. Then compare known totals through a `data_only=True` load,
scan cells whose `data_type == "e"`, and confirm formulas are still present through
a separate formula load. Compare charts, names and formatting that matter to the
file; different spreadsheet engines can change unsupported features.

For the included example, independently expected line costs are 24 and 21, with
a grand total of 45. Changing quantity B2 from 2 to 4 changes the expected total
to 69. Those expectations are test oracles, not precomputed Excel cache values.

References: [formulas](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html)
and [structural edits](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html).
