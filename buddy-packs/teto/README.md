# Teto

A red-haired, marker-drawn Teto companion with a white face, twin tails, a gray
dress with red trim, and simple stick legs. Its drawing style pairs with
[Migu Marker Basic](../migu-marker-basic/README.md).

## Preview and download

<img src="preview.png" alt="Teto still preview" width="192" height="192"> <img src="preview.gif" alt="Teto animated expression preview" width="192" height="192">

[**Download Teto**](teto.tldw-persona-vpack) · 252,591 bytes · [SHA-256 checksums](SHA256SUMS)

The still is the exact idle frame. The GIF cycles through actual pack frames on
a dark background. Downloadable PNG artwork has transparency, including around
the stick legs, while the white face and hair clip remain opaque. These are
artwork previews, not application screenshots.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 |
| Pack creator | tldw-project |
| Reference artwork credit | anonymous (artist unidentified) |
| License | [Apache-2.0](LICENSE.txt) for project contributions; reference and character rights remain separate in [NOTICE.txt](NOTICE.txt) |
| Contents | 16 poses, 18 state mappings, one 512 × 512 transparent atlas with 128 × 128 frames |
| Animation | Idle/blink, thinking, speaking, greeting, and celebration sequences; still reaction poses |
| Orientation | Faces the user, with a common body scale and planted support baseline |
| Tested | Chatbook `b4e460f751`; server `27cd027555`; 2026-09-08 |

## Import and use

Download the native archive using GitHub's **Download raw file** button. In
Chatbook, save or select a local Persona, then use **Persona Visual → Import
Pack…**, review the states, and **Save Pack**. The server uses its native import
preview/commit flow. See [complete import steps](../IMPORT.md).

The finished pack needs no image-generation service, model download or Petdex
tool. It is optional collection content and does not replace an application default.

In a Chatbook build with Buddy-to-character conversion, use **Create character…**
in Persona Visual to make an independent editable character with these reactions.
It can emote in the Console without the floating Buddy enabled. **Settings →
Appearance → Character expressions** selects Dynamic or Static. Static still
changes expressions but freezes animation; Reduce motion takes precedence.
Older builds may support Buddy import without those newer character features.

## States and source artwork

Operational states: `idle`, `wake_armed`, `listening`, `thinking`, `speaking`,
`tool_running`, `approval_needed`, `error`, and `offline`. Tool activity uses the
thinking loop; approval uses the confused pose; offline uses the sleepy pose.
Additional mappings cover greeting, happy, success, neutral, thinking, sleepy,
confused, and love; some intentionally share artwork. See [manifest.json](manifest.json).

[source.png](source.png) contains all sixteen poses:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
| --- | --- | --- | --- | --- |
| 1 | Idle | Neutral alternate (unused) | Blink | Neutral (unused) |
| 2 | Thinking | Thinking alternate | Speaking | Speaking alternate |
| 3 | Listening | Sleepy | Worried/error | Confused |
| 4 | Wave | Happy | Celebrate | Love |

The built-in OpenAI image tool generated the sheet from the supplied references.
Authorized local processing removed its baked-in checkerboard, retained enclosed
white shapes, scaled every pose by one common factor, and aligned the feet to
x=64 and y=118 in each cell. [PROMPT.txt](PROMPT.txt) records the exact prompt;
[recipe.json](recipe.json) records the preparation and registration.

## Verification and rebuilding

[Exact archive digests and results](verification.json) record the tested bytes.
The native archive passed Chatbook import review, publication, reload,
export/re-read, animated/static frame selection, conversion into eighteen
expressions, and independent character publication. Neutral, thinking and
speaking expressions contain multiple frames. Creator and reference notices
survived export and character publication.

The same archive passed server preview, committed untrusted import into an
inactive draft, exact asset checksums and activatable-manifest validation.
Tests used private temporary profiles and real SQLite databases, with only the
server asset-root locator redirected to temporary storage. No live application
UI or server HTTP-worker testing is claimed.

All sixteen poses were visually reviewed for identity, limb count, framing and
alignment. Artifact checks verified transparency, clear margins, fixed support
anchors, exact still previews, GIF animation, archive integrity and file hashes.

With the [documented application environments](../../docs/buddy-collection-verification.md#reproduce-and-rebuild), run from this repository:

```sh
python scripts/build_buddy_collection.py buddy-packs/teto
python tests/check_buddy_collection.py --host chatbook --pack teto
python tests/check_buddy_collection.py --host server --pack teto
```

The builder consumes the reviewed atlas and does not call image generation or
modify installed content. ADR required: no; this pack uses the existing native
visual and character-expression contracts without application changes.

## Attribution and updates

Character-design references: [first supplied Teto drawing](https://i.4cdn.org/g/1788844177063862.png)
and [second supplied Teto drawing](https://i.4cdn.org/g/1788893235735517.png), credited
to **anonymous** because their artist is unidentified. No published license was
supplied or verified for these reference images. Originals are linked, not bundled
or relicensed. Existing Migu artwork was used as a style reference; its pixels are
not included in Teto. [PROVENANCE.json](PROVENANCE.json) records these sources.

Keep [LICENSE.txt](LICENSE.txt), [NOTICE.txt](NOTICE.txt), and provenance with
copies. The archive embeds creator, full license and reference notices. Chatbook
preserves them; server tests cover imported visuals, not notice retention through
a later server export, so retain the accompanying files.

For an update, import into a new Persona/draft and compare before switching.
Downloaded and customized copies remain independent and never update automatically.
