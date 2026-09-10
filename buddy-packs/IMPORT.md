# Import a Buddy pack

Keep the item README and its referenced license/provenance notices with your
download. The shipped default archives do not embed those repository notices inside
the archive. The original companion and reference-trio archives include creator and full
Apache-2.0 notice metadata; keep their accompanying files for hosts that do not
preserve that metadata on export.

Download the `.tldw-persona-vpack` file from an item's directory (on GitHub use
**Download raw file**). Keep its extension. It is the native ZIP-based
`tldw.persona_visual_pack.v1` format, including the visual manifest in
`metadata/pack.json`, asset declarations in `metadata/assets.json`, all PNG bytes
under `assets/persona_visuals/`, and `checksums/sha256.json`.

For shipped defaults, `starter-catalog.json` is the original server catalog detail and production recipe
for reference. It is **not** the file to import. Its fixture asset keys precede
the exporter's native ID remapping. The archive is self-contained.

## Chatbook: independent Buddy

A Persona is optional. On a build with **Buddy & Persona Management**:

1. In **Console**, choose **Menu → Buddy**.
2. Expand **Import pack & size** and enter the downloaded archive's local path,
   for example `~/Downloads/trenchcoat.tldw-persona-vpack`. Full paths and paths
   surrounded by matching single or double quotes are accepted.
3. Enable the Buddy and choose the conversation or workspace it should follow.
   Create that target first if your profile has none. Leave the Persona choice
   unchanged unless you also want to change assistant behavior.
4. Choose **Apply** to import and save. Reopen management to check the selected
   Buddy and target, then close the modal to see the artwork.

Artwork import does not need a model, API key or image-generation service.
Conversation replies and optional speech need their own configured services.
Static/Dynamic controls change expression playback, not the attached assistant.

Use the downloaded file itself, not its GitHub page URL, a saved HTML page,
`starter-catalog.json`, a folder or a filesystem link. Do not unzip or rename
the archive to import it.

