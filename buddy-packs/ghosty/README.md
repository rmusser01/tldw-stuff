# Ghosty

A friendly white sheet ghost with expressive little sheet arms.

## Preview and download

<img src="preview.png" alt="Ghosty still preview" width="192" height="192"> <img src="preview.gif" alt="Ghosty animation and reaction preview" width="192" height="192">

[**Download Ghosty**](ghosty.tldw-persona-vpack) · 210,700 bytes · [SHA-256 checksums](SHA256SUMS)

The still is the exact idle frame. The animated preview cycles through actual
pack frames on a dark background; the downloadable artwork has transparency.
These are artwork previews, not application screenshots.

## Details

| Field | Value |
| --- | --- |
| Version | 1.0.0 |
| Creator | tldw-project |
| License | [Apache-2.0](LICENSE.txt), including this new artwork |
| Artwork | Original AI-assisted 2D cartoon, referenced to the existing Buddy collection |
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
| 1 | Idle | Bob | Blink | Idle alternate |
| 2 | Thinking | Thinking alternate | Speaking | Speaking alternate |
| 3 | Listening | Sleepy | Error | Confused |
| 4 | Wave | Happy | Celebrate | Love |

## Verification and updates

This archive passed native Chatbook import, save, reload, export/re-import,
motion/static selection, and independent animated-character publication checks.
The same bytes passed server preview, committed inactive-draft import, checksum
comparison and activatable-manifest validation. Tests used disposable profiles
and SQLite databases; they did not drive either application's live UI or HTTP
worker. [Full verification and rebuilding instructions](../../docs/buddy-collection-verification.md).

Keep this [license](LICENSE.txt) and [provenance](PROVENANCE.json) when sharing
copies. The archive embeds the creator and full license notice; Chatbook preserves
that carrier. Server tests cover the imported visuals, not notice retention through
a later server export, so retain the accompanying files.

To update a customized Buddy, import into a new Persona/draft and compare before
switching. Downloaded copies are independent and never update automatically.
[PROMPT.txt](PROMPT.txt) records the built-in image-generation prompt;
[recipe.json](recipe.json) describes the prepared atlas.
