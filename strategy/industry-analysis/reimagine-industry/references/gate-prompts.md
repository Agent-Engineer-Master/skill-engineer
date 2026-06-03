# Gate Prompts

Templates for the three approval gates. Use the **Why we're asking / Default if unsure / Tradeoff / Or** four-line pattern (inherited from `analyze-industry`).

**Format requirement:** all gates render the review content as HTML via the html-output skill (see `gate-html-output.md`). The chat surfaces only (a) the saved file path, (b) a one-paragraph framing, (c) the four-line decision prompt. Do not paste the full review into chat — open the HTML for the visual layout.

---

## Gate 1 — Scope + Data Sources

Fires after Phase 0 init, before Phase 1.

**Present to the user:**

> ## Gate 1: Scope & Data Sources
>
> Before running the 6-phase reimagination workflow, please confirm scope and data plan.
>
> ### Industry definition
> [Industry slug] — [proposed definition with what's in scope and what's not]
>
> ### Inherited inputs detected at `08-knowledge/world-model/industries/[slug]/`
> - `industry-brief.yaml` — [present/absent]
> - `working/value-chain-profit-pools.md` — [present/absent] — used in Phase 1
> - `working/demand.md` — [present/absent] — used in Phase 2
> - `working/trajectory.md` — [present/absent] — used in Phase 3
> - `working/moat-sources.md` — [present/absent] — informs Phase 4.5
> - `working/five-forces.md` — [present/absent] — informs Phase 4.4 counter-positioning
>
> ### Primary data you've indicated
> - [What you said you have — interviews, ops experience, surveys, etc.]
>
> ### Planned librarian dispatches
> - Phase 2 — value chain pain audit across [entity types] (skip if `working/demand.md` exists and is comprehensive)
> - Phase 3 — 5-axis enabling conditions scan (skip if `working/trajectory.md` exists and is recent)
> - Phase 6 — idea maze research per concept (always runs)
>
> ---
>
> **Why we're asking:** wrong scope produces analytically excellent but operationally useless concepts. Missing primary data causes Phase 2 to over-rely on `[A]/[I]`-tagged pain points, which collapse in Phase 6 bar test. Better to dispatch the librarian now than discover the gap later.
> **Default if unsure:** approve as proposed; the librarian dispatches are scoped to fill gaps, not redo existing analysis.
> **Tradeoff:** more librarian dispatches = more wall-clock time but stronger Phase 6 stress tests. Skipping librarian on a missing input = faster but Phase 6 bar test failures more likely.
> **Or:** provide a different scope, point to additional inherited inputs, or specify primary data the skill should use.
>
> Approve? (yes / modify / reject)

After approval: `python scripts/log_run.py --slug <slug> --event gate-1-approved`.

---

## Gate 2 — Dataset + Framework Signals

Fires after Phase 4 completes, before Phase 5.

**Present to the user:**

> ## Gate 2: Dataset + Framework Signals Review
>
> Phases 1-4 complete. Before generating venture concepts, please review the dataset and framework signals.
>
> ### Dataset population summary
> - `industry`: populated [V/C tag rate: N%]
> - `value_chain`: [N nodes, M flows]
> - `market_structure`: [N information asymmetries identified]
> - `value_chain_pain`: [N segments × M pain points across K entity types]
> - `enabling_conditions`: [N conditions across 5 axes, M intersections]
> - `incumbents`: [N major players with structural constraints named]
>
> ### Framework signals
> - Blue Ocean ERRC: [N signals] ([M Create candidates with Phase 2 evidence])
> - Aggregation Theory: [diagnostic passed/failed; N signals OR non-fit rationale]
> - Decoupling: [N signals citing top-3 pains]
> - Counter-positioning: [N signals per incumbent with structural traps]
> - 7 Powers (early): [tagged across N signals]
> - Thiel's Secret: [N human-endorsed contrarian theses]
>
> Total signals: [N]; flagged as high strength: [M]
>
> ### Quality flags
> - [N] signals rest on `[A]/[I]`-tagged claims — these will be load-bearing in Phase 6 stress test
> - [N] signals lack entry-power mapping
> - Margin-cost regression risk: [yes/no] on [N] aggregation concepts (Thompson 2024 overlay)
> - Frameworks marked N/A: [list with rationale]
>
> ---
>
> **Why we're asking:** Phase 5 applies the Seven Structural Moves as templates against these signals. Weak signals produce weak concepts; filter happens here. Once Phase 5 runs, going back is expensive.
> **Default if unsure:** approve and proceed; revisit specific signals at Gate 3 if Phase 6 surfaces problems.
> **Tradeoff:** aggressive filtering now = fewer concepts in Phase 5 shortlist; permissive = more candidates to stress-test in Phase 6.
> **Or:** send specific signals back for rework (re-run a framework against new data, or dispatch librarian for additional evidence on a load-bearing claim).
>
> Approve / rework specific signals / reject.

