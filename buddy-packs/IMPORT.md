# Import a Buddy pack

Keep the item README and its referenced license/provenance notices with your
download. The native exporter does not embed those repository notices inside
the archive.

Download the `.tldw-persona-vpack` file from an item's directory (on GitHub use
**Download raw file**). Keep its extension. It is the native ZIP-based
`tldw.persona_visual_pack.v1` format, including the visual manifest in
`metadata/pack.json`, asset declarations in `metadata/assets.json`, all PNG bytes
under `assets/persona_visuals/`, and `checksums/sha256.json`.

`starter-catalog.json` is the original server catalog detail and production recipe
for reference. It is **not** the file to import. Its fixture asset keys precede
the exporter's native ID remapping. The archive is self-contained.

## Chatbook (local Persona)

1. Open the Personas editor and select or create a local Persona. Save the Persona first.
2. In **Persona Visual**, choose **Import Pack…** and select the downloaded archive.
3. Review its states and image previews. Choose **Save Pack** to publish it to that Persona.
4. Select a listed state to preview the saved pack. The Persona Buddy uses the active pack.

A saved local Persona and a build with Persona Visual support are required.
No model, tool, API key, image-generation service, or additional content is
required to import the artwork. The server-backed Persona editor is a separate
path; use the server endpoints below for that storage.

## tldw_server

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

## Verification scope

On 2026-09-05 every published archive was produced through the server's
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
