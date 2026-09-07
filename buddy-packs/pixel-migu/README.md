# pixel-migu

Turquoise pixel-art robot companion with twin tails, state loops and expression poses.

## Preview

<img src="preview.png" alt="pixel-migu Buddy preview" width="192" height="192">

Exact preview PNG from the downloadable pack, displayed enlarged. This shows
the supplied artwork; it is not an application screenshot. The preview retains
the pack's artwork terms and provenance described below.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 (2026-09-05 catalog snapshot) |
| Type | Persona Buddy pack |
| Author | Robert Benjamin Jake Musser / tldw contributors (art supplier; artist unspecified) |
| Source | [Server starter catalog](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/tldw_Server_API/app/core/Persona/visual_starter_fixtures.py) |
| License | Artwork: `LicenseRef-User-Supplied` ([server notice](PROVENANCE-server.md), [Chatbook notice](PROVENANCE-chatbook.md)); server catalog/recipe metadata: [GPL-3.0-only](../LICENSE) |
| Production status | `art_ready`; tier `basic` |
| Target | tldw_server and Chatbook Persona Visual |
| Tested with | Server `36b846628d7755e91e0d5539740a9f5c9a837966`; Chatbook `56376e1fc188938bf350c62d3a9f95e820b93c40` |
| Verified on | 2026-09-05 |

## Files and import

- [pixel-migu.tldw-persona-vpack](pixel-migu.tldw-persona-vpack): native portable archive, 77,634 bytes, containing 64 PNG assets and 31 state mappings.
- [starter-catalog.json](starter-catalog.json): source catalog detail, including the native fixture manifest, production recipe, asset declarations and readiness metadata. Reference only; import the archive.
- [SHA256SUMS](SHA256SUMS): checksum of the complete archive.

Follow the [exact Chatbook and server import steps](../IMPORT.md).
The required application and a saved Persona are sufficient; no external
models, generation tools or additional asset downloads are required.

## Example and states

Select `idle` for the four-frame pixel loop, `reaction.greeting` for a wave, or `reaction.success` for thumbs-up. Includes twelve four-frame sequences and sixteen static poses.

States: `approval_needed`, `error`, `idle`, `listening`, `mood.angry`, `mood.celebrate`, `mood.confused`, `mood.excited`, `mood.happy`, `mood.listening`, `mood.love`, `mood.neutral`, `mood.sad`, `mood.skeptical`, `mood.sleepy`, `mood.surprised`, `mood.thinking`, `mood.thumbs_up`, `mood.type`, `mood.wave`, `offline`, `pack_private.alert_idle`, `pack_private.confused`, `pack_private.original_think`, `reaction.greeting`, `reaction.happy`, `reaction.success`, `speaking`, `thinking`, `tool_running`, `wake_armed`.

## Verification

Native server export, preview and committed import succeeded, producing a
new draft with 64 matching asset checksums and 31 states.
Native Chatbook import, publication to a temporary profile/SQLite database,
and active-graph reload also succeeded with 64 assets.
Archive export warnings: none. [Method and limits](../IMPORT.md#verification-scope).
Other application versions and live UI rendering are untested.

## Updating

Import updates into a new Persona or draft, compare your customized pack, and
switch only after review. Keep your customized copy; these files do not update
installed content automatically. Version 1.0.0 preserves the pinned catalog.

## Attribution

Artwork is maintainer-supplied; the original artist is unspecified. Preserve
both original provenance notices. `LicenseRef-User-Supplied` records that
provenance and is not a public-domain, Creative Commons or blanket GPL grant
for the artwork. This collection copy follows the maintainer's request to
publish the shipped defaults. No broader artwork license is asserted.

The [Chatbook bundled Buddy](https://github.com/rmusser01/tldw_chatbook/blob/56376e1fc188938bf350c62d3a9f95e820b93c40/tldw_chatbook/assets/persona_visual/pixel_migu/manifest.json)
and server fixture have identical parsed manifest values and all 64 PNG bytes
match exactly. One archive therefore covers both applications; no second
asset copy or format conversion is needed. The native exporter remaps asset
IDs and generates synthetic export metadata. See the separate character card
collection for the character identity; a Buddy import does not import a card.
