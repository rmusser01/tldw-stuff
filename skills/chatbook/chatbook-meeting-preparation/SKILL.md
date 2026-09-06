---
name: chatbook-meeting-preparation
description: Prepare meeting agendas and pre-reads from Chatbook notes or supplied context, with source references, decision questions, timeboxes and carry-over actions. Use for planning, status, decision, retrospective, brainstorming or one-on-one meetings.
license: MIT; original Notion Labs notice retained in LICENSE.txt
---

# Meeting preparation for Chatbook

Adapted from Notion Labs' `notion-meeting-intelligence` in openai/skills.

1. Establish the meeting objective, attendees, duration, date and decisions needed.
   Use known context; ask only for information that affects the preparation. Keep
   unknown details marked as unresolved.
2. Read [Chatbook note operations](reference/chatbook-notes.md). Search relevant
   project and earlier meeting notes, inspect the actual content, and separate
   current facts from older decisions or conflicting accounts. User-supplied notes
   can be used without a connector. Do not initiate external research by default.
3. Choose a fitting [meeting template](reference/template-selection-guide.md).
   Adapt the sections to the meeting, omit irrelevant fields, and allocate agenda
   timeboxes within the known duration. Use factual sources for pre-read claims.
4. Draft an agenda and pre-read with source references, decisions/questions to
   resolve, relevant options/trade-offs, risks and carry-over actions. Proposed
   decisions stay proposed; agenda preparation does not record an outcome that
   has not happened. Do not assign owners or deadlines without evidence.
5. Check that an attendee can understand why the meeting exists and what input is
   needed. Check dates against the supplied context, distinguish conflicting
   sources, and make any missing evidence visible. Remove unfilled template
   placeholders or label unknown values clearly.
6. Return the draft, or save it with `create_note` when the user requests saving.
   Update an existing note only under the version/content conditions in the
   operations reference. Report its actual ID and any unresolved questions.
   Preparing a meeting note does not send invitations or notify attendees.

For realistic evaluation cases, see [behavior checks](evaluations/cases.json).
