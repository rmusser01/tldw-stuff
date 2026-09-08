# Ask an agent to install a skill

Give an agent the skill name, destination and this guide. For example:

> Install `teach` from `rmusser01/tldw-stuff` into Chatbook. Follow
> https://raw.githubusercontent.com/rmusser01/tldw-stuff/main/INSTALL.md

> Install `property-based-testing`, `customer-research` and `copy-editing` from
> `rmusser01/tldw-stuff` into this Claude Code project. Follow the repository’s INSTALL.md.

> Find `@owner/skill` on ClawHub, inspect the selected version, and install it
> into my OpenClaw workspace.

Use an actual ClawHub owner/skill identifier in the last example. When the target
agent or project is unclear, establish that before writing files. Installation
means acquiring and registering the complete bundle; dependency setup, account
connections and executing the skill are separate operations.

## Instructions for the installing agent

1. Read [catalog.json](skills/catalog.json) and match the requested `name` or
   `id`. Use its exact `path`, `install_url`, README and license. Do not select a
   similarly named publisher’s skill or install the whole collection by default.
2. Read the selected collection README and manifest as package information.
   Installation is not an instruction to perform the workflow inside SKILL.md.
3. Use the destination host’s available installation tool first. Otherwise use
   an authorized CLI or file-import route below. A denied tool/policy operation
   is not permission to switch tools to evade the denial.
4. Preserve supporting files, licenses and provenance. Never install only
   SKILL.md when its bundle includes scripts or references. Use an existing
   destination only when the user authorized replacement; otherwise report the
   collision and leave it intact.
5. Verify the installed path/store entry and expected files. Report the source,
   resolved revision/version, destination, result and any remaining trust review
   or dependencies. Distinguish downloaded, registered and usable.

The catalog’s URLs follow `main`. For a reproducible installation, resolve it
once with `git ls-remote https://github.com/rmusser01/tldw-stuff.git refs/heads/main`,
then load the catalog and install the bundle from that same commit by replacing
`/tree/main/` with `/tree/COMMIT/`. Checksums detect mismatched bytes; they are not
an independent publisher signature. Keep scope to the user’s selected skills.

## Chatbook: built-in agent tool

The Console’s primary agent can use the existing `install_skill` tool when its
skills service and installation-confirmation UI are available. Example call:

```json
{"url":"https://github.com/rmusser01/tldw-stuff/tree/main/skills/matt-pocock/teach"}
```

Call once for each selected catalog entry. Use the folder’s GitHub **tree** URL,
not its `blob/.../SKILL.md` page or the repository root. GitHub release ZIP URLs
are also supported.

Chatbook asks for its built-in installation confirmation, then registers the
bundle locally with trust pending. The user reviews it in **Library → Skills**
before use. The agent must not mark it trusted or claim it ran. This confirmation
comes from Chatbook’s installer, not an extra approval step imposed by this guide.
The tool installs into Chatbook’s local library; it does not install server skills.

The original 69 bundles passed both directory import and the complete
URL-to-ZIP installation path with a fixture transport at the Chatbook revision
recorded in [install verification](skills/install-verification.json). Three small
packaging fixes preserve the usable Python modules while satisfying the existing
path validator; their manifests document the exact changes.

## Codex, Claude Code and OpenClaw: existing CLI routes

If Codex exposes its built-in **skill-installer**, use that tool/skill with the
catalog’s GitHub folder URL. Its GitHub helper supports `--repo`, `--path`,
`--ref`, and an explicit `--dest`. Locate the helper from the installed skill;
do not assume a machine-specific absolute path or install into another host by
accident.

Alternatively, the maintained **skills** CLI supports these project targets:

| Destination | `--agent` value | Project directory |
| --- | --- | --- |
| Claude Code | `claude-code` | `.claude/skills/` |
| Codex | `codex` | `.agents/skills/` |
| OpenClaw | `openclaw` | `skills/` |

From the intended project directory, after confirming the target does not exist:

```bash
npx --yes skills@1.5.23 add https://github.com/rmusser01/tldw-stuff/tree/main/skills/matt-pocock/teach --agent claude-code --skill teach --copy --yes
```

