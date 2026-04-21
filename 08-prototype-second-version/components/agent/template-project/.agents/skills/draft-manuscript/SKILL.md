---
name: draft-manuscript
description: >
  Draft technical-scientific manuscripts from notebooks, Python code, run outputs, and
  partial drafts using a structured workflow for planning, section writing, and revision.
  Outputs Markdown and supports placeholder citations for later completion.
---

## What I Do

- Convert technical artifacts into manuscript-ready prose, including Jupyter notebooks, Python files, logs, and partial drafts.
- Propose a clear manuscript structure before writing full prose.
- Draft and revise sections such as title, abstract, introduction, methods, implementation details, results, discussion, and conclusion.
- Improve logical flow, scientific tone, and internal consistency across sections.
- Produce a final Markdown draft with explicit assumptions and unresolved citation placeholders.

## When To Use Me

Use this skill when the user asks to:

- Draft a manuscript or paper from code, notebooks, and technical project artifacts.
- Write or improve a specific scientific section (for example abstract or discussion).
- Turn implementation and analysis work into a coherent narrative for internal or external reporting.
- Refine language, structure, and clarity of an existing draft.

## Input and Output Contract

Inputs may include:

- Jupyter notebooks (.ipynb) and Python source files (.py).
- Experiment outputs, logs, tables, and metric summaries.
- README files, technical docs, and architecture notes.
- Existing manuscript excerpts or full draft text.
- Target audience and publication constraints if provided.

Output:

- Markdown only.
- Include clear section headings.
- Preserve user-provided terminology unless the user asks for changes.

## Workflow

1. Clarify drafting objective: full manuscript, section-level draft, or revision-only pass.
2. Collect minimum context from technical artifacts: pipeline purpose, methods, implementation details, outputs, evidence, audience, and required sections.
3. Map technical evidence to manuscript sections (for example methods from notebooks/code, results from outputs/tables, limitations from known constraints).
4. Propose structure first and ask for confirmation when scope is ambiguous.
5. Draft section by section, keeping claims tied to provided evidence.
6. Run one revision pass for coherence, redundancy removal, and style consistency.
7. Deliver Markdown draft with a short list of open gaps (missing data, missing references, unresolved assumptions).

If essential context is missing, ask concise follow-up questions before drafting unsupported content.

## Citation and Evidence Policy

- Prefer user-provided sources and references when available.
- Prefer evidence grounded in provided code/notebook artifacts and user-provided sources.
- If citation details are missing, use explicit placeholders such as [REF], [REF-1], or [TODO-CITATION].
- Never invent bibliographic metadata (DOI, authors, title, venue, year) when unknown.
- Mark any uncertain statement clearly so the user can verify it.
- Keep claims proportional to the evidence provided.

## Style and Quality Rules

- Use precise scientific language and avoid inflated claims.
- Maintain consistent terminology and notation throughout the draft.
- Prefer clear paragraph topic sentences and smooth transitions.
- Describe implementation choices and analysis steps at a level that another technical reader can reproduce.
- Keep methods and results factual; place interpretation mainly in discussion/conclusion unless requested otherwise.
- Explicitly state assumptions where needed.
- Keep output concise but complete for the requested scope.

## Boundaries and Non-Goals

- Do not perform automated bibliography formatting pipelines.
- Do not produce journal-submission packages or platform-specific templates unless explicitly requested.
- Do not convert output to LaTeX, DOCX, or PDF.
- Do not claim code behavior, performance, or results that are not evidenced in provided artifacts.
- Do not fabricate experimental results, references, or external evidence.

## Completion Behavior

- After delivering the draft, ask whether the user wants a task summary reported.
- If the user says yes, invoke the reporting workflow via the report-conversation skill.
