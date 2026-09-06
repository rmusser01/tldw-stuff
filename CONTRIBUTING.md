# Contributing content

Add one self-contained item per pull request, in the matching collection.
Use a stable lowercase directory name with hyphens, such as
`prompts/meeting-summary/`. Keep related assets beside their content.

## Required information

Start from [the content README template](templates/content-README.md). Include:

- A short description and a useful example of the result.
- The native content files and exact import or use steps.
- Required applications, models, tools, or other dependencies.
- Tested app version or commit, test date, and observed outcome. Mark untested
  targets explicitly; do not infer cross-app compatibility from similar formats.
- Author, original source, modifications, license, and required attribution.
- A content version and any instructions for updating customized copies.

Add a relative link and a one-line description to the collection's README.
Remove its empty-state sentence when adding its first published item.

## Content and formats

Preserve the target application's native formats. A README is descriptive
metadata, not a new import manifest. Character cards, character expression packs,
and Persona Buddy packs have different import paths; document each supported
path separately. Include only verified working payloads, not placeholder cards.

For skills, explain which tools they use, required permissions, network access,
and any scripts or external dependencies. Keep examples free of credentials,
private conversations, personal data, and machine-specific paths. Reviewers
should read scripts and instructions as content, not execute them automatically.

## Keep downloads small

Commit editable text, manifests, attribution, and small previews. Avoid duplicate
copies of assets across packs. Do not commit model weights, datasets, generated
build directories, user databases, caches, or large media archives.

For optional large media, publish a versioned GitHub Release asset and link it
from the item's README. Include its size, SHA-256 checksum, license, and exact
installation steps. Use a specific release URL rather than a moving `latest`
link. Keep the editable source or its documented upstream source available.

## Licensing and provenance

Original contributions follow the repository's AGPL-3.0-or-later default unless
explicitly marked otherwise. For imported or adapted work, preserve the source's
license and attribution, identify modifications, and include the applicable
license text. Record provenance and terms for text, artwork, and scripts
separately if they differ. Do not submit material without permission to
redistribute it; link to its upstream source instead when appropriate.

## Before submitting

- Check that README links and relative asset paths resolve.
- Import the item using its documented steps and record the actual result.
- Check any archive contents and verify published download checksums.
- Confirm the contribution contains no private data or local configuration.
- Keep application runtime changes in the relevant application's repository.
