# Gate Prompts

Templates for the three approval gates plus the ambidexterity checkpoint. Use the **Why we're asking / Default if unsure / Tradeoff / Or** four-line pattern. The user may be a founder, operator, investor, strategist, or analyst — the prompts address "you", not a specific role.

---

## Gate 1 — Scope + Market Definition

**Present to the user:**

> ## Gate 1: Scope & Market Definition
>
> I've drafted 3 candidate market framings for your industry question. Before the environment diagnosis and sub-skills run, please confirm the scope.
>
> ### Market framing options
>
> | Framing | Definition | Implication |
> |---------|-----------|-------------|
> | Broad | [industry, global, all customer segments] | Wide context, lower analytical depth per segment |
> | Sharpened | [sub-sector, geography, primary customer segment] | Recommended for most attractiveness questions |
> | Surgical | [sub-segment × geography × size-band × customer-segment] | Use when the question is investment-specific |
>
> **Four-test result for sharpened framing:** [pass/fail per: specificity, measurability, supply-side coherence, customer coherence]
>
> ### Proposed sub-skill battery for [Quick/Deep] mode
> - [list of sub-skills to run, with parallel/sequential annotations]
>
> ---
>
> **Why we're asking:** wrong framing produces analytically excellent but operationally useless output. The strategic environment diagnosis (step 3) is run against the confirmed scope — so scope must be locked first.
> **Default if unsure:** Sharpened framing + the proposed sub-skill battery.
> **Tradeoff:** Broader framing = more context but less actionable; surgical = more actionable but may miss adjacent threats.
> **Or:** provide a custom framing.
>
> Approve? (yes / modify / reject)

After approval: `python scripts/log_run.py --event gate-1-approved --slug <slug>`.

---

## Ambidexterity Checkpoint (post-environment-diagnosis, pre-sub-skill-battery)

Fires ONLY if the `assess-strategic-environment` sub-skill declares ambidexterity (industry genuinely spans two environments at different layers / geographies / customer segments). If single-environment, skip this checkpoint and proceed directly to sub-skill battery.

**Present to the user:**

> ## Ambidexterity Detected
>
> The strategic environment diagnosis found this industry spans **two distinct environments**:
> - [Layer/Geo/Segment A]: [Environment 1] — [one-sentence evidence]
> - [Layer/Geo/Segment B]: [Environment 2] — [one-sentence evidence]
>
> Each environment routes downstream sub-skills differently. Three ways to proceed:
>
> | Option | What happens | When to choose |
> |--------|-------------|----------------|
> | A. Single-focus | Pick one layer/segment; sub-skills run once with that environment's routing | Your strategic question is genuinely about one side |
> | B. Dual analysis | Sub-skills run twice (once per environment); brief produces two parallel WTP/HTW threads | You need to compare the two; doubles cost and run time |
> | C. Re-scope | Return to Gate 1 with tighter framing that targets one layer/segment | The scope was broader than you intended |
>
> ---
>
> **Why we're asking:** running one environment's toolkit on the other half produces wrong recommendations. The orchestrator does not auto-choose because the right answer depends on your actual decision question.
> **Default if unsure:** Option C (re-scope). Tighter scoping usually clarifies the question and avoids the doubled cost of dual analysis.
> **Tradeoff:** Option B is most thorough but ~2x time/tokens; Option A risks missing material side of the ambidexterity; Option C may force you to pick before you know.
> **Or:** specify a different scoping (e.g., "focus on Layer A but flag any Layer B implications as risks").
>
> Choose: A / B / C / custom

After resolution: `python scripts/log_run.py --event ambidexterity-resolved --slug <slug> --note "[A|B|C|custom: ...]"`.

---

## Gate 2 — Factual Base Review

**Present to the user:**

> ## Gate 2: Factual Base Review
>
> All [N] sub-skills have produced outputs. Before synthesis, please validate the factual base.
>
> ### Sub-skill outputs
>
> | Sub-skill | Output path | V/C/A/I distribution | Key finding |
> |-----------|------------|---------------------|-------------|
> | [name] | `working/[file].md` | V:X% C:Y% A:Z% I:W% | [one-sentence finding] |
> | ... | | | |
>
> ### Flags
> - [Any sub-skill with >50% A/I tags — weak evidence base]
> - [Any contradictions between sub-skills, e.g., Five Forces governing force vs profit pool location]
> - **[Helmer power consistency check — ACTIVE ENFORCEMENT as of 2026-05-18]** — the structural protection named in `value-chain-profit-pools.md` (one of Helmer's 7 Powers) MUST match the dominant Power identified by `assess-moat-sources.md`. The `assess-moat-sources` skill writes a "Cross-reference reconciliation" section that reaches MATCH or MISMATCH explicitly. If MISMATCH: Gate 2 is BLOCKED — orchestrator must require rework on the weaker of the two sub-skills (typically the one with lower V/C tag density on the disputed claim) before proceeding. Resolution must be in-text; "defer to next phase" is not acceptable.
>
> ---
>
> **Why we're asking:** synthesis amplifies errors in the factual base. Catching a weak sub-skill output here costs minutes; catching it after synthesis costs hours.
> **Default if unsure:** approve all sub-skill outputs with no flags; request rework on flagged outputs. If Helmer MISMATCH flagged: rework before approving — do not defer.
> **Tradeoff:** approving weak sub-skills produces a brief that bar-tests poorly.
> **Or:** request specific rework.
>
> Approve all / rework [list] / reject

After approval: `python scripts/log_run.py --event gate-2-approved --slug <slug>`.

---

## Gate 3 — Full Draft + Bar-Test + Quality-Review Review

**Present to the user:**

> ## Gate 3: Final Draft Review
>
> The HTML brief, structured YAML, bar-test output, and analysis-quality-review audit are ready.
>
> ### Files
> - `industry-brief.html` — reader-facing HTML report (SCQA opening, Pyramid body, WTP/HTW closing), rendered via html-output
> - `industry-brief.yaml` — structured filters for downstream consumption
> - `bar-test.md` — fresh-context senior-analyst grading
> - `tasks/analysis-quality-review/<doc-slug>-<timestamp>/` — analysis-quality-review audit dir (Pass 1 structure + Pass 2 readability reports)
>
> ### Bar-test summary
> - Non-obvious observations surfaced: [N] (required: ≥3)
> - Obvious observations captured: [N] (required: ≥5)
> - Obvious-missing list: [empty / list] (required: empty)
> - Overconfidence flags: [zero / list] (required: zero)
> - Modernization flags: [zero / list] (required: zero)
> - **Internal-consistency contradictions: [zero / list]** (required: zero — "defer to Phase 2" is NOT a valid resolution; brief must either resolve in-text or change the recommendation)
>
> ### Quality-review summary (analysis-quality-review)
> - Pass 1 — argument structure: [PASS / iterations to PASS] (required: PASS)
> - Pass 2 — readability: [PASS / iterations to PASS] (required: PASS)
>
> ### Overall verdict
> [Pass / Iterate / Reject]
>
> ---
>
> **Why we're asking:** this is the final ship gate. Approval = brief lands in `industries/[slug]/` as authoritative.
> **Default if unsure:** Approve if bar-test passed cleanly; iterate the flagged sections otherwise.
> **Tradeoff:** shipping a brief that fails bar test damages future skill credibility.
> **Or:** rework specific sections.
>
> Approve / rework [sections] / reject

After approval: `python scripts/log_run.py --event gate-3-approved --slug <slug>`.
