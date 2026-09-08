# Dipsy (Qipao)

Dipsy with round glasses, twin buns and a blue floral qipao.

This is Dipsy from the reference illustration. The separate
[blue-whale Dipsy](../dipsy/README.md) remains available.

## Preview and download

<img src="preview.png" alt="Dipsy (Qipao) still preview" width="192" height="192"> <img src="preview.gif" alt="Dipsy (Qipao) animation and reaction preview" width="192" height="192">

[**Download Dipsy (Qipao)**](dipsy-qipao.tldw-persona-vpack) · 204,423 bytes · [SHA-256 checksums](SHA256SUMS)

The still is the exact idle frame. The animated preview cycles through actual
pack frames on a dark background; the downloadable artwork has transparency.
These are artwork previews, not application screenshots.

## Reference

Character design reference: [the supplied 4chan meme](https://i.4cdn.org/g/1788855416369834.png),
credited to **anonymous** at the user's request. No published reference-image
license was supplied or verified. The original image is not bundled or relicensed;
[NOTICE.txt](NOTICE.txt) separates that credit from tldw-project's new contributions.

## Details

| Field | Value |
| --- | --- |
| Version | 1.0.1 |
| Creator | tldw-project |
| License | [Apache-2.0](LICENSE.txt) for project contributions; reference rights remain separate in [NOTICE.txt](NOTICE.txt) |
| Artwork | Viewer-facing 2D sprites adapted from the supplied reference |
| Reference creator | anonymous, as requested by the user; see [NOTICE.txt](NOTICE.txt) |
| Contents | 16 poses, 18 state mappings, one 512 × 512 transparent atlas with 128 × 128 frames |
| Animation | Idle, thinking, speaking, greeting, and celebration sequences; still reaction poses |
| Tested | Chatbook `b4e460f751`; server `27cd027555`; 2026-09-08 |

## Import and use

Download the `.tldw-persona-vpack` using GitHub's **Download raw file** button.
In Chatbook, save or select a local Persona, then use **Persona Visual → Import
Pack…**, review the states, and **Save Pack**. The server uses the native import
preview/commit flow. See [complete import steps](../IMPORT.md).

No model, image-generation service, Petdex tool, or external asset download is
needed to use the finished pack. These companions are optional collection content.

In a Chatbook build with Buddy-to-character conversion, use **Create character…**
in Persona Visual to create an independent editable character with these reactions.
The Console character can emote without the floating Buddy being enabled.
**Settings → Appearance → Character expressions** selects Dynamic or Static;
Static still changes expression but freezes its animation. Reduce motion takes
precedence. Older builds may support Buddy import without these newer features.

## States and source artwork

Operational states: `idle`, `wake_armed`, `listening`, `thinking`, `speaking`,
`tool_running`, `approval_needed`, `error`, and `offline`. Tool activity uses the
thinking loop; approval uses the confused pose; offline uses the sleepy pose.

Additional reactions: greeting, happy, success, neutral, thinking, sleepy,
confused, and love. Some reactions intentionally share the same artwork.
[manifest.json](manifest.json) records every mapping, frame rectangle and duration.

[source.png](source.png) contains all sixteen prepared poses, ordered by rows:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
| --- | --- | --- | --- | --- |
| 1 | Idle | Alternate pose (unused) | Blink | Idle alternate |
| 2 | Thinking | Thinking alternate | Speaking | Speaking alternate |
| 3 | Listening | Sleepy | Error | Confused |
| 4 | Wave | Happy | Celebrate | Love |

## Verification and updates

Version 1.0.1 lowers the dress crease toward the natural waist across all sixteen
poses. Only the blue-dress waist area was updated; original pixels outside it,
including the face, expressions and foot positioning, are preserved exactly.

This archive passed native Chatbook import, save, reload, export/re-import,
motion/static selection, and independent animated-character publication checks.
The same bytes passed server preview, committed inactive-draft import, checksum
comparison and activatable-manifest validation. Tests used disposable profiles
and SQLite databases; they did not drive either application's live UI or HTTP
worker. [Full verification and rebuilding instructions](../../docs/reference-trio-verification.md).

Keep this [license](LICENSE.txt), [reference credit](NOTICE.txt), and [provenance](PROVENANCE.json) when sharing
copies. The archive embeds the creator, reference credit, and full license notice; Chatbook preserves
that carrier. Server tests cover the imported visuals, not notice retention through
a later server export, so retain the accompanying files.

To update a customized Buddy, import into a new Persona/draft and compare before
switching. Downloaded copies are independent and never update automatically.
[PROMPT.txt](PROMPT.txt) records the built-in generation, viewer-facing and dress-correction prompts;
[recipe.json](recipe.json) describes the prepared atlas.
