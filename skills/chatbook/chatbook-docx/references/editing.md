# Editing and review

Open the input with `docx.Document(path)`. Inventory body paragraphs and tables,
plus each section's headers and footers. Text in drawings, footnotes or revision
markup may not be included in ordinary paragraph iteration; do not describe that
iteration as a complete extraction of an arbitrary document.

## Preserve formatting during targeted edits

`paragraph.text = replacement` rebuilds the paragraph's runs. When changing text
inside one known run, update that run instead. A match spanning several runs
requires deliberate handling of their formatting and hyperlinks. Resolve the
specific occurrence using its surrounding paragraph/table, and verify the result.
Do not flatten the entire document to make a small substitution easier.

```python
from docx import Document

doc = Document("source.docx")
matches = [run for paragraph in doc.paragraphs for run in paragraph.runs
           if run.text == "Draft decision"]
if len(matches) != 1:
    raise ValueError("Expected one exact run; inspect split or repeated text")
matches[0].text = "Approved decision"
doc.save("reviewed.docx")
```

This narrow example edits body runs only. Inspect nested tables, headers or
footers separately when they are within scope. Table-cell `.text` assignments
also replace rich run content; use them only where that is intended.

## Comments and revisions

With python-docx 1.2 or later, `Document.add_comment(runs, text, author, initials)`
anchors a comment to existing runs. Select the exact passage and verify both the
comment and unchanged passage after saving. Attribution should identify the
actual reviewer rather than impersonate a source author. Older library versions
may lack this API; check availability before using it.

If the request requires tracked changes, inspect available revision-capable tools.
The standalone example does not implement revision insertion or acceptance.
Preserve existing revisions and use a supported editor for complex review files;
otherwise provide an explicit proposed-change list alongside an unchanged original.
Never accept or reject existing revisions just to simplify extraction.

## Package and layout checks

A `.docx` is an OOXML ZIP package, not plain text. `zipfile.ZipFile.testzip()`
checks ZIP integrity only. Successful reopening checks library readability, not
all Word compatibility. Work on copies of complex files; inspect fields,
references, comments and revision markup affected by the edit.

If LibreOffice is installed, this command exports without changing the input:

```bash
soffice --headless --convert-to pdf --outdir review-output reviewed.docx
```

Use a fresh output directory, inspect diagnostics and confirm that a new PDF
exists. Review its pages using an available PDF/image viewer; this is a layout
check, not a separate PDF manipulation workflow. Do not promise that all Word
features render identically in LibreOffice.

API references: [Document](https://python-docx.readthedocs.io/en/latest/api/document.html)
and [paragraphs/runs](https://python-docx.readthedocs.io/en/latest/api/text.html).
