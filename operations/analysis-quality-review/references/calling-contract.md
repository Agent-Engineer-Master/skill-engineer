# Calling Contract — analysis-quality-review

This is the formal contract for upstream skills invoking `analysis-quality-review`. The skill is a **review-only multi-mode** protocol with three modes: `spec` (returns an authoring template), `spec-judge` (grades a filled-in storyline), and `review` (grades the realized document in two gating passes). In all model-grading modes, the skill returns a structured violation report plus a pointer to `fix-patterns.md`. The CALLER writes the spec, applies fixes, and decides whether to iterate. The recommended end-to-end flow is at the bottom of this file.

## Required inputs (depends on mode)

| Field | Required for mode | Values | Default | Notes |
|---|---|---|---|---|
| `mode` | all | `spec \| spec-judge \| review` | `review` | Selects the orchestration branch |
| `doc_type` | all | `brief \| deck \| memo \| decision-record \| wiki \| daily-note` | — | Determines format conventions (action titles required? readability checks?) and the soft default for `structural_framework` |
| `structural_framework` | `spec`, `spec-judge`, `review pass: 1` | `minto-pyramid \| rumelt-kernel \| issue-tree \| scqa-only \| adr \| concept-page \| descriptive` | inferred from `doc_type` per `references/framework-selection-guide.md` | Determines which Pass 1 dimensions fire and which authoring template `mode: spec` returns. The caller should override the default when the document's intent doesn't match the default (e.g., a `doc_type: brief` that is descriptive-not-recommendation should be tagged `structural_framework: descriptive`) |
| `document_path` | `review` | repo-relative or absolute path | — | Must be markdown or plain text |
| `spec_path` | `spec-judge` | path to the filled-in authoring spec | — | Must follow the template structure for the doc_type |
| `template_path` | `spec-judge` | path to the template the spec was filled from | — | Echo from the prior `mode: spec` call |
| `pass` | `review` | `1` (structure) \| `2` (readability) | — | Single pass per invocation |
| `strictness` | all | `low \| standard \| high` | `standard` | Gates artifact-reading depth and manifest requirements — see below |
| `caller_skill` | no | name of upstream skill | — | For audit trail |
| `audit_dir` | no | path | — | Set on re-invocations to reuse snapshot and load_bearing_index |
| `previous_violations` | no | path to prior report | — | Set on re-invocations after applying fixes |
| `iteration` | `spec-judge` | integer ≥ 1, cap 3 | 1 | The `max_spec_iterations` cap blocks runaway loops |

## Required for analytical documents — supporting_artifacts manifest

For `doc_type` in `{brief, memo, decision-record, deck}` at `strictness ≥ standard`, the caller MUST pass:

```yaml
supporting_artifacts:
  - path: "path/to/disruption-dataset.yaml"
    role: "source-of-truth"           # do not contradict — claims must match
    description: "Dataset of disruption signals; cited via SECRET-XX codes"
  - path: "path/to/working/"
    role: "evidence"                  # concepts must trace back here
    description: "Working notes from Phase 4 venture exploration"
  - path: "path/to/7-powers-mapping.md"
    role: "framework-reference"       # framework anchor — restructuring must match
    description: "7-Powers chain for Phase 4.5"

load_bearing_elements:
  - class: "concept_ids"
    pattern: "[A-Z][A-Z0-9]*-[A-Z0-9]+"   # e.g., M1-DTC, SECRET-02, AUTH-DTC — first segment may contain digits after the leading letter
    rule: "cross-references — preserve as-is OR update everywhere together; never local edit"
  - class: "evidence_tags"
    pattern: "\\[(V|C|A|I)\\]"          # verified/cited/asserted/inferred
    rule: "load-bearing on adjacent numeric claims; never strip"
  - class: "phase_citations"
    pattern: "Phase [0-9]+(\\.[0-9]+)?"
    rule: "cross-reference to upstream framework; preserve label and position"
  - class: "numeric_claims_with_citations"
    pattern: "[0-9]+(\\.[0-9]+)?[x×%]?.*\\((per|source:|via).*\\)"
    rule: "number, unit, and citation are a unit — edit all three together or none"

intent_summary: |
  One paragraph from the calling skill about what the document is trying to achieve
  and who the reader is. The reviewer uses this to calibrate severity — a venture
  shortlist for a partner has different tolerances than a working memo.
```

