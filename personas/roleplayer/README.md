# Roleplayer

Immersive character interaction and collaborative storytelling. This is a native tldw_server persona archetype: a first-run
assistant setup seed containing a prompt and configuration defaults.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 (unchanged upstream YAML) |
| Type | Persona archetype YAML |
| Author | Robert Benjamin Jake Musser / tldw_server contributors |
| Source | [Pinned upstream YAML](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/tldw_Server_API/Config_Files/persona_archetypes/roleplayer.yaml) |
| License | YAML: [GPL-3.0-only](../LICENSE); README: [AGPL-3.0-or-later](../../LICENSE) |
| Target | tldw_server archetype loader and startup catalog |
| Tested with | tldw_server commit `36b846628d7755e91e0d5539740a9f5c9a837966` |
| Verified on | 2026-09-05 |

## Files

- [roleplayer.yaml](roleplayer.yaml): original YAML, including persona, module, policy,
  voice, scope, Buddy seed, and starter-command fields. It contains no visual assets.

## Requirements

Use an existing tldw_server Python environment compatible with the pinned commit.
Validation uses its native loader and dependencies (including PyYAML, Pydantic,
Loguru, and the server's MCP/schema packages); this repository installs nothing.
No model, network connection, credentials, or database is needed for the loader check.
Chatting afterward requires the application's configured model.

The archetype seeds enabled MCP modules: none. Suggested external servers:
none. These are configuration suggestions, not bundled services or automatic
connections. Its confirmation mode is `never`; review the YAML's module and
policy defaults when customizing it.

## Import or use

### Verified native loader use

1. Download this directory, keeping the YAML beside this README.
2. Activate an existing compatible tldw_server environment and change to that
   server checkout's root so its Python packages are importable.
3. Run the following, replacing the example directory with the downloaded item's
   absolute directory. The key retains upstream underscores.

```python
from pathlib import Path
from tldw_Server_API.app.core.Persona.archetype_loader import (
    get_archetype,
    list_archetypes,
    load_archetypes_from_directory,
)

item_dir = Path("/path/to/tldw-stuff/personas/roleplayer")
loaded = load_archetypes_from_directory(item_dir)
assert set(loaded) == {"roleplayer"}
assert get_archetype("roleplayer") == loaded["roleplayer"]
assert list_archetypes()[0].key == "roleplayer"
print(loaded["roleplayer"].persona.name)
```

This validates the YAML and replaces the archetype cache in that Python process.
It does not import a persistent persona into a database or update a running server.
The loader reads direct `*.yaml` children only, so point it at this item directory.

### Server catalog use (source-inspected; live setup untested)

The pinned server already ships this exact default. For a matching source checkout,
startup reads `tldw_Server_API/Config_Files/persona_archetypes/roleplayer.yaml`. To restore
that default, back up any customized file, copy this YAML to that location, and
restart the server. Its key is `roleplayer`. For a separate custom archetype, use a
unique filename **and** change `archetype.key` to avoid a duplicate key being skipped.

The server exposes cached catalog list, detail, and preview routes under
`/api/v1/persona/archetypes`. This is not a general YAML upload format. Character
card import, Persona Buddy visual-pack import, and tldw_chatbook UI import are
separate paths and were not verified for this payload.

## Example

Input: “Let us begin a mystery in a floating city.”

Intended prompt behavior: A collaborative scene with vivid description and dialogue following the chosen setting. This is an illustrative expectation, not a
recorded model response. A loader check prints `Storyteller`.

## Verification

On 2026-09-05, the unmodified YAML was copied into its own temporary directory and
loaded with the actual pinned `archetype_loader.py` and `ArchetypeTemplate` schema.
The loader returned exactly `roleplayer`; its persona name and prompt were nonempty;
cache lookup and list operations returned the same entry. No schema or loader
mocks were used. The process used existing server dependencies and no user
configuration/database writes or network calls.

Live server startup, authenticated HTTP requests, setup wizard completion, LLM
output, external MCP services, voice, and Buddy rendering were not tested. The
`buddy` mapping is seed metadata, not an importable visual pack.

## Updating

Keep local customizations separately before replacing a downloaded copy. Compare
with the pinned source above, then repeat the loader check when adopting a newer
upstream file. Maintain a unique `archetype.key` for a customized additional item.

## Attribution

Copyright (c) 2026 Robert Benjamin Jake Musser.

The YAML is reproduced byte-for-byte from the pinned upstream file; only this
README and its collection directory were added. Upstream's [license scope](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/LICENSE)
licenses `tldw_Server_API/**` under GPL-3.0-only. The corresponding
[license text](../LICENSE) applies to this YAML independently of
the repository's default license. No artwork or third-party service assets are included.
