# Import a character

## Chatbook

Open **Roleplay → Characters**, use the character import action, and choose a
pack's `.character.json` file. For pixel-migu, its `.character.png` also embeds
the card and imports its portrait. A JSON card does not embed these packs'
separate portrait or expression images.

For Samira, import `assets/characters/samira/Samira.character.json`, then use
the character editor's avatar upload action to choose `Sammy.png` beside it.
Sammy.png is a portrait, not an embedded character card.

The Default Assistant is already present in a fresh database. The native
importer may reuse an existing matching card. If keeping a separate customized
copy, use the application's duplicate workflow or rename the copy deliberately.
These downloads do not replace the application's default-selection setting.

## Server

Use the character JSON import operation in your server's character interface or
API documentation. Use `default-assistant/server.character.json` for the
server's minimal default, `samira/server.character.json` for Samira, and the
original pixel-migu JSON for pixel-migu. The native server endpoint's JSON-file
import was verified for these three files.

The original Samira JSON contains `character_book: null`, which the pinned
server rejects. Its separate server variant omits only that optional empty
field; authored text and other metadata are unchanged.

## Expression assets

Each illustrated pack preserves its original `assets/characters/...` directory.
The manifest's `storage_relpath` values resolve relative to that pack's `assets/`
directory. Keep this structure intact when inspecting or reusing the manifest.

The card and expression manifest are separate payloads. Importing a JSON/PNG
card does not automatically install or activate the expression collection.
The images are supplied for reuse through the target application's expression
editor and as complete source references for the existing built-in pack.
Use the manifest's `expression_key` mappings rather than assuming filenames
map identically in every application. No standalone expression-bundle upload
or automatic card-to-pack binding is claimed by this collection.

## Verification scope

Tested on 2026-09-05 against Chatbook `56376e1fc188938bf350c62d3a9f95e820b93c40` and server `36b846628d7755e91e0d5539740a9f5c9a837966`.

- Native Chatbook file imports persisted the original Samira JSON, both Default
  Assistant variants, the server-compatible Samira variant, and pixel-migu JSON/PNG into temporary SQLite databases.
  Existing default rows were renamed first to verify creation, not just reuse.
- Server `import_character_endpoint` was called directly with real uploaded-file
  objects and temporary databases for the server default, adapted Samira,
  and pixel-migu JSON. Persisted authored text was compared with the source.
- All 57 copied source files match the pinned Chatbook repository byte-for-byte.
  All 49 expression images passed Chatbook's actual manifest, checksum, image
  format, dimension, and decoded-image budget validation.

These are native service and persistence checks, not live UI, HTTP authentication,
LLM behavior, avatar-upload, or expression-activation tests. See
[verification.json](verification.json) for the exact files and results.
