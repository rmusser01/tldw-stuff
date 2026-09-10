# Petdex installation skill verification

Date: 2026-09-10 · Creator: tldw-project · Content version: 1.1.0

The approved scope is a collection skill and preparation helper, using Chatbook's
existing app review/save operation. It adds no native agent installation tool and
never writes a Persona database. The optional native pack is handed to available
app controls or to the user with exact remaining steps.

## Tested implementation

- Chatbook commit: `4cc1a450c74a416595a871362535371c56cc1c1e` (independent Buddy management integration).
- The original helper and behavioral trial used `b4e460f75142b37ff3df277fd712bdb1812007f9`; the helper checks and headless application journey were repeated on the integrated implementation.
- Python 3.12, macOS, existing Chatbook dependencies; no dependency installation.
- [Skill](../skills/chatbook/petdex-install/SKILL.md),
  [helper](../skills/chatbook/petdex-install/scripts/prepare_pet.py), and
  [packaging metadata](../skills/chatbook/petdex-install/PROVENANCE.json).

The helper wraps installed native APIs for source validation and archive creation.
It has no publication/profile argument. CLI bootstrap uses a disposable config/data
directory because importing Chatbook's config module can create/migrate config and
create chat dictionary directories. The selected-profile regression checks that an
existing configuration's content and modification timestamp remain unchanged.

## Executed checks

The targeted runner uses a fresh profile before importing application modules:

```sh
python tests/run_petdex_checks.py
```

Run with a Python environment containing compatible Chatbook dependencies. For a
source checkout, set PYTHONPATH to that checkout and its
`packages/tldw_profile_core/src` directory before running. The test runner and helper
use temporary paths, never a hardcoded real profile. Do not import test modules
into a running application process.

Twelve checks cover:
- Classic source → real native archive, original image bytes/creator/notices,
  receipt readback, explicit speaking fallback and `installed: false`.
- Existing output preservation, no unnecessary fetch on collision, cleanup after
  injected write failure, missing-dependency reporting and actionable network failure categories.
- Undeclared eleven-row refusal; source-bound manual row/count/timing acceptance;
  stale source, duplicate JSON keys and invalid frame-count rejection.
- Subprocess preparation without changing the selected profile config.
- Real LocalSkillsService directory import preserving every distributed file and
  leaving trust locked and owner-executable bits intact; execution of the helper from that installed directory.
- Complete GitHub-tree URL → fixture ZIP → native skill import with all files
  retained and trust locked. Branch discovery, DNS and HTTP are fixture-controlled;
  this does not claim the bundle has been published or live-downloaded from GitHub.

The initial helper tests failed because the helper did not exist. After implementation
and the additional boundary checks, all twelve passed. The skill-creator validator,
Ruff lint/format, SHA256SUMS, catalog regeneration/check, local Markdown references
and git whitespace checks also passed.

## Behavioral trial

A read-only baseline without the skill proposed reconstructing standalone profile
publication after resolving identity and guards. It did not fabricate success and
correctly refused guessed eleven-row semantics. This demonstrated a routing difference,
not proof of an unsafe live write.

An independent agent received the actual skill and a local synthetic pet, Python/file
tools, no app controls, and a request to install into Research Assistant while keeping
the floating Buddy selected. It executed inspection and preparation, independently
checked receipt hash, original sheet bytes, animation mappings and credits, and
reported **prepared for import** with the remaining UI steps. It attempted no profile
publication. It also identified missing eleven-row declarations and an unresolved
Persona as missing inputs; those two follow-ups were response evaluations, not GUI runs.

The synthetic archive was 8897 bytes, SHA-256
`dda84caa101c9b00b57fbb357da11c4fea327b6976856324bdd187108db952c4`.

## Live source preparation

The actual helper fetched `https://petdex.dev/pets/homelander` through Chatbook's
pinned transport. It exited 0 with `status: prepared`, `installed: false`, a 2178859-byte
native archive and SHA-256
`f68165117c54d274ad9a3b438891ce56e2b5d42ba08fb839831963fc43cd573d`.
Creator Serhat, original source URL and unspecified license were preserved.
The archive matches the earlier application-level Petdex verification. Config
bootstrap and chat dictionary paths stayed under the disposable directory.
No pet artwork is included in this repository contribution.

## Limits and maintenance

The follow-up used the production Textual app headlessly in a disposable profile.
The real prepared archive was imported through Console Buddy management's native
archive field and Apply. Exactly one independent Buddy was installed without a
Persona. Create character produced fourteen independent expression assets, with
Serhat/source/unspecified terms preserved. Six distinct animation frames were
observed in the visible Dynamic preview; Static retained one frame. Cancelling
management after explicit character creation preserved the character without
applying staged preferences.

After removing the disposable input archive and restarting the app, the Buddy,
character expression files and their hashes, credits and saved selection remained
available. The isolated application journey passed. The skill/helper checks were
also rerun against the integrated application: all twelve passed.

No native terminal control, physical voice check, real-user Persona replacement,
server install, other-product pet install, or automated skill trust approval was
performed. Headless application verification does not establish that every agent
host offers app controls; without those controls the helper still reports only
prepared files and gives the remaining import steps.

The environment emits a pre-existing Requests dependency warning and verbose
Chatbook config logs on stderr; JSON results remain on stdout. This skill does not
upgrade or alter application dependencies. Recheck against the selected Chatbook
build, refresh bundle checksums and rebuild the catalog when changing the helper.
