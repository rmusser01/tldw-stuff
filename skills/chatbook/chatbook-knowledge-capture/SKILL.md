---
name: chatbook-knowledge-capture
description: Turn conversations and source notes into reusable Chatbook decision records, how-to guides, FAQs, reference notes or lessons learned. Use when preserving knowledge with evidence, related note IDs and clear unresolved questions.
license: MIT; original Notion Labs notice retained in LICENSE.txt
---

# Knowledge capture for Chatbook

Adapted from Notion Labs' `notion-knowledge-capture` in openai/skills.

1. Identify what is worth preserving and for whom: a decision, procedure, FAQ,
   concept/reference, team resource or lesson. Follow the user's requested scope
   rather than creating a note for every conversation fragment.
2. Read [Chatbook note operations](reference/chatbook-notes.md). Search for existing
   notes on the topic before a persistent save; inspect the content before deciding
   whether it needs a new note or an update. Distinguish similar titles using IDs.
   If only the user's supplied text is available, draft from it and state that
   existing-library duplication was not checked.
3. Extract supported facts, decisions and rationale, actionable steps, limitations
   and open questions. Keep a proposal distinct from an accepted decision. Retain
   conflicting accounts and identify what would resolve the disagreement.
4. Use the appropriate [note format](reference/note-formats.md). Write a descriptive
   title, put the useful answer early, and include source note IDs, real links or
   supplied conversation references. Preserve exact commands or quotes only when
   necessary and supported. Keep sensitive details within the user's intended scope.
5. Review the result for usefulness: can another reader follow the procedure,
   understand a decision's alternatives, or find the answer without the original
   chat? Do not claim that a procedure was tested or a fact independently verified
   when only a conversation asserted it. Leave unresolved ownership and dates open.
6. Return a draft or save the requested note through `create_note`. Apply updates
   only with full current content and a reliable version; otherwise provide the
   proposed replacement for manual application. Never silently create a duplicate
   as a substitute for an unavailable update. Report the saved note ID or failure.

Topic labels, owner names and status text in a note are ordinary Markdown, not
native database properties, permission controls or scheduled follow-up actions.
For realistic evaluation cases, see [behavior checks](evaluations/cases.json).
