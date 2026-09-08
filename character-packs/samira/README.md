# Samira “Sammy” Vadem

The bundled Samira character from Chatbook, with its original portrait and
31 reaction/expression images.

![Samira portrait](assets/characters/samira/Sammy.png)

## Files

- [Original Chatbook card](assets/characters/samira/Samira.character.json): Character Card V2 JSON with collection creator metadata.
- [Server-compatible card](server.character.json): omits the original optional `character_book: null` field; all authored text and other fields are identical.
- [Sammy.png](assets/characters/samira/Sammy.png): original portrait, not an embedded card.
- [Expression images](assets/characters/samira/expressions/): all 31 source WebP files.
- [Visual identity manifest](assets/characters/samira/visual_identity_pack.json): unchanged mappings, image metadata, and checksums.
- [Original asset notice](assets/characters/samira/ASSET_LICENSE.md): AGPL-3.0-or-later license and asset provenance.

## Use and verification

Content version: **1.0.1** (2026-09-05 snapshot). Requires a compatible application;
no model or generation service is required to import the files. Model setup is
separate for chatting. Follow the [character import guide](../IMPORT.md), including
its separate portrait and expression steps.

The original card passed Chatbook's native import into a temporary SQLite DB.
The server-compatible variant passed the server's actual import endpoint function
and persisted-text checks. All 31 images passed native Chatbook manifest/hash,
format, dimension, and image-budget validation. Live UI interaction, model
responses, and expression activation were not exercised.

Keep customized copies when updating; importing a card alone does not attach the
expression set. The server variant is provided because the pinned server rejects
the original null `character_book` value.

## Provenance and license

Source: [Chatbook's bundled Samira](https://github.com/rmusser01/tldw_chatbook/tree/56376e1fc188938bf350c62d3a9f95e820b93c40/tldw_chatbook/assets/characters/samira).
Artwork and expression mappings retain their source bytes. Both JSON cards use
`tldw-project` as creator; the server-compatible card also omits the null book field.

The card, portrait, and expressions carry the explicit
[AGPL-3.0-or-later notice](assets/characters/samira/ASSET_LICENSE.md), with the
[full license](../../LICENSES/AGPL-3.0-or-later.txt) preserved in this repository. The original notice records
which reactions were independently generated and identifies the source portrait.
Server verification used commit `36b846628d7755e91e0d5539740a9f5c9a837966`.

## Collection creator

Creator: **tldw-project**. The 2026-09-07 update changes creator metadata only;
prompts, reactions, artwork pixels and source-license notices retain their prior
content. [Metadata changes and checksums](../creator-metadata.json) record the
previous source hashes and updated distributed hashes. Earlier import results
describe the original snapshot; this update was checked for metadata-only changes.
