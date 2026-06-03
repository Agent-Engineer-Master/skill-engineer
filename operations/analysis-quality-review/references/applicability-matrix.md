# Applicability Matrix — framework × dimension × doc_type

The skill grades structure against the declared `structural_framework`, and readability against the doc-type conventions. Pass 1 (structure) is **framework-dependent**; Pass 2 (readability) is **framework-independent** (it grades any prose document the same way).

Legend: **M** = mandatory at standard+, **O** = optional / recommended, **H** = high-strictness only, **N/A** = does not apply, **partial** = limited scope (see notes).

## Mode applicability by doc_type

| Mode | brief | deck | memo | decision-record | wiki | daily-note |
|---|---|---|---|---|---|---|
| `spec` (return template) | yes | yes | yes | yes | yes | N/A |
| `spec-judge` (grade storyline) | yes | yes | yes | yes | yes | N/A |
| `review pass: 1` (structure) | yes | yes | yes | yes | yes | low-strictness only |
| `review pass: 2` (readability) | yes | yes | yes | yes | yes | low-strictness only |

**Why spec / spec-judge skip daily-note:** too lightweight to warrant the ghost-deck discipline. A daily scratchpad doesn't need a Rumelt kernel or a MECE supporting-reasons structure. The cost of writing the spec exceeds the cost of writing the document.

`wiki` was previously excluded from spec mode but now uses the `concept-page` framework — its spec is a definitional scaffold (terms, properties, relationships), which is light enough to be useful.

## Pass 1 — Structure dimensions by framework

| Dimension | minto-pyramid | rumelt-kernel | issue-tree | scqa-only | adr | concept-page | descriptive |
|---|---|---|---|---|---|---|---|
| D1 governing observation | M (apex) | M (= guiding policy) | O | M (= Answer) | M (= Decision) | O (= primary concept) | O (= phenomenon thesis) |
| D2 MECE | M (on supporting reasons) | M (on coherent actions; reasons under policy) | M (high bar — issue-tree integrity) | N/A | N/A | O (on properties list) | O (on mechanism categories) |
| D3 SCQA opening | M | O (recommended) | N/A | M | O (Context section partial) | N/A | O (recommended) |
| D4 dot-dash narrative | M | M | M | O | O | O (section flow) | M |
| D5 evidence carries | M | M | M | M | M | M | M (highest priority — descriptive lives or dies on evidence) |
| D6 Frankenstein detection | H | H | H | H | H | H | H |
| D7 Rumelt kernel coherence | N/A | M | N/A | N/A | O (Decision implies diagnosis) | N/A | N/A |
| D8 issue-tree decomposition depth | N/A | N/A | M | N/A | N/A | N/A | N/A |

Notes on nested checks:

- **Inside `rumelt-kernel`**, the guiding-policy section is graded with Minto-style D1+D2+D5 checks (the policy is a governing observation; the supporting reasons under it must be MECE; evidence must carry). D7 is the apex check; the Minto pieces are subordinate. Don't fail rumelt-kernel for missing SCQA opening unless strictness=high.
- **Inside `issue-tree`**, D2 MECE is the dominant check — applies to every horizontal grouping in the tree. D8 (decomposition depth) checks whether each level-2 question can decompose into 2-4 sub-questions (Conn & McLean issue-tree depth test).
- **Inside `descriptive`**, the absence of D1/D7 is deliberate — a state-of-X analysis does not require an apex recommendation. D5 evidence-carries is the hardest check (descriptive documents fail if claims aren't sourced).
- **Inside `concept-page`**, most pyramid-style checks fire only as O — a definitional doc doesn't have a thesis. D5 still fires hard.

## Pass 2 — Readability dimensions by doc_type (framework-independent)

Readability dimensions grade prose quality; they do not depend on the storyline framework. They depend on the doc_type's format conventions.

| Dimension | brief | deck | memo | decision-record | wiki | daily-note |
|---|---|---|---|---|---|---|
| D1 (action titles) | M | M (mandatory) | M | M | no — noun labels OK | no |
| D2 (so-what) | M | M | M | M | O | no |
| D3 (specificity) | M | M | M | M | M | O |
| D4 (jargon discipline) | M | M | M | M | M | O |
| D5 (no internal codes in prose) | M | M | M | M | M | M |
| D6 (Frankenstein, high-only) | H | H | H | H | H | no |
| D7 (one-message discipline, high-only) | H | H | H | H | H | no |

## Doc-type definitions

| doc_type | Definition | Reader | Common framework defaults |
|---|---|---|---|
| `brief` | Long-form analytical document; executive or working brief | Senior reader who decides or recommends based on it | `minto-pyramid` (default), `rumelt-kernel`, `descriptive`, `issue-tree` |
| `deck` | Slide-shaped document — titles do heavy lifting | Sponsor, partner, investor — read in 10–15 minutes | `minto-pyramid` (default), `scqa-only` |
| `memo` | Argumentative memo with a recommendation | Decision-maker peer or one level up | `minto-pyramid` (default), `rumelt-kernel`, `scqa-only` |
| `decision-record` | Captures a decision and its rationale for the record | Future self, team, audit | `adr` (default) |
| `wiki` | Knowledge base concept page | Anyone in the org, asynchronous | `concept-page` (default) |
| `daily-note` | Daily review / scratchpad / capture | Self | N/A (spec mode does not apply) |

## Default-framework inference table

When `structural_framework` is omitted, the orchestrator infers as follows. See `references/framework-selection-guide.md` for the full decision tree.

| doc_type | Default framework | Override if … |
|---|---|---|
| brief | `minto-pyramid` | document is strategy → `rumelt-kernel`; problem-solving → `issue-tree`; diagnostic → `descriptive` |
| deck | `minto-pyramid` | very short / single-message → `scqa-only` |
| memo | `minto-pyramid` | strategy memo → `rumelt-kernel` |
| decision-record | `adr` | — |
| wiki | `concept-page` | — |
| daily-note | (none) | spec mode does not apply |

## Special cases

- **Routine outputs** (morning-brief, SEO-review summaries): default to `doc_type: daily-note` and `strictness: low`. The protocol short-circuits and does not run the full passes — see SKILL.md pre-flight.
- **Mixed docs** (a brief whose sections use different frameworks): pick the dominant framework. The reviewer notes mixed-mode in `## Notes` if it sees structural conflict between sections.
- **Decks-as-markdown** (slides composed in markdown): treat as `doc_type: deck` even though the file extension is `.md`. The action-titles dimension is mandatory.
- **Strategy documents that ALSO include diagnostic sections**: pick `rumelt-kernel` — the diagnosis section is part of the kernel, not a separate framework.
