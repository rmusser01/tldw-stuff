# Tool Helper Intermediate — scaffold

Catalog scaffold fixture, not final character art or animation: Utility-themed starter with a declared exact tool animation variant.

**Scaffold reference only.** The shipped images are 4 × 4 solid-color fixtures, not finished Buddy art. Import is verified for format exploration; author and review the assets in the production recipe before using it as a finished companion.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 (2026-09-05 catalog snapshot) |
| Type | Buddy scaffold reference |
| Creator | tldw-project |
| Source | [Server starter catalog](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/tldw_Server_API/app/core/Persona/visual_starter_fixtures.py) |
| License | [GPL-3.0-only](../../LICENSE); see [upstream scope map](../../UPSTREAM_LICENSE.md) |
| Production status | `scaffold`; tier `intermediate` |
| Target | tldw_server and Chatbook Persona Visual |
| Tested with | Server `36b846628d7755e91e0d5539740a9f5c9a837966`; Chatbook `56376e1fc188938bf350c62d3a9f95e820b93c40` |
| Verified on | 2026-09-05 |

## Files and import

- [tool-helper-intermediate.tldw-persona-vpack](tool-helper-intermediate.tldw-persona-vpack): native portable archive, 5,253 bytes, containing 6 PNG assets and 6 state mappings.
- [starter-catalog.json](starter-catalog.json): source catalog detail, including the native fixture manifest, production recipe, asset declarations and readiness metadata. Reference only; import the archive.
- [SHA256SUMS](SHA256SUMS): checksum of the complete archive.

Follow the [exact Chatbook and server import steps](../../IMPORT.md).
The required application and a saved Persona are sufficient; no external
models, generation tools or additional asset downloads are required.

## Example and states

Selecting `idle` previews the solid-color fixture. `lofi-study-intricate` demonstrates atlas regions; the other scaffolds demonstrate state rows. This is a format sample, not the identity described in the production recipe.

States: `error`, `idle`, `listening`, `speaking`, `thinking`, `tool.notes_search`.

## Verification

Native server export, preview and committed import succeeded, producing a
new draft with 6 matching asset checksums and 6 states.
Native Chatbook import, publication to a temporary profile/SQLite database,
and active-graph reload also succeeded with 6 assets.
Archive export warnings: none. [Method and limits](../../IMPORT.md#verification-scope).
Other application versions and live UI rendering are untested.

## Updating

Import updates into a new Persona or draft, compare your customized pack, and
switch only after review. Keep your customized copy; these files do not update
installed content automatically. Version 1.0.0 preserves the pinned catalog.

## Attribution

Copyright (c) 2026 Robert Benjamin Jake Musser. Source is the server-owned
`DEFAULT_PERSONA_VISUAL_STARTER_PACKS` catalog at the pinned commit above.
The source label `bundled` is retained in the catalog detail; the upstream
scope map supplies the GPL-3.0-only terms for repository-authored material.
The native exporter remapped fixture asset keys to portable asset IDs and
created synthetic export metadata. Artwork bytes, timings, state mappings,
production status and recipes are unchanged. No original art was generated here.
