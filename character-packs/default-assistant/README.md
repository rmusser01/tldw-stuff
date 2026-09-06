# Default Assistant

The built-in general-purpose character, preserved as separate application defaults.

| File | Source and behavior | License |
| --- | --- | --- |
| [chatbook.character.json](chatbook.character.json) | Chatbook's enriched example card, including personality, system prompt, detailed greeting, and alternate greetings | [AGPL-3.0-or-later](../../LICENSES/AGPL-3.0-or-later.txt) |
| [server.character.json](server.character.json) | Server's minimal general-purpose card and greeting, with no added system prompt | [GPL-3.0-only](SERVER_LICENSE.txt) |

Content version: **1.0.0**, exported from fresh temporary databases on 2026-09-05.
Neither variant includes artwork or a voice profile. Choose the variant you want;
they have the same character name but different original content.

## Use and verification

Follow the [character import guide](../IMPORT.md). Both JSON variants passed
Chatbook's native file import into new records after renaming the pre-existing
default in an isolated database. The server variant also passed the actual
server import endpoint function and persisted-field checks. Live UI/model
behavior and the enriched Chatbook variant on the server were not tested.

Updates are separate downloads. Preserve any customized card before importing,
and do not assume an import changes your active/default character selection.

## Provenance

Author/creator metadata remains the upstream **System** value. Repository source
attribution: Robert Benjamin Jake Musser and tldw contributors.

- [Chatbook database seed](https://github.com/rmusser01/tldw_chatbook/blob/56376e1fc188938bf350c62d3a9f95e820b93c40/tldw_chatbook/DB/ChaChaNotes_DB.py), exported using `export_character_card_to_json` from a fresh row 1.
- [Server database seed](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/tldw_Server_API/app/core/DB_Management/ChaChaNotes_DB.py), exported using the native `export_character(format="v2", include_world_books=False)` operation.

Native exporters normalize database null text values to empty strings. No
prompts or greetings were rewritten. Server material retains its
[upstream scope](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/LICENSE)
and required notice: Copyright (c) 2026 Robert Benjamin Jake Musser.
