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
> - `capability_seeds`: [N newly-possible jobs seeded from intersections — first-principles lane]
> - `incumbents`: [N major players with structural constraints named]
>
> ### Framework signals (two lanes)
> **Incumbent-anchored (must be ≤50% of total):**
> - Blue Ocean ERRC: [N signals] ([M Create candidates with Phase 2 evidence])
> - Aggregation Theory: [diagnostic passed/failed; N signals OR non-fit rationale]
> - Decoupling: [N signals citing top-3 pains]
> - Counter-positioning: [N signals per incumbent with structural traps]
>
> **First-principles:**
> - Capability seeds: [N newly-possible jobs → feed Move 8]
> - Thiel's Secrets: [N contrarian secrets, each in grounded form, each emitting a bet]
>
> **Overlay:**
> - 7 Powers (early): [tagged across N signals]
>
> Total signals: [N]; incumbent-anchored share: [M%]; flagged as high strength: [M]
>
> ### Lane allocation (proposed — ratify or override)
> **[incumbent]% incumbent-anchored / [capability]% capability-first.**
> Structure score [S/3] ([reads that fired]); frontier score [F/3] ([reads that fired]). Confidence: [high/low].
> Rationale: [one sentence — e.g. "Non-consumption is broad and a capability inflected in 2025 while incumbents are weak, so I'm proposing 30/70 toward capability-first."]
> Approve this mix, or override (e.g. "make it 50/50" / "lead incumbent"). The ≥1-per-lane floor holds either way. See `references/lane-allocation.md`.
>
> ### Thiel Secrets as bets (no truth-endorsement asked)
> For each secret: grounded form + the venture it generates + its load-bearing hypothesis + the cheapest test (cost / time-to-signal / pass-fail) + prize if true. **You are not asked which secrets are true** — that's unknowable. These flow into Phase 5 as candidate bets you'll choose tests for at Gate 3.
>
> ### Quality flags
> - [N] signals rest on `[A]/[I]`-tagged claims — these will be load-bearing in Phase 6 stress test
> - [N] signals lack entry-power mapping
> - Margin-cost regression risk: [yes/no] on [N] aggregation concepts (Thompson 2024 overlay)
> - Frameworks marked N/A: [list with rationale]
>
> ---
>
> **Why we're asking:** Phase 5 applies the eight structural moves (Moves 1-7 incumbent-anchored + Move 8 capability-first) as templates against these signals. Weak signals produce weak concepts; filter happens here. Once Phase 5 runs, going back is expensive.
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
> ### Ranked shortlist (each is a bet)
> 1. **[handle]** `[concept_id]` — [one-line] — `origin: [capability-first | incumbent-first]`
>    - Verdict: [SHIP / PROCEED / RECONSIDER]
>    - Load-bearing hypothesis: [the one claim that, if false, kills it]
>    - Cheapest test: [experiment — cost / time-to-signal / pass-fail threshold]
>    - Prize if true: [value_if_true]
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
> **Why we're asking:** Phase 6 surfaces the rank; the human owns the choice of which **experiments to fund**. The decision is test-worthiness — prize if true × cost/speed of test × strategic fit — not whether you believe the hypothesis (conviction is the test's output, not its input).
> **Default if unsure:** fund the test for the top-ranked bet(s) marked SHIP; flag iteration items for follow-up.
> **Tradeoff:** funding the top-ranked maximizes analytical defensibility; funding a lower-ranked bet may reflect a cheaper/faster test or better strategic fit. Both are valid.
> **Or:** send specific concepts back for further iteration (re-run a specific stress test, or redesign a `validation_test` that's too slow/expensive) before final approval.
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