At `strictness: low` the manifest is optional. At `strictness: high` the protocol BLOCKS if the manifest is missing or empty.

## Return contract (mode-dependent)

`mode: spec` returns a **single line** — the path to the framework-matched authoring template. No model call, no audit dir:

```
TEMPLATE_PATH: .claude/skills/analysis-quality-review/references/authoring-templates/<structural_framework>.md
```

The orchestrator picks the template based on the declared `structural_framework`. If `structural_framework` is omitted, the orchestrator infers it from `doc_type` per `references/framework-selection-guide.md`. If called with `doc_type: daily-note` the response is `TEMPLATE_PATH: BLOCKED` with rationale "spec mode does not apply to this doc_type — too lightweight for ghost-deck discipline."

`mode: spec-judge` and `mode: review` return the **same five-line block** via the orchestrating session's final message — a pass identifier plus four return values (verdict, violation report path, fix patterns path, audit directory):

```
PASS: spec-judge | 1 | 2
VERDICT: PASS | FAIL | BLOCKED | ESCALATE
VIOLATION_REPORT_PATH: <path>
FIX_PATTERNS_PATH: .claude/skills/analysis-quality-review/references/fix-patterns.md
AUDIT_DIR: <path>
```

For `spec-judge`, the `PASS` field reads `spec-judge` rather than `1` or `2` — it identifies which mode was just graded. The `VERDICT: ESCALATE` value is reserved for `spec-judge` exceeding `max_spec_iterations: 3` without converging — caller should consult a human.

The caller parses these. The audit directory contains all per-iteration reports and the load_bearing index for traceability.

## Strictness gating — what changes at each level

| Strictness | Pass 1 dimensions | Pass 2 dimensions | Artifact reads | Preservation notes |
|---|---|---|---|---|
| `low` | D1, D7 | D1 (action titles), D5 (no internal codes) | None | None |
| `standard` | D1–D5 | D1–D5 | 1–2 declared `source-of-truth` artifacts | Only on cross-reference violations |
| `high` | D1–D7 | D1–D7 | All declared artifacts | On every flagged load_bearing element |

Strictness governs review depth (how many dimensions fire and how deeply the reviewer reads artifacts to produce preservation_notes). It does NOT govern fix depth — the calling skill decides how much to fix per iteration.

## Pre-flight responsibilities (orchestrator)

1. Verify `document_path` exists and is text.
2. Verify all required agent files exist at `.claude/skills/analysis-quality-review/agents/` (`artifact-loader.md`, `argument-structure-reviewer.md`, `readability-reviewer.md`).
3. If `strictness ≥ standard` and `doc_type ∈ {brief, memo, decision-record, deck}`: validate manifest is present.
4. If `audit_dir` not supplied: create `tasks/analysis-quality-review/<doc-slug>-<YYYYMMDD-HHMM>/`, snapshot the document to `00-original.md`, and invoke `artifact-loader` once to build `<audit_dir>/load_bearing_index.yaml`.
5. If `audit_dir` IS supplied (re-invocation): verify it exists and contains the snapshot + index; skip rebuild.

## Caller responsibilities — the apply-fixes-yourself pattern

The calling skill is the natural fixer of an analytical document because it has the substantive context: it generated the brief, holds the supporting artifacts in working memory, owns the cross-references, and can coherently update both the brief and any source dataset that needs to move with it.

The caller's loop:

