# Hugging Face

An unofficial Buddy inspired by Hugging Face's yellow hugging mascot: a round
face, two expressive hands, warm smiles and gentle reactions, drawn to fit the
collection's 2D cartoons.

## Preview and download

<img src="preview.png" alt="Hugging Face Buddy still preview" width="192" height="192"> <img src="preview.gif" alt="Hugging Face Buddy animated expression preview" width="192" height="192">

[**Download Hugging Face**](huggingface.tldw-persona-vpack?raw=1) · 185,511 bytes · [SHA-256 checksums](SHA256SUMS)

The still is the exact idle frame. The GIF cycles through actual pack frames on
a dark background; the downloadable PNG artwork is transparent. These are
artwork previews, not application screenshots.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 |
| Pack creator | tldw-project |
| Mascot and brand credit | [Hugging Face](https://huggingface.co/brand) |
| License | [Apache-2.0](LICENSE.txt) for project contributions to the extent applicable; underlying mascot and brand rights remain separate in [NOTICE.txt](NOTICE.txt) |
| Contents | 16 poses, 18 state mappings, one 512 × 512 transparent atlas with 128 × 128 frames |
| Animation | Idle/blink, thinking, speaking, greeting and celebration sequences; still reaction poses |
| Orientation | Front-facing, with a fixed circular face position and exactly two hands |
| Tested | Chatbook `b4e460f751`; server `27cd027555`; 2026-09-08 |

## Import and use

Download the native archive. In Chatbook, save or select a local Persona, then
use **Persona Visual → Import Pack…**, review the states, and **Save Pack**.
The server uses its native import preview/commit flow. See
[complete import steps](../IMPORT.md).

The finished pack needs no image-generation service, model download, Hugging Face
account or API key. It is optional collection content.

In a Chatbook build with Buddy-to-character conversion, use **Create character…**
in Persona Visual to make an independent editable character with these reactions.
It can emote in the Console without the floating Buddy enabled. **Settings →
Appearance → Character expressions** selects Dynamic or Static. Static still
changes expressions but freezes animation; Reduce motion takes precedence.
Older builds may support Buddy import without those newer character features.

For example, the Buddy thinks during tool activity, waves in greeting and opens
its hands in celebration on success. [manifest.json](manifest.json) records all
operational, reaction and mood mappings; some intentionally share artwork.

## Source artwork

[source.png](source.png) contains sixteen poses, read left to right:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
| --- | --- | --- | --- | --- |
| 1 | Idle | Neutral alternate (unused) | Blink | Neutral (unused) |
| 2 | Thinking | Thinking with bubbles | Speaking | Speaking alternate |
| 3 | Listening | Sleepy | Worried/error | Confused |
| 4 | Wave | Happy | Celebrate | Love |

The built-in OpenAI image tool generated the sheet from a textual description.
Authorized local processing preserved alpha, removed disconnected specks,
separated complete poses and applied one common scale. Frames use a shared
lower baseline; horizontal placement follows the face's upper arc, so moving
hands do not pull the face sideways. Blink and speaking reuse unchanged body
regions; thinking adds bubbles over the same pose.
[PROMPT.txt](PROMPT.txt) and [recipe.json](recipe.json) record the preparation.

## Verification and rebuilding

[verification.json](verification.json) records the exact tested archive digest
and application commits. Chatbook checks passed native import, publication,
reload, export/re-read, Dynamic/Static frame selection, conversion into eighteen
expressions, independent character publication and attribution retention.
Neutral, thinking and speaking expressions contain multiple frames.

Server checks passed preview, committed untrusted import into an inactive draft,
exact asset checksums and activatable-manifest validation. Checks used temporary
profiles and real SQLite databases, with only the server asset-root locator
redirected to temporary storage. Live UI and HTTP-worker testing are not claimed.
Server export notice retention is not covered; retain the accompanying files.

Artifact checks cover transparency, margins, face alignment, previews and file
hashes. The alignment check rejects four initially displaced poses and passes
all sixteen corrected frames. The atlas was visually reviewed for consistent
identity, two-hand anatomy, readable expressions and clean framing.

With the [documented application environments](../../docs/buddy-collection-verification.md#reproduce-and-rebuild), run from this repository:

```sh
python scripts/build_buddy_collection.py buddy-packs/huggingface
python tests/check_buddy_collection.py --host chatbook --pack huggingface
python tests/check_buddy_collection.py --host server --pack huggingface
```

The builder consumes the reviewed atlas without generating images or changing
installed content. ADR required: no; this pack uses existing Buddy and character
expression contracts without application changes.

## Attribution and updates

**Hugging Face** is credited for the mascot and brand identity, documented on
its [official brand page](https://huggingface.co/brand). Its name, logo and
underlying rights remain separate from this unofficial pack. No official logo
file is bundled or copied into the atlas, and no affiliation or endorsement is
implied. [PROVENANCE.json](PROVENANCE.json) records the reference and generation.

Project contributions use Apache-2.0 to the extent applicable. Keep
[LICENSE.txt](LICENSE.txt), [NOTICE.txt](NOTICE.txt) and provenance with copies.
The native archive embeds the creator, full license and attribution notice.

To update, import into a new Persona or draft and compare before switching.
Downloaded and customized copies remain independent and never update automatically.
