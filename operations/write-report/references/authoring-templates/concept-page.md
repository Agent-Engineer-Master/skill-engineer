# Authoring Template — Concept Page (definitional)

> **When to use this framework.** Definitional documents that define and explain a concept, term, framework, or system. Reader is consulting for reference, not being walked through an argument. There's no recommendation, diagnosis, or decision being made. Wiki pages, glossary entries, framework explanations all fit. See `references/framework-selection-guide.md`.
>
> **How to use this template.** Less stringent than minto-pyramid or rumelt-kernel: no apex governing observation required, no SCQA, no Rumelt kernel, noun-label headers are acceptable. The spec stage exists mainly to lock down the primary concept (D1, optional) and the page structure (D2, optional). D5 (evidence) still fires hard — claims about how the concept works must be sourced.
>
> Spec-judge in `mode: spec-judge` is **OPTIONAL** for `concept-page` framework. If invoked, it grades only D1 (if present), D2 (if structured), and D5.

---

## Frontmatter

```yaml
spec_type: authoring-spec
doc_type: wiki
intent_summary: |
  [What concept is this page about? Who reads it (org-internal, async)? What should they walk away knowing?]
supporting_artifacts:
  - path: [path]
    role: [role]
    description: [one line]
```

---

## D1 — Central claim / definition

What is the one-sentence definition or central claim of this concept? Even on a wiki page, the reader should be able to extract a clear governing observation from the opening paragraph.

> [one sentence]

---

## D2 — Page structure (sections)

List the page sections. Wiki pages can use noun-label headers (e.g., "Definition", "Origin", "Mechanism", "Related concepts"). MECE still matters but less strictly — pages can overlap with sibling wiki pages.

1. [section]
2. [section]
3. [section]
4. (optional) [section]

---

## D5-structure — Sources

List the sources or supporting artifacts this page draws from. Tagging is optional for wiki.

- [source / artifact path] — [what it provides]

---

## Pre-write checklist

- [ ] D1 central claim is clear.
- [ ] Page structure is sensible.
- [ ] Sources are listed.

---

## What the review pass will then grade

For wiki, Pass 1 evaluates D1 (governing observation) and D5 (evidence carries) only. Pass 2 evaluates D5 (no internal codes in prose) and D3 (specificity). Action titles and Rumelt kernel are N/A.
