# pixel-migu

The turquoise pixel character, with 18 expression images and both native card formats.

![pixel-migu](assets/characters/pixel_migu/pixel-migu.character.png)

## Files

- [PNG character card](assets/characters/pixel_migu/pixel-migu.character.png): includes the embedded card and portrait; verified with Chatbook.
- [JSON character card](assets/characters/pixel_migu/pixel-migu.character.json): verified with both Chatbook and the server.
- [Expression images](assets/characters/pixel_migu/expressions/): all 18 source PNGs.
- [Visual identity manifest](assets/characters/pixel_migu/visual_identity_pack.json): original expression mappings, image metadata, and checksums.
- [Original asset notice](assets/characters/pixel_migu/ASSET_LICENSE.md): source-sheet provenance and supplied-artwork terms.

## Use and verification

Content version: **1.0.0** (2026-09-05 snapshot). Follow the
[character import guide](../IMPORT.md). Chatbook's native file importer created
characters from both JSON and PNG; the PNG retained the portrait. The server's
actual JSON import endpoint function created a character and preserved its text.
All 18 images passed native Chatbook manifest/hash, format, dimension, and budget
checks. No model or generation service is required for these imports.

The expressions include eight canonical emotions plus ten custom/operational
poses. Their exact keys are in the manifest. Card import alone does not attach
the expression set; live expression activation and LLM emote behavior were not
tested. Updates are opt-in: keep customized copies before importing new content.

The separate [pixel-migu Buddy pack](../../buddy-packs/pixel-migu/README.md) has
animated runtime states and its own verified import path.

## Provenance and license

Copied unchanged from [Chatbook's bundled pixel-migu](https://github.com/rmusser01/tldw_chatbook/tree/56376e1fc188938bf350c62d3a9f95e820b93c40/tldw_chatbook/assets/characters/pixel_migu).
Tested with that commit and server `36b846628d7755e91e0d5539740a9f5c9a837966`.

The maintainer supplied the original artwork and requested this collection copy.
The artist is unspecified. The original `LicenseRef-User-Supplied` notice is
preserved; no broader artwork license or copyright assignment is asserted, and
the repository's default Apache-2.0 terms do not override that specific notice.
