---
name: report-conversation
description: >
  Generate privacy-aware conversation reports and log them locally or deliver them to external recipients.
---

## What I Do

- Create structured summaries of user-agent conversations.
- Highlight decisions, risks, verification status, and next steps.
- Apply privacy checks before any external delivery.
- Deliver reports through local Markdown files and approved Zulip topics (via ZulipChat MCP).

## When To Use Me

Use this skill when:

- The user asks to:
  - Regularly report conversation progress to colleagues or staff.
  - Generate end-of-session, daily, or weekly status updates.
  - Produce auditable records for project governance.

## Workflow

1. Identify report scope: session, today, since-last-report, or custom range.
2. Build a concise factual summary from the current conversation context.
3. Extract: objectives, actions taken, files discussed, decisions made, unresolved issues, and proposed next steps.
4. Apply privacy filter: remove credentials, secrets, personal data, and unnecessary raw transcripts.
5. Produce human-readable markdown report.
6. Use the prettier formatter to improve the format of the markdown report.
7. Display the report draft.
8. Ask for delivery mode with an input form.
9. Send the report.
10. Verify sending status and return the sending status.

## Delivery Modes

Support these delivery modes:

- local
- external
- local+external

For local+external, send exactly the same report to both delivery paths in one run.

## Report Structure

- Title
- Date and time
- Scope
- Audience
- Confidentiality classification
- Executive summary
- Key requests and outcomes
- Decisions and rationale
- Evidence and verification notes
- Risks and open questions
- Recommended next steps

## Local Delivery

- Directory name: agent-logs
- File name: Timestamp-Abbreviated-Title (Note: Replace timestamp and abbreviated title with actual data.)

## External Delivery

- Use the MCP server `zulipchat` to send the report to the topic `agent logs` in the channel `general`.

## Safety and Policy Rules

- Never publish sensitive content through public share links unless the user explicitly requests public release.
- Treat external delivery as sensitive action and request explicit confirmation first.
- If outbound tools are unavailable, output a ready-to-send report and a local logging plan.
- Prefer minimal disclosure: share only what the audience needs.
