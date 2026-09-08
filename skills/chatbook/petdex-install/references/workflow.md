# Preparation and app handoff

The helper uses Chatbook's Petdex APIs, tested at commit `b4e460f75`. This feature
was implemented on a development branch; do not assume an installed release has
it. Use the intended Chatbook environment or the available app route. Importing
this skill does not install Chatbook, its dependencies, or app-control tools.
Run the helper as a separate Python process, not inside the running app. Its CLI
uses disposable configuration so Chatbook's import-time config bootstrap does not
initialize or migrate the user's profile. It never opens a Persona database.

## Inspect before preparing

Run from this skill directory, or resolve the script to its absolute installed path:

```sh
python scripts/prepare_pet.py --pet https://petdex.dev/pets/homelander --inspect
python scripts/prepare_pet.py --local /path/to/downloaded-pet --inspect
```

The JSON report includes original credits, atlas geometry and a `review` object.
To edit mappings, save the report to a fresh JSON file using authorized file tools.
Edit `review.states` and `review.mappings`; keep `review.source_sha256` unchanged.
All five required mapping keys must remain present. The idle value must name a
source state; null on another key explicitly selects the idle fallback.

Each state names its zero-based atlas row, used frame count (1–8), total duration
in milliseconds, and loop flag. For example, this is the **shape**, not a supplied
map for an unknown pet:

```json
{"name":"idle","row":0,"frames":6,"duration_ms":1100,"loop":true}
```

Obtain actual eleven-row meanings/counts/timings from explicit metadata or user
review. A successful image decode, the number of rows or a familiar-looking pet
does not determine those facts. Do not label guessed rows as reviewed.

```sh
python scripts/prepare_pet.py --local /path/to/downloaded-pet --review /path/to/review.json --output ./reviewed-buddy
```

Preparation requires a new directory inside an existing writable parent. It
produces `buddy.tldw-persona-vpack` and `review.json`, including the archive hash.
It copies the original image into the native archive and retains bounded notices.
The report always has `installed: false`: a prepared archive is not a saved Persona.

| Result | Meaning / next step |
| --- | --- |
| Exit 0, inspected | Review data printed; no files created. |
| Exit 0, prepared | Native archive and receipt created; import/save still required. |
| Exit 0, needs_mapping with --inspect | Missing declarations reported; no files created. |
| Exit 3, needs_mapping | Preparation refused; supply an explicit reviewed map. |
| Exit 2 | Dependency, validation, stale review, output collision or I/O error; no successful install. |

An edited review is bound to the source digest, including credits and image bytes.
If remote or local data changed, inspect again instead of replacing the digest
blindly. Keep an existing output intact and choose a fresh output path on retry.
Validation errors, private-target blocks or version contradictions are not reasons
to try an unvalidated download command.

## Finish in Chatbook

1. Select the intended saved active local Persona. Save/cancel existing draft edits
   as authorized; confirm any unresolved replacement of a customized Buddy.
2. In Persona Visual, use **Import Pack…** with the prepared native archive.
3. Inspect mappings and preview. **Save Pack** publishes the draft; **Cancel Draft**
   discards it. Keep the existing floating Buddy selection unless asked to change it.
4. Reopen the saved pack to verify the result. Report exactly the achieved stage.

A character is optional separate output: **Create character…** creates an independent
editable copy. Its Dynamic/Static display preferences remain governed by Chatbook's
existing settings and reduced-motion behavior. Server actors must use the established
explicit local-copy workflow; this skill does not promise server installation.
