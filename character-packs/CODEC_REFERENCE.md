# MGS1 codec portrait reference

Reference: [MGS1 — All Optional Codec Calls](https://www.youtube.com/watch?v=otEcx0U6YBE),
George Salonikh. Checked on 2026-10-25. The supplied capture runs 2:42:47.
This review sampled Campbell near 00:40 and frame-stepped a short Naomi segment
near 02:41; it did not audit every call in the complete video.

## Mouth count and compositing

For the ordinary simple-portrait path, **three mouth looks** is the useful asset
count. The [reverse-engineered PSX renderer](https://github.com/FoxdieTeam/mgs_reversing/blob/7bbcb71021b59c55adeb9be46074adebaf68d2ad/source/menu/radiofacedraw.c#L155)
describes three mouth animation frames and draws a fixed base portrait followed
by optional mouth and eye images. The independent
[FACE.DAT parser](https://github.com/otac0n/Codec/blob/378ad3f368d4af3850b33487375b7d32a611b2ca/Codec.MGS/Archives/FaceDatArchive.cs#L253)
identifies a base image and two named mouth images. Read together, those support
a neutral base plus two speaking shapes. This is a conclusion from reverse
engineering sources, corroborated visually by the supplied footage, rather than
an official Konami asset specification.

Eyes are separate. The renderer advances its blink sequence over six update
steps; these are not six distinct full portraits or six additional mouth shapes.
Its eye assets include a drooping/partial-lid state. The code also has a separate
full-animation path, so three mouth looks should not be presented as a universal
count for every special portrait or expression in the game. Video compression,
screen effects, blink combinations and held frames make pixel-unique video-frame
counts a poor way to infer the underlying sprite count or original animation rate.

## Choice for this collection

Keep the app's existing **rest / small / open** mouth roles, each with its matching
closed-eye partner: six final PNGs per set. Match the fixed source and overlays
approach by preserving all pixels outside the selected eye/mouth regions, sharing
the same mouth across each eye pair, and sharing eye pixels across mouth states.
There is no need to add extra mouth states based on this reference check.

The app's TTS playback already has a pause gate, smoothing and mouth hysteresis.
These content packs use that existing behavior; they do not change timing or
claim to reproduce the game's scripted animation cadence. A partial-lid frame
could improve blink transitions in a later app change, but it is outside the
current six-role import format and is not supplied as an unused extra slot here.

No original game portraits, audio or code are distributed in these packs.
The MGS footage is a behavioral reference; each pack records its own artwork
source and license separately. [Import instructions](CODEC.md) and
[qualification scope](codec-verification.json) describe what was actually checked.
