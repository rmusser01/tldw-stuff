# Import and compatibility

## Chatbook local library

1. Download the complete skill directory, preserving its relative paths and license files. For example, choose `skills/openai/jupyter-notebook`.
2. In Chatbook’s Library → Skills, use the local Import row with that directory’s absolute path or its `SKILL.md` path.
3. Import one skill at a time. A publisher directory such as `skills/openai` does not itself contain a SKILL.md and is not a batch import target.
4. Review the imported instructions, scripts, requirements, and trust state before enabling their use. Directory import does not install dependencies, approve scripts, or supply API credentials.

Example selective checkout:

```sh
git clone --filter=blob:none --sparse https://github.com/rmusser01/tldw-stuff.git
cd tldw-stuff
git sparse-checkout set skills/openai/jupyter-notebook
```

For a scripted local import in an environment with Chatbook installed, this is
the native service call exercised by our verification. Replace the source and
store paths with your chosen directories; the example intentionally uses a
separate store and does not alter an existing profile:

```python
import asyncio
from pathlib import Path
from tldw_chatbook.Skills_Interop.local_skills_service import LocalSkillsService

async def main():
    source = Path("/path/to/tldw-stuff/skills/openai/jupyter-notebook")
    service = LocalSkillsService(store_dir=Path("/path/to/separate-skill-store"))
    await service.import_skill_directory(
        source, name=source.name, trust_approved=False
    )

asyncio.run(main())
```

The service import, stored file bytes, and owner executable bits were checked
against Chatbook commit `7584478d7a6562a1c3fb094a24e103706f1915f8` on 2026-09-05.
The UI route above was inspected in source, not driven in a live GUI. All skills
remained untrusted in the verification store. The tested path validator rejects
leading underscores. It omitted skill-creator’s
empty `scripts/__init__.py`, and the nonempty `scripts/_hermes_home.py` dependency
from Hermes google-workspace and grounded-citations. The latter two imported
bundles are incomplete for helper execution; use their complete repository
directories. Other files were preserved. See [verification.json](verification.json).

## Host-specific assumptions

Publisher snapshots are unchanged, so importing them does not translate their
runtime assumptions. The two separately labeled Chatbook note adaptations do
replace the original Notion workflow and tool mapping. Publisher-specific examples:

- OpenAI notebook instructions refer to `$CODEX_HOME/skills/...`. On another host, resolve the script within the imported skill’s actual directory; importing into Chatbook does not create that Codex path.
- OpenClaw video examples use `{baseDir}`. It denotes the skill directory in OpenClaw; use the actual skill path when running the helper manually elsewhere. OpenClaw `metadata.requires` and `metadata.install` describe dependencies and do not install them through Chatbook.
- Anthropic’s web-artifacts-builder downloads frontend packages, can install pnpm globally, and rebuilds output in its working directory. Its Claude display step does not automatically register an artifact with Chatbook. See its item README before running the scripts.
- Anthropic examples may refer to Claude tooling such as WebFetch, browser helpers, or MCP clients. Configure equivalent authorized tools before using the workflow.

Do not assume a skill’s example tool names grant permissions or that its
upstream installer metadata has been executed. Dependency and network needs
are listed in every item README. Keep local path changes in a customized copy;
the published copy remains traceable to its upstream revision.

## Other hosts and runtime verification

Server, Codex, Claude, OpenClaw and Hermes host imports were not exercised. No live LLM
workflows, cloud API calls, credential setup, model downloads, or dependency
installations were performed. This is a reference collection with verified
Chatbook file import, not a promise of automatic cross-host execution.

Initial local helper smoke checks passed: both notebook scaffold templates generated
valid notebook JSON, and the video helper extracted a PNG from a synthetic clip.
Python and shell syntax checks passed. These checks do not evaluate the quality
of generated writing, diagrams, or threat models.

Additional offline checks exercised skill-creator validation and packaging, and
GitHub comment retrieval fixtures. The latter reproduced upstream fork lookup
and pagination limitations documented in its [README](openai/gh-address-comments/README.md).
Claude evaluation and live GitHub retrieval were not exercised.

## Hermes and Chatbook note adaptations

Hermes source paths such as `${HERMES_HOME}/skills/productivity/...` refer to
Hermes's installation. This collection groups entries under `skills/hermes/`;
resolve scripts from the actual complete bundle and review dependencies before
running. Import does not install Hermes, OAuth flows, cron, browser tools or agent
workers. Original examples may reference sibling skills outside this selection.

The [Chatbook note adaptations](chatbook/README.md) use the actual local note
schemas. They preserve source evidence, expose unavailable-tool and conflict
outcomes, and do not claim that note text creates native tags, relations or tasks.
Their reference files explain the limitations of snippet reads and versioned updates.

Hermes DOCX, PowerPoint and XLSX create/read helpers passed isolated file checks.
The Chatbook note tools passed isolated SQLite create/search/expand/update and
stale-version checks. Office layout rendering and formula recalculation were not
exercised. These helper checks do not certify end-to-end LLM workflow behavior.
