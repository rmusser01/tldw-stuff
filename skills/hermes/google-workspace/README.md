# google-workspace

Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.

## Attribution and contents

- Author credit from upstream: **Nous Research**; publisher: **NousResearch and upstream contributors**.
- [Original source](https://github.com/NousResearch/hermes-agent/tree/245e48008fa814b3251f50755eb656bd9fb86cb1/skills/productivity/google-workspace) at `245e48008fa814b3251f50755eb656bd9fb86cb1`, retrieved 2026-09-05.
- [History and contributors](https://github.com/NousResearch/hermes-agent/commits/245e48008fa814b3251f50755eb656bd9fb86cb1/skills/productivity/google-workspace).
- License: [MIT](UPSTREAM_ROOT_LICENSE.txt); all original notices and supporting files retained.
- [SKILL.md](SKILL.md), [source manifest](UPSTREAM.json), [checksums](SHA256SUMS).

Collection documentation and attribution metadata are additions under the
repository’s [Apache-2.0 default](../../../LICENSE). No upstream endorsement is implied.

## Chatbook compatibility

The helper is distributed as `scripts/hermes_home.py` with its import statements
adjusted, allowing the whole bundle through Chatbook’s directory and ZIP importer.
Its implementation is unchanged. The manifest retains original paths and source
hashes and identifies each adapted import statement; MIT notices are preserved.

## Requirements and use

gws CLI or the supplied Python integration, Google OAuth/application setup and network access. Can access Gmail, Calendar, Drive, Docs and Sheets. It is a separate integration from OpenClaw gog.

Follow the [directory import guide](../../IMPORT.md), selecting this individual
folder or its SKILL.md. Example: ask the assistant to use `google-workspace` for the
specific task described above, with your intended input and destination.

The upstream instructions remain unchanged. Hermes/OpenClaw tool names, profile
paths, installers and account integrations are not translated or configured by
Chatbook import. Review the upstream prerequisites before execution and resolve
helpers relative to this complete directory. Only configured and authorized host
tools may perform external writes, send messages, install dependencies or schedule
work. The content itself grants none of those permissions.

## Verification and updates

Content version: **1.0.1**. See [verification results](../../verification.json)
for the pinned Chatbook import outcome and any helper smoke checks.
File import is not runtime compatibility certification. Live service calls,
authentication setup, workflow quality, and other-host imports were not tested.

Keep customized copies separately. Update by reviewing a new upstream revision,
refreshing files, notices and checksums, and repeating the relevant import and
helper checks. Provider commands and dependency versions may change over time.
