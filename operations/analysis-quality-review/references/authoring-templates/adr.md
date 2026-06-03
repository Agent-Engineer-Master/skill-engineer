# Authoring Template — ADR (decision record)

> **When to use this framework.** Decision records that capture a decision and its rationale for the record. Reader is future self / team / audit — not a decision-maker being convinced. Structure is retrospective: Context → Decision → Consequences. Use this even for non-architectural decisions where you want a durable record. See `references/framework-selection-guide.md`.
>
> **How to use this template.** Fill in BEFORE writing. Submit to `mode: spec-judge`, iterate until PASS.
>
> Decision records have a different shape than briefs/memos — the section headers (Decision, Rationale, Implications, Alternatives) are conventional and exempt from action-title rewriting. The underlying argument still needs evidence-carries (D5) discipline, and the Decision functions as the governing observation (D1).

---

## Frontmatter

```yaml
spec_type: authoring-spec
doc_type: decision-record
intent_summary: |
  [What decision is being recorded, when, by whom, for what context. Reader = future self or team audit.]
supporting_artifacts:
  - path: [path]
    role: [role]
    description: [one line]
load_bearing_codes: []
```

---

## D1 — The decision (governing observation)

One declarative sentence stating the decision.

> [one sentence — e.g., "We will adopt MCP as the primary agent protocol for the DTC store, deprecating the custom JSON-RPC interface by Q3."]

---

## D2 — Rationale axes (MECE)

Why this decision? Typically 3 axes: (1) the situation that forced the decision, (2) the substantive argument, (3) what alternatives were considered and rejected.

1. **Axis 1.** [description]
2. **Axis 2.** [description]
3. **Axis 3.** [description]

---

## D3 — SCQA framing (implicit in ADR sections)

- **Situation (= "Context" section).** [agreed-on ground]
- **Complication (forces the decision).** [tension]
- **Question (= the decision being made).** [explicit]
- **Answer (= the Decision section, restates D1).** [= D1]

---

## D5-structure — Evidence inventory per axis

Per axis ≥2 tagged evidence items pointing to declared artifacts.

---

## D5-readability — Handles for any load-bearing codes referenced

| Code | Handle | Telegraphs? |
|---|---|---|

---

## D7 — Rumelt kernel (MANDATORY for decision records)

- **Diagnosis.** [the obstacle the decision addresses]
- **Guiding policy.** [the approach this decision embodies]
- **Coherent actions.** [implementation moves with owners and time bounds]

---

## Implications (decision-record convention)

What follows from this decision? (Not graded by spec-judge — captured here for the writer's benefit and reviewed against the written record in Pass 1 D5.)

- [implication 1]
- [implication 2]

---

## Alternatives considered

Briefly name alternatives and why they were rejected.

- **Alternative A:** [name + one-line rejection reason]
- **Alternative B:** [name + one-line rejection reason]

---

## Pre-write checklist

- [ ] D1 is a single declarative decision sentence.
- [ ] Rationale axes are MECE.
- [ ] SCQA Answer = D1.
- [ ] Evidence per axis is tagged and traces to artifacts.
- [ ] Kernel is coherent.
- [ ] Implications and alternatives are captured.

---

## What the review pass will then grade

Pass 1 evaluates D1-D7 with action-title test relaxed (ADR headers are exempt). Pass 2 evaluates D1-D5 with the same exemption.
