# Framework Selection Guide

Picking the right `structural_framework` is the most important decision the calling skill makes before invoking `mode: spec`. The framework determines the storyline scaffold the document will use and which Pass 1 dimensions the reviewer will grade against. Wrong framework choice produces over-applied or under-applied grading.

This guide explains when to use each framework. Use it (a) to override the default when the default doesn't match your document's intent, or (b) to set the default for a new doc_type.

## The seven frameworks at a glance

| Framework | When to use | Apex question the document answers |
|---|---|---|
| `minto-pyramid` | The document recommends an action or position to a senior reader | "What should we do / believe?" |
| `rumelt-kernel` | The document is a strategy — names what to do, why, against what diagnosis | "What's our strategy?" |
| `issue-tree` | The document works through a complex problem by decomposing it MECE | "What's the answer to this problem?" |
| `scqa-only` | The document is short — a one-pager or message | "Here's the situation and what I think we should do" |
| `adr` | The document records a decision for future reference | "We decided X. Here's why." |
| `concept-page` | The document defines and explains a concept (no recommendation) | "What is X?" |
| `descriptive` | The document describes the state of something without recommending action | "What's true about X right now?" |

If you can't decide between two, the document probably needs to be split or its purpose clarified before writing.

## Detailed selection criteria

### Use `minto-pyramid` when:

- The document recommends an action, decision, position, or set of priorities to a senior reader
- The recommendation is supported by 3-5 reasons that can be made MECE
- A senior reader would want the recommendation in the first sentence
- Examples: "We should enter market X," "Brand Y is best positioned to acquire Z," "These three concepts should ship this quarter"

This is the default for `brief`, `deck`, and `memo` doc_types because most analytical work that gets to a senior reader takes a position.

### Use `rumelt-kernel` when:

- The document is explicitly a strategy — what to do over what time horizon, anchored in a diagnosis of the situation
- The recommendation requires explaining *why* this approach is the right one against *this specific situation*
- A reader who only saw "what we'll do" without "what we're up against" would miss the strategy
- Examples: "Our 3-year category strategy," "How we'll respond to the new competitor," "Why we're pivoting"

Rumelt teaches that strategy = Diagnosis + Guiding Policy + Coherent Actions. If your document doesn't have all three, it's not strategy — pick a different framework. Rumelt's most useful contribution to the rubric: catching goal-masquerading-as-strategy (D7 FAIL).

### Use `issue-tree` when:

- The document works through a problem by decomposing the root question into MECE sub-questions
- The structure is fundamentally hypothesis-testing — each branch tests a claim that resolves up
- Examples: "Why is our profit declining?" "Where should we cut costs?" "What's driving customer churn?"

This is the McKinsey 7-step problem-solving structure (Conn & McLean). It's distinct from Minto: Minto starts with the answer; issue-tree starts with the question and decomposes. Use issue-tree when the analytical work is the point and the answer is what falls out at the end.

### Use `scqa-only` when:

- The document is short — typically under 500 words or one page
- Full Minto pyramid would be overkill — there isn't space for MECE supporting reasons + evidence
- The Answer is enough; readers don't need the full deductive scaffold
- Examples: an email recommending an action, a one-page brief for a busy reader, a status update with a takeaway

### Use `adr` when:

- The document captures a decision that already exists, for future reference
- The reader is a future self, the team, or an audit — not a decision-maker who needs convincing
- The structure is retrospective: here's the context, here's what we decided, here are the consequences
- Examples: architecture decision records, governance decisions, capital allocation records

ADR is intentionally different from minto-pyramid because the rhetorical purpose is different. Minto persuades; ADR records.

### Use `concept-page` when:

- The document defines and explains something — a concept, a term, a framework, a system
- There's no recommendation, no diagnosis, no decision being made
- The reader is consulting it for reference, not being walked through an argument
- Examples: wiki concept pages, glossary entries, framework explanations

### Use `descriptive` when:

- The document describes the state of something (an industry, a market, a system, a problem) without recommending action
- The reader needs to understand what's true; downstream readers will use this as input to their own decisions
- Examples: industry state-of-the-market reports, post-mortems that don't recommend changes, diagnostic analyses that hand off to a separate recommendation document

Descriptive documents live or die on evidence (D5). They explicitly do NOT require an apex governing observation, a Rumelt kernel, or a recommendation.

## Decision tree

```
Is the document mainly a recommendation / position?
├─ Yes
│   ├─ Is it a strategy (diagnosis + guiding policy + actions)?
│   │   ├─ Yes → rumelt-kernel
│   │   └─ No → 
│   │       ├─ Is it short (≤ 1 page)? → scqa-only
│   │       └─ Long-form analytical brief → minto-pyramid
│   └─ Is the document working through a complex problem by decomposing it?
│       └─ Yes → issue-tree
└─ No (no recommendation)
    ├─ Is it a record of a decision already made?
    │   └─ Yes → adr
    ├─ Is it defining or explaining a concept?
    │   └─ Yes → concept-page
    └─ Is it describing the state of something?
        └─ Yes → descriptive
```

## How the default-by-doc_type inference works

When the caller omits `structural_framework`, the orchestrator picks based on `doc_type`:

| doc_type | Default framework | Reasoning |
|---|---|---|
| `brief` | `minto-pyramid` | Most briefs that get to a senior reader take a position |
| `deck` | `minto-pyramid` | Decks for sponsors / partners are typically recommendation-driven |
| `memo` | `minto-pyramid` | Memos to peers / one-up are typically argumentative |
| `decision-record` | `adr` | The doc_type literally names the structure |
| `wiki` | `concept-page` | Wiki pages are definitional by convention |
| `daily-note` | (spec mode does not apply) | Too lightweight for ghost-deck discipline |

These defaults are tuned for the typical case. The caller should override when the document's intent doesn't match — e.g., a `doc_type: brief` that is a diagnostic industry report (no recommendation) should be tagged `structural_framework: descriptive`, even though the default would be `minto-pyramid`.

## Common selection mistakes

- **Picking `rumelt-kernel` for a brief that recommends an action but isn't a strategy.** A recommendation isn't automatically a strategy. If you have a recommendation but no diagnosis-policy-actions structure, pick `minto-pyramid` instead. Rumelt is specifically for documents whose central object IS a strategy.

- **Picking `descriptive` to dodge the rigor of a recommendation framework.** If your document has an implicit recommendation buried in the conclusion, picking `descriptive` to skip the apex governing-observation check is a bad-faith framework choice. Make the recommendation explicit and pick the right framework, or genuinely commit to descriptive (no recommendation at all).

- **Picking `issue-tree` for a document that has the answer already.** Issue-tree is for working through a problem. If you already know the answer and you're presenting it, pick `minto-pyramid` or `rumelt-kernel`. Issue-tree is the wrong rhetorical scaffold for a brief that says "here's what we found."

- **Picking `minto-pyramid` for a strategy document.** Strategy documents typically fail D7 (Rumelt kernel) if graded under minto-pyramid because the kernel check doesn't fire. Conversely, a strategy graded under rumelt-kernel that has a goal masquerading as a strategy will be caught. Don't downgrade the rubric by picking the wrong framework.

- **Treating frameworks as composable.** Pick ONE primary framework. Minto-style checks fire NESTED inside rumelt-kernel and issue-tree where they apply — the rubric handles this. You don't pick `minto-pyramid + rumelt-kernel`.
