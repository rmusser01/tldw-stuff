# Preparation and app handoff

The helper uses Chatbook's Petdex APIs. Check the bundle README for the exact
tested build; do not assume an older installed release has this feature.
Use the intended Chatbook environment or the available app route. Importing
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
The report always has `installed: false`: a prepared archive is not an installed Buddy.

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

1. Open **Console → Menu → Buddy** in the intended profile. Record current settings
   when the user has asked to preserve them. No saved Persona is needed.
2. For the prepared archive, expand **Import pack & size** and enter its absolute
   path. Alternatively, **Import from Petdex** opens the app's source review; its
   **Use draft** action stages the pet for this management form.
3. **Apply** installs the independent Buddy and selects it with the displayed
   settings. Cancel before Apply leaves the library and settings unchanged. If Apply
   reports a settings-save failure, the Buddy may already be installed but unselected:
   retry Apply in the same form, or reopen and verify the library and selection
   before importing again. If asked to keep
   the prior floating Buddy, reopen management, reselect it and Apply, preserving
   its original show/motion/follow/Persona settings.
4. Reopen management, find the newly installed Buddy and preview representative
   states. Verify the final selection and target. Report exactly the achieved stage.

A character is optional separate output: select an installed Buddy, choose **Create
character**, edit the name/personality/greeting and expression mappings, then
**Prepare preview**. Review conversion warnings before **Create character**.
The created copy is independent of later Buddy edits; closing management does not
undo explicit character creation. Creating it does not apply staged management
preferences. Preserve animation in the file when desired; Dynamic/Static display
preferences and reduced motion control actual playback.

## Persona authoring route

For an explicitly requested saved local Persona, **Persona Visual → Petdex… →
Use draft → Save Pack** remains available. A prepared native archive instead uses
**Import Pack… → Save Pack**. Review any replacement of customized artwork within
the user's existing authorization. **Cancel Draft** discards the draft; reopening
the saved pack verifies publication. This changes that Persona's pack, so it is a
different destination from an independent Buddy library import.

Server actors must use the established
explicit local-copy workflow; this skill does not promise server installation.
