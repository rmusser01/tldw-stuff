# License scope

Copyright (c) 2026 Robert Benjamin Jake Musser.

## Repository default

Repository-authored documentation and original contributions are licensed under
[Apache License 2.0](LICENSE), unless a file or pack states different terms.
This includes collection indexes, import guides, contribution instructions,
templates, and the newly authored item READMEs. The default applies to original
contributions in prompts, skills, chatdictionaries, chatbooks, and other collections;
imported material keeps its own terms.

## Retained content licenses

The Apache default does not relicense the default Buddy archives, character
images, cards, or imported persona YAMLs. More specific notices take precedence.

| Content | Applicable terms |
| --- | --- |
| [Selected Anthropic and OpenAI skills](skills/README.md) | Apache-2.0 under each skill’s unchanged upstream LICENSE.txt; per-item source and contributor attribution retained |
| [Selected OpenClaw skills](skills/openclaw/README.md) | MIT; upstream root license and OpenClaw Foundation copyright copied into each skill’s LICENSE.txt |
| [Samira](character-packs/samira/README.md): original and adapted cards, portrait, expressions, and manifest | AGPL-3.0-or-later; [original asset notice](character-packs/samira/assets/characters/samira/ASSET_LICENSE.md) and [full text](LICENSES/AGPL-3.0-or-later.txt) |
| [Default Assistant](character-packs/default-assistant/README.md): Chatbook JSON | [AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt) |
| Default Assistant: server JSON | [GPL-3.0-only](character-packs/default-assistant/SERVER_LICENSE.txt) |
| [Persona archetypes](personas/README.md): native YAMLs | [GPL-3.0-only](personas/LICENSE), with [upstream attribution](personas/UPSTREAM_LICENSE.md) |
| [Default Buddy packs and scaffolds](buddy-packs/README.md): server exports and catalog metadata | [GPL-3.0-only](buddy-packs/LICENSE), subject to more specific artwork notices; [upstream scope](buddy-packs/UPSTREAM_LICENSE.md) |
| pixel-migu character artwork and Buddy artwork | Retained `LicenseRef-User-Supplied` notices: [character assets](character-packs/pixel-migu/assets/characters/pixel_migu/ASSET_LICENSE.md), [Buddy server provenance](buddy-packs/pixel-migu/PROVENANCE-server.md), and [Buddy Chatbook provenance](buddy-packs/pixel-migu/PROVENANCE-chatbook.md) |

The imported Buddy packs were distributed with GPL-3.0-only server terms, not a
blanket AGPL grant. Their existing notices are retained. Samira and the Chatbook
Default Assistant retain AGPL-3.0-or-later. Pixel-migu's supplied-art provenance is
not an independent Apache, GPL, or AGPL artwork license grant.

Upstream scope maps are historical copies describing their source repositories;
they do not change this repository's Apache default. Keep item READMEs and their
referenced license/provenance files with downloaded content. Existing upstream
copyright and attribution notices are preserved.
