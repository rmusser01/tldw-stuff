# Moss

A tiny mushroom creature with a terracotta cap, a moss patch and a flower that blooms for celebrations.

## Preview and download

<img src="preview.png" alt="Moss still preview" width="192" height="192"> <img src="preview.gif" alt="Moss animated expression preview" width="192" height="192">

[**Download Moss**](moss.tldw-persona-vpack) · 206,278 bytes · [SHA-256 checksums](SHA256SUMS)

The still is the exact idle frame. The GIF cycles through actual pack frames on a dark background; the downloadable PNG artwork has transparency. These are artwork previews, not application screenshots.

## Details

| Field | Value |
| --- | --- |
| Content version | 1.0.0 |
| Creator | tldw-project |
| License | [Apache-2.0](LICENSE.txt) |
| Format | Native Persona Buddy visual pack |
| Artwork | One 512 × 512 transparent atlas, sixteen 128 × 128 sprite slots |
| States | 18 mappings, including all nine built-in operational states |
| Animation | Idle/blink, thinking, speaking, greeting and celebration; other reactions are still poses |
| Verified on | 2026-09-29 |

## Import and use

Download the archive using GitHub's **Download raw file** button. In Chatbook, open **Console → Menu → Buddy**, expand **Import pack & size**, enter its local path, choose the conversation or workspace, and **Apply**. A Persona is optional. See the [complete import guide](../IMPORT.md) for independent Buddies, the older Persona editor and the server's preview/commit API workflow.

The server import creates an inactive draft; review it before activation. No generation service, model download or Petdex account is required to use the artwork.

On builds with Buddy-to-character conversion, **Create character…** makes an independent editable character with these reactions. Character expression **Dynamic/Static** settings control playback; reduced motion takes precedence. Custom reactions are retained as custom slots, not a promise of every canonical character emotion.

## States and artwork

The [manifest](manifest.json) maps `idle`, `wake_armed`, `listening`, `thinking`, `speaking`, `tool_running`, `approval_needed`, `error` and `offline`. Tool activity uses thinking, approval uses confused, and offline uses sleepy. Additional greeting, happy, success and mood mappings share artwork intentionally.

The [source atlas](source.png) uses this row order:

| Row | Column 1 | Column 2 | Column 3 | Column 4 |
| --- | --- | --- | --- | --- |
| 1 | Idle | Idle copy (unused) | Blink | Idle copy (unused) |
| 2 | Thinking | Thinking with another dot | Speaking | Speaking alternate |
| 3 | Listening | Sleepy | Worried/error | Confused |
| 4 | Greeting | Happy | Celebrate | Love |

Frames have a fixed support baseline at y=118 and center at x=64. [recipe.json](recipe.json) records extraction, registration and corrections. Idle/blink and speaking reuse unchanged body pixels; thinking adds a second dot over the same frame.

## Verification and rebuilding

[verification.json](verification.json) records the exact archive hash and passing checks. Tested against clean committed sources: Chatbook `c49be0691652557c4a32db54a1604e4ea90cac97` and server `6110d2ae436c805c3beeda8f84427b4890534ddf`.

Chatbook checks covered native import, publication, reload, export round-trip, animation/static selection, conversion into eighteen expressions, independent character publication and creator/license retention. Server checks covered native preview, committed inactive draft, asset checksums and activatable-manifest validation. Checks used isolated temporary profiles and real SQLite databases, with the server asset-root locator redirected to temporary storage. No live UI or HTTP-worker test is claimed.

Artwork checks covered all sixteen support anchors, transparent margins, the exact still preview, animated GIF, provenance and checksums. With the [documented application environments](../../docs/buddy-collection-verification.md#reproduce-and-rebuild), run:

```sh
python scripts/build_buddy_collection.py buddy-packs/moss
python tests/check_buddy_collection.py --host chatbook --pack moss
python tests/check_buddy_collection.py --host server --pack moss
```

The existing builder consumes the reviewed atlas without image generation. ADR required: no; this is optional content using existing contracts, with no application changes.

## Attribution and updates

Original artwork and pack creator: **tldw-project**. Created with OpenAI's built-in image tool, followed by user-authorized local image processing. [PROMPT.txt](PROMPT.txt) contains the generation prompt; [PROVENANCE.json](PROVENANCE.json) records the original image digest and preparation method. The collection's [Llama](../llama/) was viewed for style; none of its image pixels are included here.

Keep the license and provenance with copies. The archive embeds the creator and full license notice. For updates, import a new copy and compare before switching; downloaded and customized copies remain independent.
