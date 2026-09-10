# petdex-install

Help an agent install a requested Petdex companion as an independent Chatbook Buddy,
using the app's review and Apply flow. An optional Python helper prepares a
validated native Buddy archive when file execution is available.

| Field | Value |
| --- | --- |
| Version | 1.1.0 |
| Author | tldw-project |
| License | [Apache-2.0](LICENSE.txt) for this skill/helper; downloaded pets retain their own terms |
| Target | Chatbook independent Buddies; optional character expressions or Persona artwork |
| Tested application | Chatbook `4cc1a450c74a416595a871362535371c56cc1c1e` integration build |
| Verification date | 2026-09-10 |

## Install the skill

Import this complete directory through **Library → Skills**, then review its trust
state before use. An agent can install the bundle using the collection's
[installation guide](../../../INSTALL.md) and catalog once this revision is published.
Example: “Install `petdex-install` from `rmusser01/tldw-stuff` into Chatbook.”
Installing the skill and installing a pet are separate requests. No companion,
dependency, account connection or trusted-script grant is installed automatically.

## Use

> Install https://petdex.dev/pets/homelander as my Buddy in Chatbook.
> Also make an independent character with animated expressions from it.

With authorized app controls, the agent opens **Console → Menu → Buddy → Import
from Petdex**, reviews the exact pet, stages it with **Use draft**, and installs
and selects it with **Apply**. No Persona is required. Cancelling before Apply
publishes nothing. Without app controls,
the helper can prepare files and provide the remaining import/save steps; it does
not claim to have installed them. Character creation is an optional separate step
when requested.

For manual preparation, from this skill directory:

```sh
python scripts/prepare_pet.py --pet https://petdex.dev/pets/homelander --output ./homelander-buddy
```

The new output directory contains `buddy.tldw-persona-vpack` and a JSON review
receipt. In Buddy management, expand **Import pack & size**, enter the archive's
absolute path and **Apply**. Existing output directories are never replaced.
[Workflow details](references/workflow.md) cover local sources, inspection,
source-bound manual mappings and result codes.

## Requirements

- An agent/LLM and authorized app controls, or local Python/file execution.
- For the helper: Python 3.11+ with a compatible Chatbook build and its required
  dependencies, including Pillow, installed in that interpreter. The Petdex feature
  may not exist in an older release; no automatic upgrade is attempted.
- Public Petdex preparation requires HTTPS access to petdex.dev and assets.petdex.dev.
  Downloaded local packages need no network. Remote reads use Chatbook's validated
  transport; the Petdex CLI is not required.
- The output parent directory must exist and be writable. Run the helper as a
  separate process; it uses disposable configuration and never publishes a profile.
- Server installation and installation into other products are untested/unsupported
  by this workflow. Their skill-folder support does not supply Chatbook APIs.

## Files, attribution and updates

[SKILL.md](SKILL.md) contains agent instructions; [prepare_pet.py](scripts/prepare_pet.py)
uses installed application APIs; [workflow.md](references/workflow.md) documents
manual mapping and the app handoff. UI discovery metadata is in
[agents/openai.yaml](agents/openai.yaml). [PROVENANCE.json](PROVENANCE.json) records
sources and [SHA256SUMS](SHA256SUMS) identifies distributed bytes.

All bundle text/helper code is original tldw-project content. Chatbook remains an
external AGPL dependency; no application implementation or third-party pet art is
redistributed or relicensed here. Original pet creators and terms travel in the
prepared native archive. Unknown terms remain unspecified.

Before updating an installed copy, preserve customizations and compare the new
bundle. Recheck the app interfaces, run the targeted helper/import tests and
refresh checksums/catalog. See [verification](../../../docs/petdex-install-verification.md)
for executed checks and limits; this is not a claim of automatic pet installation
in a live user session.
