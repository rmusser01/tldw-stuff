# Repository design

## Purpose

Provide an optional, public content reference for tldw_chatbook and tldw_server
so users can choose additional content independently of application installs.

## Structure and ownership

Use human-browsable category directories and self-contained item directories.
Keep native import formats; describe compatibility and provenance in each
item's README. Category READMEs form the catalog, avoiding a second generated
index or custom manifest schema. The initial repository contains scaffolding
only. Existing app content and defaults remain unchanged.

## Distribution

Individual files and sparse Git checkouts support selective retrieval. Large
optional assets belong in versioned releases with checksums and attribution.
There is no automatic installation, content execution, synchronization, or
runtime dependency on this repository. App integration or content migration
requires a separate change in the relevant application.

## Verification

Check local links, Git whitespace, file sizes, and the published repository
state for the scaffold. Content submissions additionally require an actual
import/use check on every claimed target, with version and result recorded.

## Decision

ADR required: no application ADR. This creates a standalone reference and does
not change application storage, service contracts, or runtime behavior. This
document records the content repository's organization and distribution choice.
