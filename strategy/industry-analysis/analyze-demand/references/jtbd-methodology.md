# JTBD Methodology — Industry-Analysis Adaptation

## Origin and altitude shift

Jobs-to-be-Done emerged from product design — Christensen (HBS, "milkshake" case) and Ulwick (Strategyn, Outcome-Driven Innovation, 1991). The original use was **product-team-scoped**: "what job is the user hiring THIS product to do?"

At **industry-analysis altitude**, JTBD is aggregated across the buyer population. The question becomes: "what is the JOB that this industry's customers, in aggregate, are hiring solutions to perform?" The answer is the question the industry exists to answer. When that question changes — when a cross-category substitute can perform the same job — the industry is structurally exposed even when share data still looks stable.

## Job-as-process, not job-as-attribute (Ulwick)

State JTBD as a **process** with verb + object + contextual qualifier. Not "customers want a faster product." That is a feature wish. The job is the underlying process they are trying to complete.

- ❌ "Customers want a fast CRM."
- ✅ "Customers are hiring the CRM to compress the sales-rep weekly handoff from 4 hours to under 30 minutes so the rep can hit Friday quota."

The process framing reveals what could substitute (anything that completes the process is a candidate, regardless of category).

## The three components

Every JTBD has three components. State all three, even when one is minimal — omission is the most common failure mode.

### 1. Functional job
The task being completed. Always present and usually easiest to articulate. Examples:
- B2C: "complete the daily commute"
- B2B: "produce an audit-ready close package within 5 business days"

### 2. Emotional job
The feeling the buyer wants to achieve or avoid. **Real in B2B**, despite the common reflex to call B2B "rational."

- Career-risk minimization ("don't blow up on my watch") — almost universal in enterprise IT
- Confidence ("I can defend this decision to the board")
- Control ("I won't be locked in to a vendor that surprises me")
- Relief ("the painful process is finally done")

If genuinely minimal, state: "Emotional job: minimal — routinized procurement, no career exposure (e.g., consumable office supplies under threshold)." Do not omit.

### 3. Social job
How the buyer wants to be perceived. Also real in B2B.

- "Be seen as the person who modernized the stack"
- "Be seen as cost-conscious by the CFO"
- "Be seen as innovative by peers in the industry forum"
- B2C: "be seen as health-conscious," "be seen as a serious creator"

## B2B multi-stakeholder JTBD

In B2B, a single purchase involves a buying committee (Gartner: typically 6-10 stakeholders in enterprise deals). Different stakeholders are hiring the SAME purchase to do DIFFERENT jobs.

Map at least the four canonical roles:

| Role | Typical JTBD focus |
|------|--------------------|
| Economic buyer (CFO, VP, etc.) | ROI, risk, budget defensibility |
| Technical evaluator (IT, architect) | Integration, reliability, technical debt avoidance |
| End user | Time saved, friction reduced, daily-use experience |
| Procurement | Cost containment, terms, vendor risk, defensibility of process |

If any one stakeholder's JTBD is not met, the deal stalls — regardless of product quality on the other axes. Industries change when ONE of these jobs gets a new credible solution (e.g., "procurement risk" got a new solution via vendor-risk-management SaaS, reshaping enterprise software buying patterns).

For B2B industry analyses, identify which stakeholder JTBD is currently the BINDING constraint — the one whose dissatisfaction most often kills deals. That is the JTBD where substitution risk concentrates.

## Ulwick opportunity score (when granular data is available)

Where outcome-level satisfaction + importance data exists (rare in PE-CDD timelines; common in product-team contexts):

```
Opportunity = Importance + max(Importance − Satisfaction, 0)
```

Outcomes scoring >12 (on Ulwick's 10-importance + 10-satisfaction scale) are "underserved" — the highest-priority disruption attack surfaces.

In industry-analysis use, this is a directional check rather than a precise score: "the industry currently over-serves on speed and under-serves on auditability — auditability is the open attack surface."

## When JTBD breaks down at industry level

- **Pure commodity markets** (steel rebar, cement) — the JTBD is so degenerate ("provide the spec'd product at the agreed price") that JTBD analysis adds little; profit-pool + supplier-power do the real work.
- **Highly regulated markets where buyer choice is constrained** (defense procurement, regulated utilities) — JTBD is real but secondary to regulatory structure.
- **Two-sided platforms** — run JTBD on EACH side of the platform separately; the supply-side job is often misanalyzed.

When JTBD adds little, state it explicitly and weight the analysis toward substitution + WTP only. Do not force-fit.
