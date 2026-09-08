# Original Buddy collection verification

Date: 2026-09-08 · Creator: tldw-project · Content version: 1.0.0

The [twelve companion packs](../buddy-packs/README.md#new-companion-collection)
contain finished 2D cartoon artwork, native archives and previews. Their visual
references were the existing Paperclip, Search Lens and Index Card buddies.
The built-in OpenAI image tool generated each character's pose sheet separately.
The user explicitly authorized local background removal, frame extraction and
animation-preview assembly. Each pack includes the exact generation prompt,
input-image digest, prepared source atlas, provenance and Apache-2.0 license.

These optional companions add no application defaults or runtime code. Existing
default Buddy and character-image licenses remain unchanged.

ADR required: no. The collection uses existing native Buddy and character
contracts; it introduces no application interface, storage or ownership change.

## Deliverables

Woodpecker, Rubber Duck, Werewolf, Circle, Square, Rhombus, Octagon, Triangle,
Trenchcoat, Shiba-inu, Dipsy and Ghosty each contain:

- A 512 × 512 transparent RGBA source atlas, containing sixteen 128 × 128 poses.
- A native `.tldw-persona-vpack` archive with the same atlas bytes, 18 state
  mappings, deterministic static selections, and animated sequences for idle,
  thinking, speaking, greeting and celebration.
- A still PNG, an animated GIF gallery preview, manifest and recipe, creator
  attribution, full license text, generation prompt, and SHA-256 inventory.

The GIF previews intentionally use a dark matte because GIF has only one-bit
transparency. Native PNGs retain full alpha. Previews are rendered from the
distributed atlas; they are not screenshots of a running application.
The native archives total 2,525,950 bytes. Exact per-pack sizes and digests are
recorded in [companions-verification.json](../buddy-packs/companions-verification.json).

## Executed application checks

Chatbook development commit:
`b4e460f75142b37ff3df277fd712bdb1812007f9`.

All twelve packs passed the real `import_persona_visual_pack` review,
`publish_persona_visual` save, active-graph reload, native export and re-read.
Every original asset byte and the embedded creator/license carrier survived.
Idle, thinking and speaking resolve to animation with a valid static first frame.
Each saved Buddy converted into eighteen character expressions, including
multi-frame neutral/thinking/speaking images, and published as an independent
character in a disposable database. Character artwork attribution was retained.

Server commit:
`27cd02755563d326d218787ac60e0bc8e0524cb8`.

All twelve identical archives passed the real import preview and committed
untrusted import into separate inactive drafts. Asset counts, original atlas
SHA-256 values, all eighteen states, and activatable manifest validation matched.
Only the configured asset-root locator was redirected into temporary storage;
the importer, validation and database operations were the actual implementation.
These tests do not claim server retention of the archive's artwork carrier on
subsequent export. Keep the supplied license and provenance with server copies.

Each test run created fresh private configuration, profiles and SQLite databases.
No real Persona, account, installed Buddy, credentials or user configuration was
modified. The tests did not drive a live UI or the server's HTTP job worker.
Older releases may support native Buddy import without the newer animated
character conversion and Dynamic/Static preference.

## Artifact and visual checks

Every pack's file checksums, atlas dimensions and alpha channel were checked.
All sixteen frame cells contain visible art and clear edge margins. The still
preview exactly matches the idle atlas frame; the GIF contains the advertised
frame sequence. Source sheets and previews were visually reviewed for consistent
identity, readable facial changes, clean transparency and complete silhouettes.
The rubber duck was corrected to a bath-toy silhouette without feet. Dipsy's
detached water-spout droplets were fitted into their own cell to prevent clipping.
Near-transparent resampling specks were removed before the final builds.

The first Chatbook test failed because the temporary root retained macOS's `/var`
symlink alias; resolving that test path satisfied the native no-follow file
boundary. No importer change was made. The full collection check then caught
low-alpha resampling specks at three cell edges; the source cleanup removed them.

## Reproduce and rebuild

Use a Python environment containing the corresponding tested application and
Pillow. For a Chatbook source checkout, put the checkout and its
`packages/tldw_profile_core/src` on PYTHONPATH. For the server, put its checkout
on PYTHONPATH and use its dependency environment.

```sh
python tests/check_buddy_collection.py --host chatbook
python tests/check_buddy_collection.py --host server
```

Both commands target only the twelve entries in `buddy-packs/companions.json`.
`--pack ghosty` narrows a run; `--report /path/to/report.json` records outcomes.
They isolate configuration before importing application modules. Do not import
the check module into a running application process.

Rebuild an individual pack from its committed reviewed source atlas:

```sh
python scripts/build_buddy_collection.py buddy-packs/ghosty
```

The builder uses Chatbook's native writer and regenerates only that pack's
archive, manifest, previews and checksum file. It does not generate new artwork,
download content, install a pack, or modify an application profile. Update the
source/provenance deliberately, then rebuild, review the visuals, and rerun the
targeted checks before publishing a new content version.