After approval: `python scripts/log_run.py --slug <slug> --event gate-2-approved`.

---

## Gate 3 — Final Shortlist

Fires after Phase 6 stress test + bar test, before final write.

**Present to the user:**

> ## Gate 3: Final Shortlist Review
>
> Phases 1-6 complete. Bar test verdict: [PASS / verdict reasoning].
>
> ### Ranked shortlist
> 1. **[concept_id]** — [one-line]
>    - Verdict: [SHIP / PROCEED / RECONSIDER]
>    - Non-obvious because: [specific reason from bar test]
>    - Top risk: [specific failure mode surfaced in Phase 6]
>    - Required iteration before ship: [list, or "none"]
> 2. ...
>
> ### Concepts considered and rejected
> - [concept_id] — killed at [stress test] — rationale: [specific]
> - [concept_id] — killed at [stress test] — rationale: [specific]
>
> ### Concepts requiring iteration before ship
> - [concept_id] — needs: [specific iteration before SHIP verdict]
>
> ### Outputs to be written on approval
> - `venture-concepts.md` — final ranked shortlist
> - `reimagination-brief.md` — narrative synthesis
> - `disruption-dataset.yaml` — `final_status` per concept set
> - `signals-log.md` — append rejected concepts with rationale (durable for future runs)
> - `bar-test.md` — sub-agent verdict + reasoning
>
> ---
>
> **Why we're asking:** Phase 6 surfaces the rank; the human owns the choice of what to actually pursue. The AI cannot fully measure conviction or strategic fit.
> **Default if unsure:** approve top-ranked concept(s) marked SHIP; flag iteration items for follow-up.
> **Tradeoff:** pursuing top-ranked maximizes analytical defensibility; pursuing a lower-ranked concept may reflect conviction the AI can't measure. Both are valid.
> **Or:** send specific concepts back for further iteration (re-run a specific stress test with more research) before final approval.
>
> Approve / iterate / reject.

After approval: write all outputs, then `python scripts/log_run.py --slug <slug> --event gate-3-approved`.

---

## Chat surface vs HTML payload

The templates above describe what the HTML gate review must include. The **chat surface** at each gate is much smaller:

```
## Gate [N] — [name]

I've rendered the gate review. Open here:
  → 08-knowledge/world-model/industries/[slug]/gates/gate-[N]-[date].html

Quick framing: [one paragraph summarizing what changed since the last gate
and what decision this gate is asking for. Reference memorable concept
handles, not concept_ids.]

[Four-line decision prompt: Why we're asking / Default / Tradeoff / Or]

Approve / iterate / reject.
```

The HTML carries the full review (diagrams, signal cards, scorecards, plain-English explainers). Chat carries only the decision prompt and links. This keeps the human surface clean and forces the visual layout where it belongs.

If the user prefers a markdown summary in chat alongside the HTML (e.g., for quick mobile review), generate a 5-bullet TL;DR — but the HTML is still authoritative and the decision is made against it.
