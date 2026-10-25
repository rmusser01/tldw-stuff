# Living portraits for codec calls

44 optional sets cover the [character roster](README.md): application characters,
four original support contacts, the finished Buddy character/creature cast, and
Saffron, Rowan and Sunny from supplied design boards. The five geometric shapes
and unfinished scaffolds are excluded. All sets use the same six roles and exact
eye/mouth pairs. Most stills are 256×256px; pixel-migu remains 128×128px.
The 264 PNGs total 22.87 MiB, distributed as small per-character files.
Keep each pack's files and notices together. Manual imports need no image provider.

## Set up one character in Chatbook

1. Open **Roleplay → Characters** and import the pack's native JSON card (see
   [card import guide](IMPORT.md)). For an existing customized character, duplicate
   or back it up first; the new files do not automatically replace its prompts.
2. Edit the saved local character, upload `codec/rest.png` as its portrait and
   **Save**. Card JSON does not embed the portrait. For pixel-migu the existing
   embedded PNG card remains available, but it does not contain these poses.
3. Expand **Living portrait**, leave the saved-source input on `idle`, and choose
   **Prepare saved artwork**. Check that **Saved source** matches `codec/rest.png`.
   If an active reaction/expression overrides the portrait, use the character's
   reaction editor to replace its neutral/idle source with this `rest.png`, Apply
   that artwork, then prepare the matching saved source again. Do this on your
   duplicate if you want to keep the original expression behavior intact.
4. In the role selector choose each of the following, then **Import / replace…**
   and select the matching PNG from `codec/`:

   | Role | File | Eyes / mouth |
   | --- | --- | --- |
   | rest | `rest.png` | open / closed |
   | small | `small.png` | open / small gap |
   | open | `open.png` | open / speaking |
   | blink rest | `blink_rest.png` | closed / closed |
   | blink small | `blink_small.png` | closed / small gap |
   | blink open | `blink_open.png` | closed / speaking |

5. Select each named pose in the preview selector to compare eye/mouth pairs,
   then use **Cycle six poses** to inspect the result and choose
   **Apply performance**. Importing just one role is not enough. Manual imports
   use these finished frames directly; **Edit regions** and generation are not
   needed. `inventory.json` documents the assets and is not an app import file.
6. Assign an existing voice through **Voice & Speech**, or configure a default
   profile in **Settings → Speech & TTS**. Use **Play speech sample…**, review its
   destination confirmation, then start a character chat in Console and play TTS.
   With dynamic character expressions and animations enabled, the app supplies
   the radio frame, idle motion, blinks and audio-reactive mouth movement with
   pauses. Reduced motion/static settings intentionally limit animation.

Choose **Remove applied** to stop using a performance. Changing source artwork
can invalidate its attachment; prepare and import again for the new source.
Back up the profile to retain applied performances. Character cards, Actor Packs,
sync and server exports do not carry these profile-local settings. There is no
automatic installer or bundled voice assignment in this collection.

## Generation and verification limits

Artwork was created with built-in ChatGPT image generation, followed by authorized
local source-preserving composition. Ready-made imports work without a live image
provider. This does **not** qualify Chatbook's configured live image-edit adapter:
that separate PR #3244 provider gap remains open (TASK-36555 AC5). Server and
third-party clients have not been tested for these new cards or performance sets.
See [codec-verification.json](codec-verification.json) for actual checks and limits.

To check file hashes, dimensions, exact pairs and unchanged outside pixels using
Python with Pillow installed, run from the collection checkout:

```sh
python tests/check_codec_collection.py
```

Updates are opt-in. Preserve customized cards, reaction mappings and performances
before applying newer files. Existing source files and historical checksums stay
unchanged; each pack's `CODEC_SHA256SUMS` covers its additive codec directory.

[MGS1 reference findings](CODEC_REFERENCE.md) explain the three mouth looks and
separate eye overlays. No original game artwork is included in these packs.
