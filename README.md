# tldw-stuff

Optional prompts, character packs, Buddy packs, skills, and lorebooks for
[tldw_chatbook](https://github.com/rmusser01/tldw_chatbook) and
[tldw_server](https://github.com/rmusser01/tldw_server).

A shared place to discover and contribute content without growing the default
content shipped with either application. Browse here, choose what you want,
and import it into your own installation.

## Browse

| Collection | Contents |
| --- | --- |
| [Prompts](prompts/README.md) | Reusable prompts, templates, and prompt collections |
| [Character packs](character-packs/README.md) | Character cards, expression images, and related assets |
| [Buddy packs](buddy-packs/README.md) | Persona Buddy visuals and animation packs |
| [Skills](skills/README.md) | Agent skills and their supporting resources |
| [Lorebooks](lorebooks/README.md) | World information and character context collections |

The repository currently contains the contribution structure and templates;
no content packs have been published here yet.

## Use only the content you want

Open an item's README for its files, requirements, tested app versions, and
import instructions. Compatibility is recorded per item: inclusion here does
not imply support in both applications.

You can save individual files from GitHub. For packs with several files, use
a sparse checkout to retrieve one directory without downloading every pack:

```sh
git clone --filter=blob:none --sparse https://github.com/rmusser01/tldw-stuff.git
cd tldw-stuff
# Once a pack is listed, replace <pack-name> with its directory name.
git sparse-checkout set character-packs/<pack-name>
```

Keep each pack's directory structure intact. Follow its documented import
steps; downloading a skill does not install or run it. Updates are opt-in:
review changes before replacing content you have customized.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) and copy the
[content README template](templates/content-README.md) into a new item directory.
Keep native app formats, include small previews where useful, and document
provenance, licensing, and a tested import path.

Large optional assets should have versioned release downloads with checksums;
the contribution guide explains how to keep the source tree small.

## Relationship to the applications

This repository is an optional content reference. It has no application runtime,
package dependency, automatic downloader, or installer. Application behavior and
bundled defaults remain controlled by the application repositories. Existing
built-in content is not moved or removed by creating this collection.

## Licensing

Repository-authored documentation and original contributions use
**AGPL-3.0-or-later**, unless a file or pack states different terms. See
[LICENSE](LICENSE). Every content item must identify its license and source;
third-party material retains its own license and attribution. Consult the
item's README and included license files before reusing its assets.
