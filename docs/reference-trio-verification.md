# Dipsy, Kimi and Cappy verification

Date: 2026-09-08 · Collection revision: 1.0.1 · Pack creator: tldw-project

[The three packs](../buddy-packs/README.md#dipsy-kimi-and-cappy) adapt the characters
in the user-supplied illustration. Reference-image credit is **anonymous**, as
requested by the user. Its artist identity and license were not independently
verified. The original image is not bundled. Each NOTICE.txt distinguishes the
reference credit from the project's new contributions and is embedded in the
native archive's artwork notices.

Dipsy (Qipao), stored as `dipsy-qipao`, is separate from the existing blue whale.
Dipsy is now version 1.0.1; Kimi and Cappy remain at 1.0.0. The whale and
application defaults are unchanged.

ADR required: no. These content additions use existing native pack and character
contracts. The builder now includes an optional local NOTICE.txt in the existing
artwork-notice field and file checksums; it adds no runtime interface.

## Artwork and outputs

The built-in OpenAI image tool generated and edited one sixteen-pose sheet per
character. Faces, shoulders and stance turn toward the viewer, with ordinary
expressions making eye contact. Each pack records its exact prompts and the
generation history in its provenance.
The requested identities are retained: Dipsy's twin buns, round glasses and blue
qipao; Kimi's silver hair, black dress and K pendant; Cappy's capybara snout and
red/gold tang jacket. The user previously authorized local image processing.

Each sheet was keyed to transparency and resized proportionally with one scale
factor for the entire character. Complete frames were then translated to a common
support baseline at y=118 and midpoint x=64 in 128-pixel cells. Recipes record the
scale, output sizes and translations. This preserves gesture changes without
introducing per-pose zoom or position drift. All 48 final poses were visually
reviewed for consistent identity, correct limb counts and unclipped margins.

Dipsy 1.0.1 includes a targeted dress correction from the built-in image tool.
The selected blue-dress waist area was composited onto the existing registered
frames, with hands, arms, heart and gold details protected. Pixel comparison
confirmed that every pixel outside the waist band remains identical to 1.0.0.
The original frame scale, translations, support anchors and animation timings
were retained. The recipe records the changed bounds and comparison digest.

Each pack supplies a 512 × 512 RGBA atlas, sixteen poses, eighteen state mappings,
a native `.tldw-persona-vpack`, a still PNG, an animated GIF, recipe, manifest,
provenance, generation prompt, Apache license, reference notice and SHA-256 list.
GIFs use a dark matte; source and native PNGs retain full alpha. Previews show
actual distributed frames, not application screenshots.

The three native downloads total 702,849 bytes.
[Per-pack sizes, digests and host results](../buddy-packs/reference-trio-verification.json)
record the tested files.

## Executed checks

For revision 1.0.1, Dipsy passed the checks below again using the updated archive.
The byte-identical Kimi and Cappy packs retain their previous verification results.

Chatbook commit: `b4e460f75142b37ff3df277fd712bdb1812007f9`.

All three passed native import review, publication, active-graph reload, native
export/re-read, and animated/static frame selection. Each converted into eighteen
expressions and published as an independent editable character in a real temporary
SQLite database. Neutral, thinking and speaking expressions contain multiple
frames. The complete artwork carrier, including the anonymous reference credit,
remained equal through export and character publication.

Server commit: `27cd02755563d326d218787ac60e0bc8e0524cb8`.

All three passed native preview and committed untrusted import into inactive
drafts, with exact source-image checksums and activatable eighteen-state manifests.
Only the asset-root locator was redirected into temporary storage. Server export
retention of artwork notices was not tested; keep NOTICE.txt, LICENSE.txt and
PROVENANCE.json with server copies.

Artifact checks verified file digests, transparency, nonempty frame cells, clear
margins, fixed support anchors, exact still previews, animated GIFs and reference
notices. A disposable Circle rebuild was byte-identical without NOTICE.txt; adding
a notice to a second disposable copy included it in the native metadata and
checksums. Only Dipsy was rebuilt for revision 1.0.1; the other published packs were unchanged.

Tests used private temporary profiles/configuration and real SQLite databases.
No live UI or server HTTP-worker testing is claimed. No real user profile,
installed Buddy or character was modified. Older releases may not include the
newer Buddy-to-character conversion or Dynamic/Static expression preference.

## Reproduce

Use the documented application environments from
[the collection verification guide](buddy-collection-verification.md#reproduce-and-rebuild).
From the content repository:

```sh
python tests/check_buddy_collection.py --host chatbook --pack dipsy-qipao --pack kimi --pack cappy
python tests/check_buddy_collection.py --host server --pack dipsy-qipao --pack kimi --pack cappy
python scripts/build_buddy_collection.py buddy-packs/dipsy-qipao buddy-packs/kimi buddy-packs/cappy
```

Run import checks after rebuilding. The builder consumes reviewed source atlases;
it does not call image generation or modify an application installation.