| Import problem | Next step |
| --- | --- |
| File cannot be found | Check the download location and pasted path. On an older build, use an unquoted full path or update to a build containing [the path-import fix](https://github.com/rmusser01/tldw_chatbook/pull/2551). |
| Pack is invalid or unsupported | Download the `.tldw-persona-vpack` again using **Download raw file**; check the pack's compatibility record. |
| Installation or settings could not be saved | Check profile storage permissions and free space, then retry. Reopen management to inspect what was saved before creating another copy. |

See [Chatbook's Buddy guide](https://github.com/rmusser01/tldw_chatbook/blob/dev/Docs/User_Guide/buddy.md)
for controls and troubleshooting.

## Chatbook: artwork for a Persona

Use this path when you specifically want to edit a Persona's own visual pack,
or your build has the older Persona Visual editor:

1. Open the Personas editor and select or create a local Persona. Save the Persona first.
2. In **Persona Visual**, choose **Import Pack…** and select the downloaded archive.
3. Review its states and image previews. Choose **Save Pack** to publish it to that Persona.
4. Select a listed state to preview the saved pack. The Persona Buddy uses the active pack.

A saved local Persona is required for this editor. Previewing a draft does not
publish it. Importing into a Persona does not itself create an independent Buddy
or a character card. For server-backed storage, use the server workflow below.

## Server, WebUI and extension

The server can own independent Buddies with no associated Persona. Open
**Buddy & Persona** from the chat composer or workspace, choose **Your Buddies**
or **Choose a ready-made Buddy**, select **One conversation** or **Workspace**,
and choose **Apply**. These controls share the same server-backed artwork and
attachment model. See the [management guide](https://github.com/rmusser01/tldw_server/blob/dev/Docs/User_Guides/WebUI/Buddy_And_Persona_Management.md).

At the server revision checked below, this dialog has no downloaded-pack upload
control. Downloaded collection packs use the Persona import API first; an
independent copy can then be created through the Buddy API. Selecting ready-made
artwork does not install a downloaded collection pack.

### Import a downloaded pack

Use the authenticated server's API docs at `/docs` with Persona enabled and the
Persona job worker running. Create or choose a Persona owned by your account.
The routes below use the default `/api/v1` prefix; follow your installation's
configured prefix if different.

1. `POST /api/v1/persona/profiles/{persona_id}/visual-packs/import-previews`:
   upload the downloaded file as the multipart **archive** field. Keep the returned `preview_id`.
2. `GET /api/v1/persona/profiles/{persona_id}/visual-packs/import-previews/{preview_id}`:
   wait for completed validation and review the warnings, asset counts and choices.
3. `POST /api/v1/persona/profiles/{persona_id}/visual-packs/import-previews/{preview_id}/commit`:
   submit `{"trust_mode":"untrusted_import","target_mode":"create_new"}`.
   This creates a new draft and retains existing packs. Keep the returned `job_id`.
4. `GET /api/v1/persona/profiles/{persona_id}/visual-packs/imports/{job_id}`:
   wait for completion. Review the resulting draft before activating it in your
   Persona visual-pack editor.

### Create an independent Buddy from the imported artwork

The existing server import-job repository requires SQLite storage. PostgreSQL
Buddy snapshots and native exports are separate supported paths.

After the import completes, use the actual destination Persona and imported
pack IDs with authenticated `POST /api/v1/buddies`:

```json
{
  "name": "Trenchcoat",
  "source": {
    "kind": "persona_pack",
    "persona_id": "YOUR_PERSONA_ID",
    "pack_id": "YOUR_IMPORTED_PACK_ID"
  },
  "optional_persona_id": null,
  "display_mode": "dynamic"
}
```

Replace both placeholders with IDs returned by your server. Review the imported
artwork before copying it. The source Persona must be owned by you and active;
the pack must contain valid, complete artwork. The Buddy receives its own artwork
snapshot, and `optional_persona_id: null` leaves it without a Persona association.
Keep the returned Buddy ID and verify it with `GET /api/v1/buddies/{buddy_id}`.

Reopen **Buddy & Persona**, select the new entry under **Your Buddies**, choose
its conversation or workspace and **Apply**. Creating the artwork record alone
does not attach it. API clients can use the versioned attachment workflow in the
[Buddy API reference](https://github.com/rmusser01/tldw_server/blob/dev/Docs/API/Buddies.md).

Keep the supplied license and provenance files with server copies. A live check
of server `50c1f68957` confirmed that import discarded embedded artwork credits,
which also removed them from independent copies and exports. The repair is in
[server PR #2940](https://github.com/rmusser01/tldw_server/pull/2940); use a build
containing that change before relying on embedded-credit preservation.

To recover credits already lost by an older import, re-import the original
credited archive and make a new independent Buddy. Existing copies are not
silently rewritten. Archives that never embedded notices still need their
accompanying files.

## Verification scope

The independent-install instructions were checked against Chatbook
`02374bf66af4e6a594d1a63f7f2d559554714fa8` and server
`50c1f689575b1bc21ed3e78cdb193b03fe968cdd` on 2026-09-10. A subsequent live
Trenchcoat check used the actual authenticated server import/export worker:
preview, commit, independent copy, export and re-import completed. After the
repair in PR #2940, the exact creator, source URL, license, 11,654 UTF-8 bytes
of notices and every PNG byte survived. The exported archive also passed
Chatbook's actual native importer with 18 activatable states and exact credits.
These checks do not constitute a native-terminal or installed-extension walkthrough.
See the [source-bound verification receipt](https://github.com/rmusser01/tldw_server/blob/0e72f25515/Docs/Reviews/2026-09-10-buddy-followup.md). [Chatbook PR #2551](https://github.com/rmusser01/tldw_chatbook/pull/2551)
records the Trenchcoat import fix and mounted-dialog regression coverage.
Older released builds may lack independent management or pasted-path support.

### Earlier archive verification

The seven shipped defaults and six scaffolds were verified on 2026-09-05.
Those archives were produced through the server's
`PersonaVisualStarterCatalogService.copy_starter_pack_to_persona` and
`PersonaVisualPackExporter.export_pack(strict=True)` using a disposable SQLite
database and private temporary assets. Every archive then passed
`PersonaVisualPackImportPreviewer.create_preview` and
`PersonaVisualPackImporter.import_preview(trust_mode="untrusted_import")` into
another Persona, yielding an inactive draft. Asset counts and every original
PNG SHA-256 matched, and required-state manifests validated as activatable.

The same files passed Chatbook's `import_persona_visual_pack`,
`persona_visual_draft_publication_snapshot`, and `publish_persona_visual` into
a disposable SQLite database and private profile. Reloaded active graph
identities and asset counts matched, and import review staging cleaned up.
These are actual application service and persistence checks; the HTTP worker
and graphical/terminal UI flows were not exercised live. No existing user
profile, database, credentials or configuration was exported or modified.

See [verification.json](verification.json) for each file's size, SHA-256 and
observed counts. An import passing validation does not complete scaffold art.

The [twelve new companions](README.md#new-companion-collection) have a separate
[2026-09-08 verification record](../docs/buddy-collection-verification.md), including
native import in both applications and independent animated-character conversion
in Chatbook.

[Dipsy (Qipao), Kimi and Cappy](README.md#dipsy-kimi-and-cappy) have their own
[verification record](../docs/reference-trio-verification.md). Their archives also
embed the anonymous reference credit; keep each pack's NOTICE.txt with copies.
