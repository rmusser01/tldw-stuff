# product-price-monitor

Watch product, flight, or listing prices; alert on target.

## Attribution and contents

- Author credit from upstream: **Ben Barclay (benbarclay), Hermes Agent**; publisher: **NousResearch and upstream contributors**.
- [Original source](https://github.com/NousResearch/hermes-agent/tree/245e48008fa814b3251f50755eb656bd9fb86cb1/skills/productivity/product-price-monitor) at `245e48008fa814b3251f50755eb656bd9fb86cb1`, retrieved 2026-09-05.
- [History and contributors](https://github.com/NousResearch/hermes-agent/commits/245e48008fa814b3251f50755eb656bd9fb86cb1/skills/productivity/product-price-monitor).
- License: [MIT](UPSTREAM_ROOT_LICENSE.txt); all original notices and supporting files retained.
- [SKILL.md](SKILL.md), [source manifest](UPSTREAM.json), [checksums](SHA256SUMS).

Collection documentation and attribution metadata are additions under the
repository’s [Apache-2.0 default](../../../LICENSE). No upstream endorsement is implied.

## Requirements and use

Authorized browsing/provider tools, persistent storage, a scheduler and a notification destination. Hermes scheduling calls are not supplied by Chatbook import; prices and live alerts were not tested.

Follow the [directory import guide](../../IMPORT.md), selecting this individual
folder or its SKILL.md. Example: ask the assistant to use `product-price-monitor` for the
specific task described above, with your intended input and destination.

The upstream instructions remain unchanged. Hermes/OpenClaw tool names, profile
paths, installers and account integrations are not translated or configured by
Chatbook import. Review the upstream prerequisites before execution and resolve
helpers relative to this complete directory. Only configured and authorized host
tools may perform external writes, send messages, install dependencies or schedule
work. The content itself grants none of those permissions.

## Verification and updates

Content version: **1.0.0**. See [verification results](../../verification.json)
for the pinned Chatbook import outcome, omissions, and any helper smoke checks.
File import is not runtime compatibility certification. Live service calls,
authentication setup, workflow quality, and other-host imports were not tested.

Keep customized copies separately. Update by reviewing a new upstream revision,
refreshing files, notices and checksums, and repeating the relevant import and
helper checks. Provider commands and dependency versions may change over time.
