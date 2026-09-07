# Personas

Six default persona archetypes shipped by tldw_server, preserved as native YAML.
Each directory includes the original payload, provenance, exact loader steps,
and verified compatibility.

| Archetype | Purpose |
| --- | --- |
| [Blank Canvas](blank-canvas/README.md) | Start from scratch and configure everything yourself. |
| [Project Manager](project-manager/README.md) | Track tasks, organize work, and keep projects moving forward. |
| [Research Assistant](research-assistant/README.md) | Deep-dive into any topic with structured analysis and source management. |
| [Roleplayer](roleplayer/README.md) | Immersive character interaction and collaborative storytelling. |
| [Study Buddy](study-buddy/README.md) | Learn smarter with flashcards, quizzes, and guided review sessions. |
| [Writing Coach](writing-coach/README.md) | Sharpen your prose with thoughtful feedback and structured guidance. |

These files seed assistant setup: persona prompts, module and policy defaults,
voice settings, starter commands, and optional Buddy metadata. They are not
character cards or Persona Buddy visual packs. The pinned server already includes
them; downloading this repository does not change application defaults.

## Buddy companions

The [finished Buddy packs](../buddy-packs/README.md#finished-packs) are published
separately and can be attached to a saved Persona through the
[Buddy import workflow](../buddy-packs/IMPORT.md). The archetype YAMLs do not name
visual-pack IDs or contain artwork. Their original Buddy seed metadata is:

| Persona | Species | Palette | Silhouette |
| --- | --- | --- | --- |
| Blank Canvas | None | None | None |
| Project Manager | beaver | earth | standing |
| Research Assistant | owl | warm | round |
| Roleplayer | fox | twilight | playful |
| Study Buddy | dog | cheerful | round |
| Writing Coach | cat | cool | sitting |

These seeds are setup suggestions. The collection does not include matching
animal-art packs or define a one-to-one pairing with the finished visual packs.
Choose a published visual pack independently when configuring the Persona.

All six passed the real tldw_server archetype loader and schema at commit
[`36b846628d77`](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/tldw_Server_API/app/core/Persona/archetype_loader.py)
on 2026-09-05. Verification covered individual-directory loading and in-memory
cache lookup/list operations. Live setup, HTTP access, model behavior, and UI
uploads were not tested. Follow each README for the verified use path and limits.

The native YAMLs retain [GPL-3.0-only](LICENSE) from the
[upstream license scope](https://github.com/rmusser01/tldw_server/blob/36b846628d7755e91e0d5539740a9f5c9a837966/LICENSE); this index and the new item READMEs follow
this repository's [Apache-2.0 default](../LICENSE). Attribution:
Copyright (c) 2026 Robert Benjamin Jake Musser.

The unchanged upstream scope notice is also preserved locally in
[UPSTREAM_LICENSE.md](UPSTREAM_LICENSE.md). Its path scopes describe the upstream
repository; the YAML license attribution above identifies their scope here.
