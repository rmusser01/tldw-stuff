# Note formats

Adapted from the six knowledge-capture database references by Notion Labs.
Choose only the fields useful for this note; store them as Markdown content.

| Purpose | Suggested title | Body sections |
| --- | --- | --- |
| Decision | Decision: subject | Context; status (proposed/accepted/superseded, backed by evidence); decision; rationale; alternatives; consequences; implementation; sources. |
| How-to | How to complete a task | Prerequisites; ordered steps; expected result; troubleshooting; verification actually performed; sources. |
| FAQ | The user's question | Short answer; explanation; steps if relevant; related questions with observed note IDs; sources. |
| Reference | Topic: reference | Purpose; concepts or facts; boundaries; examples; source dates; unresolved questions. |
| Team knowledge | Team/topic: resource | Purpose; audience; procedures or reference material; maintainer if known; related note IDs; sources. |
| Learning | Event: lessons learned | What happened; what worked; what failed; causes supported by evidence; lessons; follow-up actions with known owners/dates; sources. |

Use a source section that separates evidence from interpretation. A note's title
and observed ID are sufficient for a local cross-reference when no actual URL
exists. Do not fabricate Notion-style page links or a Chatbook note URL scheme.

Example structure for a decision whose outcome is still open:

```markdown
# Decision: search backend
Status: Proposed

## Context
The team needs to compare two approaches for the stated workload.

## Options and evidence
Record each option and the claims actually supported by the supplied notes.

## Open questions
Record the measurements or decisions still needed.

## Sources
List the actual source titles and IDs supplied by tools or the user.
```

Do not turn a maintainer field into a claimed permission boundary. Do not invent
review dates, helpfulness counts, automated views or native relations. Preserve
an existing note's useful content and naming conventions when proposing updates.
