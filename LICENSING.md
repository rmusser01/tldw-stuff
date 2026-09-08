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
| [Selected Anthropic and OpenAI skills](skills/README.md) | Apache-2.0 under each skill’s unchanged upstream LICENSE.txt; per-item source and contributor attribution retained. Artifact builder’s bundled shadcn/ui components retain [MIT](skills/anthropic/web-artifacts-builder/SHADCN_LICENSE.txt) with [third-party notices](skills/anthropic/web-artifacts-builder/THIRD_PARTY_NOTICES.md) |
| [Selected OpenClaw skills](skills/openclaw/README.md) | MIT; upstream root license and OpenClaw Foundation copyright copied into each skill’s LICENSE.txt |
| [Samira](character-packs/samira/README.md): original and adapted cards, portrait, expressions, and manifest | AGPL-3.0-or-later; [original asset notice](character-packs/samira/assets/characters/samira/ASSET_LICENSE.md) and [full text](LICENSES/AGPL-3.0-or-later.txt) |
| [Default Assistant](character-packs/default-assistant/README.md): Chatbook JSON | [AGPL-3.0-or-later](LICENSES/AGPL-3.0-or-later.txt) |
| Default Assistant: server JSON | [GPL-3.0-only](character-packs/default-assistant/SERVER_LICENSE.txt) |
| [Persona archetypes](personas/README.md): native YAMLs | [GPL-3.0-only](personas/LICENSE), with [upstream attribution](personas/UPSTREAM_LICENSE.md) |
| [Dipsy (Qipao), Kimi and Cappy](buddy-packs/README.md#dipsy-kimi-and-cappy) | Apache-2.0 for project-created sprites and pack materials; reference creator anonymous, reference license not published/verified; see each pack’s NOTICE.txt |
| [Teto](buddy-packs/teto/README.md) | Apache-2.0 for project contributions; supplied reference artwork credited to anonymous, with no published reference license verified; reference and character rights remain separate in [NOTICE.txt](buddy-packs/teto/NOTICE.txt) |
| [Align Waifu](buddy-packs/align-waifu/README.md) | Apache-2.0 for project contributions to the extent applicable; supplied reference artwork credited to anonymous, with no published reference license verified; reference and character rights remain separate in [NOTICE.txt](buddy-packs/align-waifu/NOTICE.txt) |
| [Twelve original companion packs](buddy-packs/README.md#new-companion-collection) | Apache-2.0 for original AI-assisted artwork, manifests and metadata; creator tldw-project; full license and provenance supplied in each pack |
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

## Hermes and note-workflow additions

The [Hermes collection](skills/hermes/README.md) retains Nous Research’s MIT
license and any per-skill notices, including Siqi Chen’s humanizer copyright.
The [Chatbook note adaptations](skills/chatbook/README.md) retain Notion Labs’
MIT notice and identify their changes and original source revisions. Their skill
content is MIT; collection READMEs and indexes use the Apache-2.0 default.
Anthropic theme-factory remains Apache-2.0, and OpenClaw gog remains MIT.

## Original Chatbook Office workflows

The three [Chatbook Office skills](skills/chatbook/README.md#original-office-skills)
are original Apache-2.0 contributions, with a license copy and provenance in each
bundle. They reference public library APIs and credit the consulted Nous Research
Hermes packs; no Hermes helpers or Anthropic proprietary Office content is copied
into them. The separately imported Hermes helpers keep their MIT notices.

## Community collection additions

[Trail of Bits property-based-testing](skills/trailofbits/property-based-testing/COLLECTION.md)
retains **CC BY-SA 4.0**, with the complete license, original README, mark and source
attribution. The Apache default does not replace its attribution/share-alike terms.

The selected [Corey Haines](skills/corey-haines/README.md),
[Matt Pocock](skills/matt-pocock/README.md), and [K-Dense](skills/k-dense/README.md)
skills retain **MIT** and their original copyright notices. Two marketing
reference files have only relative-link relocations; the included integration
guides are unchanged and retain Corey Haines’s MIT terms. Collection READMEs and
indexes remain original Apache-2.0 documentation. Source/output hashes identify
these changes separately.