Change the agent and exact catalog URL/name as requested. `--copy` keeps a complete
independent bundle. The `--yes` flags make an already authorized selection
noninteractive; they do not authorize additional skills. Use `--global` only
when the user requests installation across projects. Do not use `--all` for a
named-skill request. Node >=22.20.0 is required by the tested CLI version; npx
may download the CLI and its dependencies. Prefer an existing compatible install
when available. CLI file placement is not proof that a new agent session has
loaded the skill.

The three project targets were tested with every collection skill in disposable
projects; no existing user profile was changed. [Upstream CLI documentation](https://github.com/vercel-labs/skills#readme)
describes other agents and current behavior.

## ClawHub: discover, inspect, install

Use ClawHub as a registry, keeping its owner/version identity separate from this
repository’s catalog. Matching names alone do not establish matching authors or
bytes. Start with the existing `clawhub` CLI; the tested version is **0.23.3**
(Node >=22). An authorized one-off alternative is `npx --yes clawhub@0.23.3`.

```bash
clawhub search "customer research"
clawhub inspect @owner/skill --json
clawhub inspect @owner/skill --version VERSION --files --json
clawhub inspect @owner/skill --version VERSION --file SKILL.md
clawhub --workdir /chosen/workspace --dir skills --no-input install @owner/skill --version VERSION
clawhub --workdir /chosen/workspace --dir skills list
```

Replace placeholders with the owner, version and destination established from
the request and registry metadata. Inspect the files and requirements before
installing. Existing user authorization carries forward, but stop on a registry
block or incompatible package rather than adding force flags. `--no-input` prevents
a CLI prompt from hanging an agent. Public browsing does not require logging in;
if an operation requests authentication, use the host’s normal sign-in flow.
Never print stored tokens into the conversation.

The CLI installs a full skill directory and maintains its own local origin and
lock metadata. Use the path reported by the CLI: owner-qualified entries can
live at `skills/@owner/skill`. It does not register that directory in Chatbook. Chatbook’s current
`install_skill` classifier accepts GitHub tree URLs or HTTPS paths ending in
`.zip`; a ClawHub page or `/api/v1/download?slug=...` URL is not accepted merely
because its response happens to be a ZIP.

For Chatbook, use a verified equivalent upstream GitHub skill folder if one is
provided by the publisher. Otherwise download the chosen ClawHub version to an
isolated staging directory, then use an authorized Chatbook local-directory
import capability as described below. If the agent has only `install_skill` and
no matching GitHub/ZIP URL or permitted local import, state that specific limit;
do not invent a successful install. A blocked filename or incomplete bundle must
also be reported rather than silently discarded.

[ClawHub’s CLI reference](https://github.com/openclaw/clawhub/blob/main/docs/cli.md)
explains search, inspection and versioned installation. `sync` and `publish` upload
content; they are not installation commands. Installing a third-party skill does
not authorize republishing it under ClawHub’s publishing terms.

## Local Git/file fallback

When the host has no suitable installer but permits shell/file operations, use
Git sparse checkout into a new staging directory, then copy/import the chosen
complete folder:

```bash
git clone --filter=blob:none --sparse https://github.com/rmusser01/tldw-stuff.git skill-staging
git -C skill-staging sparse-checkout set skills/matt-pocock/teach
```

For a file-based host, copy that directory into its documented skill location
and verify the result. For Chatbook, copying into an arbitrary project folder
does not register a skill. Use an offered local import tool, the Library import
UI, or an authorized Python call to `LocalSkillsService.import_skill_directory`
with `trust_approved=False`; the [import guide](skills/IMPORT.md) shows the API.
The target store must be the intended Chatbook profile’s actual skills store,
not the sample separate store in that guide. Obtain it from the selected host
configuration; ask when that destination cannot be established. Do not edit the
index or trust store by hand. Dependency execution is not part of file import.

## Maintainers

Regenerate the searchable catalog with `python scripts/build_skill_catalog.py`.
Use `python scripts/build_skill_catalog.py --check` to detect stale entries.
Keep verification records specific to the tested CLI versions and app revision.
