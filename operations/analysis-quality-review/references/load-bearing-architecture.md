# Load-Bearing Architecture — Why the Calling Skill Is the Natural Fixer

This is the architectural decision that distinguishes `analysis-quality-review` from a generic prose reviewer (e.g., `seo-review-loop`). It is load-bearing — removing it makes the skill dangerous.

## The problem

SEO violations are surface-level: they live in the prose. A reviewer/fixer pair can operate on the article file alone and produce safe edits.

Consulting and analytical briefs are different. The prose carries:

- **Cross-reference codes** — `M1-DTC`, `AUTH-DTC`, `SECRET-02`, `CP-4`. These are pointers to source datasets, framework rows, or stress-test outputs. A "readability fix" that renames them locally breaks the cross-reference chain.
- **Load-bearing evidence tags** — `[V]`, `[C]`, `[A]`, `[I]` (verified / cited / asserted / inferred). These look like clutter. They are not. A fixer that strips them destroys the document's evidence discipline.
- **Framework citations** — `Phase 4.5 7-Powers chain`, `Wardley anchor`. The surrounding section structure was chosen because an upstream framework mapping flows through it. Restructuring breaks the framework.
- **Cited claims with source dependencies** — "1.2× LTV uplift (per Q1 buyer-shortlist run)". The number, the unit, and the citation are a unit. Softening the claim while preserving "the gist" destroys the chain.

A fixer with no upstream context is competent at prose and **dangerous at meaning**.

## The original (rejected) design

The first version of this skill copied the seo-reviewer / seo-content-fixer pattern: a reviewer agent paired with a fixer agent, both orchestrated in a loop by the skill. To make the fixer safe on load-bearing edits, we built an elaborate manifest scaffold — supporting_artifacts declarations, reviewer-enriched preservation_notes, a halt rule that bailed the fixer when preservation guidance was missing, an artifact-loader pre-flight that classified every token.

It worked, but it was awkward. The fixer agent was reinventing context that the calling skill already had in working memory. The halt rule and manifest scaffold existed to give the fixer just enough context to be safe — when the cleanest answer was just to let the calling skill do the fixing.

## The new design — review-only

The calling skill is the natural fixer of an analytical document because it has the substantive context:

- It generated the brief, so it knows the intent behind every passage.
- It holds the supporting artifacts in working memory (or can re-load them cheaply).
- It owns the cross-references — it created them, so it knows where each code resolves.
- It can update both the brief AND any source dataset in the same edit pass, keeping them coherent.

This skill grades. The calling skill fixes. The skill's job is to **hand the calling skill a precise diagnosis it can act on**.

## The shared grounding artifact — load_bearing_index.yaml

Even though only the calling skill applies fixes, the reviewer and the calling skill must agree on what is load-bearing. That agreement is materialized in `load_bearing_index.yaml`, produced by the `artifact-loader` pre-flight pass.

The artifact-loader runs once per audit. It:

1. Validates the `supporting_artifacts` manifest — every declared path exists and is readable.
2. Builds the index — for each declared element class, lists every occurrence in the document with file:line and zone classification (`narrative` / `table` / `code-block` / `reference-list` / `frontmatter`).
3. Saves the index to the audit working directory.

Both the reviewer (when grading) and the calling skill (when applying fixes) read this index. They never disagree on which tokens are load-bearing because they share the same source of truth.

## What the reviewer produces (preserved from the original design)

For each violation touching a load-bearing element, the reviewer embeds two extra fields:

- `preservation_note` — what the element references, why it matters, and how to safely edit
- `suggested_fix_shape` — the shape of an acceptable fix (e.g., "introduce a plain-English handle on first mention, then use it throughout; update dataset comments to match")

The calling skill reads these alongside the canonical fix patterns in `fix-patterns.md` and applies the smallest edit that satisfies the dimension while preserving meaning.

## Strictness gating

Reading supporting artifacts is expensive (extra tokens, extra time). The `strictness` parameter gates depth:

| Strictness | Artifact reads | Preservation notes | Use case |
|---|---|---|---|
| `low` | None — prose only | None | Slack-shaped replies, daily notes, scratchpads |
| `standard` | 1–2 declared `source-of-truth` artifacts | Only on cross-reference violations | Internal briefs, working memos |
| `high` | All declared supporting artifacts | On every flagged element touching `load_bearing_elements` | Executive briefs, gate reports, venture shortlists, anything going to a senior reader |

The reviewer agent reads `strictness` and applies the matrix. The orchestrator passes `strictness` through; it does not enforce the matrix itself.

## The bail rule (caller-side, replaces the old halt rule)

If a violation touches a load-bearing element and **lacks a preservation_note**, the calling skill must **defer the fix and report it in the next invocation's `previous_violations` payload** — it must NOT guess.

This rule exists because:
- The most common failure mode of a competent prose fixer is to "infer reasonable intent" — exactly the behavior that renames `SECRET-02` to "the AI-wins finding" and breaks the cross-reference.
- A missing preservation_note signals the reviewer ran at lower strictness than this violation requires, or the canonical definition is genuinely missing from declared artifacts.
- Deferring is cheap. Guessing destroys meaning.

The reviewer handles the defer on the next pass by either re-issuing with a richer preservation_note (if higher strictness would help) or accepting the defer and excluding it from the FAIL count so the calling skill can escalate to a human author.

See `fix-patterns.md` for the full bail rule and `worked-examples.md` for an end-to-end example.

## What this design rejects

- **A fixer agent that reads upstream artifacts ad hoc, without the calling skill's context.** Token-expensive on every fix attempt; produces inconsistent decisions across passes; reinvents context the calling skill already has.
- **A reviewer that only flags violations without preservation context.** Pushes the safety decision to the caller without giving it enough information.
- **A single strictness level.** Daily-note review and executive-brief review have different cost/safety budgets; one setting cannot serve both.
- **Allowing the calling skill to "infer" cross-reference safety.** Inference is exactly the failure mode this skill exists to prevent.

## What this design accepts as cost

- The calling skill is responsible for reading `fix-patterns.md` and applying patterns correctly. Acceptable — the calling skill already operates with full context; reading a canonical patterns file is cheap.
- The reviewer + caller loop requires multiple invocations (review → fix → re-review). Acceptable — single-invocation flows existed before and produced lower-safety outputs.
- The calling contract is more demanding than a generic prose-review skill. Acceptable — callers that produce load-bearing analytical documents already track this metadata.

## Cross-reference

Fix patterns and editorial expertise live in `references/fix-patterns.md`. That file is the canonical home of the rules that used to live inside the deleted `argument-structure-fixer` and `readability-fixer` agents. The calling skill reads it; the review skill does not apply it.
