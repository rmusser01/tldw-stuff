# Hermes skills

42 of the 60 default skill directories from
[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/tree/245e48008fa814b3251f50755eb656bd9fb86cb1/skills),
pinned at `245e48008fa814b3251f50755eb656bd9fb86cb1` (2026-09-05). These are selected bundled defaults,
not a mirror of the optional skill marketplace. They cover office work, research,
creative work, developer tools and personal/workspace integrations.

Publisher files remain unchanged except for documented helper filename/import
compatibility changes in [google-workspace](google-workspace/README.md) and
[grounded-citations](grounded-citations/README.md). Each directory includes the
Hermes root MIT notice, any per-skill notices, source provenance, and collection
use notes. All distributed files now survive native Chatbook import. Import does
not provide Hermes tool names, profile paths, scheduling, accounts or delegation.
Office helper smoke checks are recorded in [verification.json](../verification.json).

| Upstream category | Skill | Purpose |
| --- | --- | --- |
| apple | [apple-notes](apple-notes/README.md) | Manage Apple Notes via memo CLI: create, search, edit. |
| apple | [apple-reminders](apple-reminders/README.md) | Apple Reminders via remindctl: add, list, complete. |
| apple | [findmy](findmy/README.md) | Track Apple devices/AirTags via FindMy.app on macOS. |
| apple | [imessage](imessage/README.md) | Send and receive iMessages/SMS via the imsg CLI on macOS. |
| creative | [ascii-video](ascii-video/COLLECTION.md) | ASCII video: convert video/audio to colored ASCII MP4/GIF. |
| creative | [design-md](design-md/README.md) | Author/validate/export Google's DESIGN.md token spec files. |
| creative | [humanizer](humanizer/README.md) | Humanize text: strip AI-isms and add real voice. |
| creative | [manim-video](manim-video/COLLECTION.md) | Manim CE animations: 3Blue1Brown math/algo videos. |
| creative | [p5js](p5js/COLLECTION.md) | p5.js sketches: gen art, shaders, interactive, 3D. |
| creative | [songwriting-and-ai-music](songwriting-and-ai-music/README.md) | Songwriting craft and Suno AI music prompts. |
| email | [email-inbox-triage](email-inbox-triage/README.md) | Triage an inbox: prioritize threads, draft replies safely. |
| email | [himalaya](himalaya/README.md) | Himalaya CLI: IMAP/SMTP email from terminal. |
| media | [gif-search](gif-search/README.md) | Search/download GIFs from Tenor via curl + jq. |
| media | [songsee](songsee/README.md) | Audio spectrograms/features (mel, chroma, MFCC) via CLI. |
| note-taking | [obsidian](obsidian/README.md) | Read, search, create, and edit notes in the Obsidian vault. |
| productivity | [airtable](airtable/README.md) | Airtable REST API via curl. Records CRUD, filters, upserts. |
| productivity | [box](box/README.md) | Box manages cloud files, sharing, search, and metadata. |
| productivity | [document-to-action-items](document-to-action-items/README.md) | Extract cited obligations, deadlines, tasks from documents. |
| productivity | [docx](docx/README.md) | Create, read, edit, template, and review Word .docx files. |
| productivity | [google-workspace](google-workspace/README.md) | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. |
| productivity | [maps](maps/README.md) | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. |
| productivity | [meeting-action-items](meeting-action-items/README.md) | Turn meeting notes into cited decisions, owners, tickets. |
| productivity | [notion](notion/README.md) | Notion API + ntn CLI: pages, databases, markdown, Workers. |
| productivity | [powerpoint](powerpoint/README.md) | Create, read, edit .pptx decks with python-pptx. |
| productivity | [product-price-monitor](product-price-monitor/README.md) | Watch product, flight, or listing prices; alert on target. |
| productivity | [teams-meeting-pipeline](teams-meeting-pipeline/README.md) | Teams meeting summaries, job replay, Graph subscriptions. |
| productivity | [weekly-review-planning](weekly-review-planning/README.md) | Weekly reset: commitments, stalled work, next-week plan. |
| productivity | [xlsx](xlsx/README.md) | Create, read, edit Excel .xlsx workbooks and CSVs. |
| research | [arxiv](arxiv/README.md) | Search arXiv papers by keyword, author, category, or ID. |
| research | [competitor-news-monitor](competitor-news-monitor/README.md) | Watch named companies for material news; cited digests. |
| research | [grounded-citations](grounded-citations/README.md) | Ground answers and documents in cited, verifiable sources. |
| research | [llm-wiki](llm-wiki/README.md) | Karpathy's LLM Wiki: build/query interlinked markdown KB. |
| research | [rss-feeds](rss-feeds/README.md) | Read RSS, Atom, JSON feeds; discover feeds behind a page. |
| social-media | [reddit-reading](reddit-reading/README.md) | Read Reddit: subreddits, search, threads, users. No browser. |
| social-media | [xurl](xurl/README.md) | X/Twitter via xurl CLI: raw post search, posting, DM, media. |
| software-development | [codebase-inspection](codebase-inspection/README.md) | Inspect codebases w/ pygount: LOC, languages, ratios. |
| software-development | [dogfood](dogfood/README.md) | Exploratory QA of web apps: find bugs, evidence, reports. |
| software-development | [github](github/README.md) | GitHub via gh CLI: PRs, issues, reviews, repos, auth. |
| software-development | [node-inspect-debugger](node-inspect-debugger/README.md) | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. |
| software-development | [python-debugpy](python-debugpy/README.md) | Debug Python: pdb REPL + debugpy remote (DAP). |
| software-development | [simplify-code](simplify-code/README.md) | Parallel 4-agent cleanup of recent code changes. |
| web | [blocked-page-recovery](blocked-page-recovery/README.md) | Use when a fetch fails: 403/429, paywall, WAF, bot wall. |

[Import guide](../IMPORT.md) · [Selection review](../REVIEW.md)
