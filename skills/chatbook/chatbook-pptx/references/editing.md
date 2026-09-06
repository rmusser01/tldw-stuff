# Editing and verification

## Text and notes

Open an existing deck with `pptx.Presentation(path)`. Inspect each slide's shapes;
not every shape has a text frame, and a blank slide can have no title placeholder.
For grouped shapes, inspect their children. Tables have cell text frames too.

Assigning a shape's `.text` rebuilds its paragraphs/runs. To retain mixed
formatting for a specific change, identify the intended runs and update their
text. Matches spanning runs require examining the original formatting. A global
substring replacement can change unrelated headings, URLs or speaker notes.

```python
from pptx import Presentation

presentation = Presentation("source.pptx")
slide = presentation.slides[1]
assert slide.shapes.title.text == "Pilot before expansion"
run = slide.shapes.title.text_frame.paragraphs[0].runs[0]
run.text = "Approve the pilot"
slide.notes_slide.notes_text_frame.text = "Ask for a decision on the pilot scope."
presentation.save("reviewed.pptx")
```

This example expects the included starter deck. For arbitrary inputs, identify
the target by content and structure rather than assuming index 1 is correct.

## Charts and templates

Use `chart.replace_data(CategoryChartData(...))` for category-chart updates,
providing aligned categories and series. Inspect the original chart type first;
XY/scatter data requires its corresponding data API. Reopen and compare embedded
numbers with source data after an update. Preserve units and labels with the data.

Choose layouts by inspecting their names and placeholders in the supplied
presentation. Do not assume a template's layout 1 is title-and-content. Rebuilding
all slides can discard animations, transitions, embedded objects and other
features outside python-pptx's supported editing surface. The starter does not
provide slide cloning, master editing or animation authoring; use a capable
editor when those are required.

## Rendering

If LibreOffice is present, export into a fresh directory:

```bash
soffice --headless --convert-to pdf --outdir review-output reviewed.pptx
```

Check diagnostics and that the output is newly created. If Poppler is available,
`pdftoppm -png review-output/reviewed.pdf review-output/slide` produces page images.
Inspect all slides using an available image viewer, then revise and render again
when you change the layout. Conversion and visual inspection are separate checks.

API references: [text](https://python-pptx.readthedocs.io/en/latest/user/text.html)
and [charts](https://python-pptx.readthedocs.io/en/latest/user/charts.html).