1. **Invoke this skill** with `pass: 1` and the manifest.
2. **Receive the five-line block.** If `VERDICT: PASS`, move to Pass 2. If `VERDICT: FAIL`, continue.
3. **Read the violation report** at `VIOLATION_REPORT_PATH`. For each violation: read `dimension`, `evidence`, `preservation_note`, `suggested_fix_shape`.
4. **Read `fix-patterns.md`** for the canonical fix pattern for that dimension.
5. **Apply targeted `Edit` calls** to the document. If the violation touches a load-bearing element and `preservation_note` references a supporting artifact, update the artifact in the same edit pass — the caller has the artifact in context.
6. **If a fix is unsafe** (preservation_note missing, named specific not in your context, load-bearing token whose meaning you don't know): leave the violation unfixed and record it as `disposition: deferred` in the next invocation's `previous_violations`.
7. **Re-invoke this skill** with the same `audit_dir`, the updated document, and `previous_violations: <path>` set to the previous report. The reviewer grades whether each fix landed.
8. **Loop until `VERDICT: PASS`** for Pass 1, then invoke Pass 2 against the same `audit_dir` and repeat the loop.

The caller bails (escalates to a human author) when:
- The same violation re-issues across 3+ iterations — the fix pattern isn't landing.
- A DEFERRED violation cannot be resolved even at `strictness: high` — the canonical definition is genuinely missing.
- The caller's own context lacks the information needed to fix a load-bearing token safely.

## What the caller does NOT do

- Does not select which dimensions fire (rubric does that based on `doc_type` + `strictness`).
- Does not pre-validate the document (reviewer does that).
- Does not directly invoke reviewer agents — only via the orchestrator.

## What the caller MUST do

- Pass the manifest at `standard` and `high` strictness for analytical document types.
- Honor BLOCKED verdicts — do not fall back to "ship anyway".
- Surface the audit directory path to the user on completion (for traceability).
- Apply fixes from `fix-patterns.md` using the canonical patterns; do not invent alternative fix shapes for load-bearing violations.
- Update supporting artifacts in the same edit pass when a prose-level fix has knock-on effects (e.g., renaming a code, splitting a section that other docs link into).

## Recommended end-to-end caller flow (standard+ strictness)

The full sequence, with each stage's mode + what the caller does between invocations:

```
Stage 0 — Pick structural framework
  Default by doc_type per framework-selection-guide.md, OR override:
    brief / memo / deck → minto-pyramid (default; recommendation-driven)
                       → rumelt-kernel (override; strategy document)
                       → descriptive    (override; diagnostic / state-of-X)
                       → issue-tree     (override; problem-solving)
    decision-record    → adr (default)
    wiki               → concept-page (default)

Stage 1 — Get template
  caller → mode: spec, doc_type: brief, structural_framework: minto-pyramid
  ← TEMPLATE_PATH: .../authoring-templates/minto-pyramid.md

Stage 2 — Fill template + judge storyline
  caller fills the template using its subject context, writes filled-in spec
  caller → mode: spec-judge, spec_path, template_path, manifest, iteration: 1
  ← VERDICT: FAIL with violations (D1 muddled, D2 axes overlap, D7 goal-not-strategy)
  caller revises spec (it has the context to refine the governing observation,
    drop or merge overlapping axes, sharpen the diagnosis)
  caller → mode: spec-judge, ..., iteration: 2, previous_violations
  ← VERDICT: PASS

Stage 3 — Write
  caller generates the document using the approved spec as scaffolding.
  No invocation of this skill during writing.

Stage 4 — Structure review
  caller → mode: review, pass: 1, manifest
  ← VERDICT: FAIL or PASS; loop with fixes until PASS

Stage 5 — Readability review (gated on Pass 1 PASS)
  caller → mode: review, pass: 2
  ← VERDICT: FAIL or PASS; loop with fixes until PASS
```

**Why this saves iteration tokens.** Most structural failures — broken governing observation, MECE-overlap, Rumelt goal-not-strategy, weak evidence inventory — are caught at the 2-3K-token spec stage rather than at the 50-100K-token document stage. Post-hoc fixes to structural problems mean rewriting large sections of the document; pre-hoc fixes mean revising 2-3 lines of the spec. Empirically, the spec-judge loop eliminates roughly 60-70% of the iteration cost that would otherwise land in `review pass: 1`.

**At `strictness: low`** the spec stages are optional (the caller can skip directly to writing and reviewing). At `strictness: standard` they are recommended. At `strictness: high` the caller should treat the spec stages as default discipline and only skip them with explicit rationale.

## Worked example — caller invocation (reimagine-industry)

```text
# Upstream skill: reimagine-industry has just produced the executive brief.
# It needs Pass 1 review before handing off to the partner.

# --- First invocation: Pass 1 ---
Task(subagent_type="claude-orchestrator", prompt=f"""
Read .claude/skills/analysis-quality-review/SKILL.md and run with:

document_path: tasks/reimagine-industry/industrial-robotics-na/executive-brief.md
doc_type: brief
pass: 1
strictness: high
caller_skill: reimagine-industry

supporting_artifacts:
  - path: 08-knowledge/world-model/entities/industrial-robotics-na.md
    role: source-of-truth
    description: Entity card with verified claims and citations
  - path: tasks/reimagine-industry/industrial-robotics-na/working/disruption-dataset.yaml
    role: source-of-truth
    description: Dataset of disruption signals cited via SECRET-XX codes
  - path: tasks/reimagine-industry/industrial-robotics-na/working/7-powers-mapping.md
    role: framework-reference
    description: 7-Powers chain for Phase 4.5

load_bearing_elements:
  - class: concept_ids
    pattern: "[A-Z][A-Z0-9]*-[A-Z0-9]+"
    rule: "cross-references — preserve as-is OR update everywhere"
  - class: phase_citations
    pattern: "Phase [0-9]+(\\\\.[0-9]+)?"
    rule: "cross-reference to framework"

intent_summary: |
  Executive brief for the industrial-robotics-NA deep run. Reader is the
  managing partner — used to decide whether to greenlight Phase 5 venture.
  Findings must remain traceable to the dataset.
""")

# Response:
#   PASS: 1
#   VERDICT: FAIL
#   VIOLATION_REPORT_PATH: tasks/analysis-quality-review/industrial-robotics-na-20260519/p1-iter1-report.md
#   FIX_PATTERNS_PATH: .claude/skills/analysis-quality-review/references/fix-patterns.md
#   AUDIT_DIR: tasks/analysis-quality-review/industrial-robotics-na-20260519/

# --- reimagine-industry now applies fixes itself ---
# Reads the report. Sees 4 violations:
#   V-01: D1 — two competing thesis statements
#   V-02: D4 — noun-label section titles
#   V-03: D5 — SECRET-02 in narrative prose (load-bearing; preservation_note present)
#   V-04: D7 — Rumelt diagnosis missing
#
# Reads fix-patterns.md. Applies:
#   V-01: Edit at top of doc to promote dominant thesis, demote secondary to sub-section
#   V-02: Edit each section title to a complete-sentence claim derived from section lead
#   V-03: Edit to introduce "the retailer-AI dominance signal (`SECRET-02`)" on first mention.
#         Then verifies SECRET-02 in disruption-dataset.yaml still uses the same canonical
#         definition (it does, no artifact edit needed).
#   V-04: Edit to add a 2-sentence diagnosis block before guiding policy.

# --- Second invocation: Pass 1 re-grade ---
Task(subagent_type="claude-orchestrator", prompt=f"""
Read .claude/skills/analysis-quality-review/SKILL.md and run with:

document_path: tasks/reimagine-industry/industrial-robotics-na/executive-brief.md
doc_type: brief
pass: 1
strictness: high
audit_dir: tasks/analysis-quality-review/industrial-robotics-na-20260519/
previous_violations: tasks/analysis-quality-review/industrial-robotics-na-20260519/p1-iter1-report.md
caller_skill: reimagine-industry

# manifest fields unchanged from first invocation
""")

# Response:
#   PASS: 1
#   VERDICT: PASS
#   VIOLATION_REPORT_PATH: tasks/analysis-quality-review/industrial-robotics-na-20260519/p1-iter2-report.md
#   FIX_PATTERNS_PATH: .claude/skills/analysis-quality-review/references/fix-patterns.md
#   AUDIT_DIR: tasks/analysis-quality-review/industrial-robotics-na-20260519/

# --- reimagine-industry now invokes Pass 2 against the same audit_dir ---
# Same loop pattern. Caller applies readability fixes from fix-patterns.md.
```
