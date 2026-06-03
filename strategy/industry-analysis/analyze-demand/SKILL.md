---
name: analyze-demand
description: "Structural demand-side analysis for a defined industry: JTBD (Christensen/Ulwick — functional + emotional + social), JTBD-based segmentation (NOT demographic), substitution risk per segment (named cross-category candidates + switching cost + likelihood), WTP drivers per segment, and named leading demand signals. Output: demand.md — surfaces disruption threats before they show in share data. Sub-skill of analyze-industry, also invocable standalone. CONDITIONAL: orchestrator SKIPS when ALL three hold — market mature (>20yr) AND demand volatility <±2% AND no substitution threat flagged in Five Forces; standalone caller decides. Triggers: 'analyze demand for [industry]', 'JTBD for [industry]', 'customer segmentation for [industry]', 'substitution risk for [industry]', 'WTP drivers in [industry]'. Do NOT use for product-level JTBD, single-company positioning (use build-company-model), market sizing (use size-market), or supply-side competition (use map-competitive-arena)."
---

# Analyze Demand

For a defined industry, produce a structural demand-side analysis. Output: `demand.md` that names the JOB the industry's customers are hiring solutions to perform, segments by that job (not demographics), and surfaces substitution risk before it shows in share data.

**The discipline:** Demand-side analysis is the early-warning system for disruption. Five Forces tells you the structure; profit pools tell you where the money sits today; competitive arena tells you who is winning. Demand analysis tells you whether the question being asked is about to change. JTBD originated in product design; at industry-analysis level it aggregates outcomes across the buyer population to spot cross-category substitution before market-share data moves.

**Iron rules:**
- Every fact-claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- ≥1 JTBD identified with ALL THREE components (functional / emotional / social) named — even if a component is "minimal" or "absent," state it explicitly. Do not omit.
- ≥2 customer segments defined by **the job they hire the product to do**, not by demographic or firmographic attributes. "Young urban professionals" or "mid-market SaaS companies" fail this test; "buyers hiring the product to reduce time-to-decision in regulatory submissions" passes.
- ≥1 substitution risk with **named** substitute candidate (cross-category preferred), explicit switching cost, and stated likelihood. Naming "general competition" or "other vendors" fails.
- Substitution analysis section MUST use the standard heading `## Substitution Risk` (exact wording, level-2 heading). Downstream consumers parse by heading; variants fail.
- WTP drivers stated per segment — NOT a single price. Drivers explain WHY this segment will or won't pay.
- ≥1 named demand signal with a measurable leading indicator (search trend, channel check, expert-interview language shift, regulatory filing shift, etc.). Lagging metrics like revenue fail.

## Process

### 1. Intake — lock the analysis frame
Confirm: industry slug, geographic scope, B2B / B2C / hybrid, focal value-chain layer (must match the layer used in `map-five-forces` if running in orchestrator mode), buying-unit definition (individual / household / SMB / enterprise procurement committee). Read `references/jtbd-methodology.md` and `references/customer-segmentation.md`. Note any substitution threats already flagged in `working/five-forces.md` (orchestrator mode) — they are the priority candidates to chase in step 4.

### 2. Identify the Job(s)-to-be-Done
Read `references/jtbd-methodology.md`. For this industry, name the primary JOB customers are hiring solutions to perform. Express as **job-as-process**, not job-as-attribute (Ulwick): "[verb] [object] [contextual qualifier]" — e.g., "minimize time-to-decision for a regulatory submission under FDA Q-Sub review." For each identified JTBD, name all three components:

- **Functional job** — the task being done (always present; the easiest to articulate)
- **Emotional job** — the feeling the buyer wants to achieve or avoid (career-risk minimization, confidence, control). In B2B, this is real and usually under-stated.
- **Social job** — how the buyer wants to be perceived (innovative, prudent, cost-conscious, modernizer)

If a component is genuinely minimal, state "Emotional job: minimal — purchase is routinized procurement with no career exposure" rather than omitting. Each JTBD carries ≥1 tagged evidence claim.

For B2B industries, additionally map jobs across the buying committee — read `references/jtbd-methodology.md` "B2B multi-stakeholder JTBD" section. Different stakeholders (economic buyer, technical evaluator, user, procurement) often have DIFFERENT jobs for the same purchase.

### 3. Segment by JTBD, not demographics
Read `references/customer-segmentation.md`. Define ≥2 customer segments grounded in the job they are hiring the product to do. Each segment needs:

- **Segment name** — describes the job-context, not the buyer demographic
- **Distinguishing JTBD or outcome-priority pattern** — what makes this segment hire the product differently
- **Approximate size or weight in the market** (V/C/A/I-tagged)
- **Why this segment is structurally distinct** — what would cause it to switch differently than other segments

Anti-pattern (REJECTED): "Mid-market enterprises in financial services," "Gen-Z consumers," "manufacturers with >$500M revenue." These are demographic/firmographic boxes, not jobs.
Correct pattern (ACCEPTED): "Buyers hiring the product to compress a 6-week manual reconciliation cycle into a single audit-ready report," "Buyers hiring the product as career insurance against a known regulator escalation."

The validator scans for demographic-only segment names and fails outputs that show segmentation by attribute rather than job. If a segment is *named* demographically but its definition is genuinely job-based, restate the name to lead with the job.

### 4. Substitution risk per segment
Read `references/substitution-risk.md`. **The section heading must be exactly `## Substitution Risk` (verbatim wording, level-2 heading).** Downstream consumers (Five Forces reconciliation, analyze-trajectory cross-category-substitute scan) parse this section by exact heading match. Variants like "Threat from Adjacent Categories", "Substitutes", or "Cross-Category Risk" fail validation.

For each segment, name the leading substitute candidates — cross-category preferred. A substitute is anything else the buyer could hire to perform the same JOB, including:

- In-category competitors (weakest substitute analysis — usually already in Five Forces)
- Cross-category substitutes (Zoom for travel, Airbnb for hotels, GLP-1 for snack food + diet programs, ChatGPT for Google search + entry-level analyst work, AI coding assistants for offshore dev labor)
- DIY / in-house build
- Do-nothing (the most common substitute; explicitly assess)

For each named substitute, state:
- **Switching cost** — financial + workflow + skill + psychological (cite anchor)
- **Likelihood over 3-yr horizon** — Low / Moderate / High with reasoning
- **Trigger event that would accelerate substitution** — what would have to be true

At least ONE substitution risk must name a specific candidate with these three fields filled. "Generic competitor pressure" fails.

### 5. Willingness-to-pay drivers per segment
Read `references/wtp-drivers.md`. For each segment, identify the DRIVERS of willingness to pay — not a single number. Drivers explain why this segment's price ceiling sits where it sits. Examples:

- "Regulated buyers in segment A will pay 3-5x premium for documented compliance proofs because non-compliance carries seven-figure fines [V: FDA 483 history]"
- "Self-serve developer-tooling buyers in segment B will not pay until usage exceeds free tier ~2x because the procurement friction is higher than the rational threshold [C: PriceBeam B2B WTP study 2024]"
- "Consumer segment C exhibits steep WTP cliff at $X where category framing shifts from impulse to considered [A: vendor pricing test, single data point — confirm]"

Distinguish B2B vs B2C explicitly: B2B WTP is dominated by ROI quantification + procurement-committee risk aversion; B2C WTP is dominated by perceived value at point-of-purchase + reference pricing. State your method anchor (Van Westendorp / conjoint / value-theory / expert-elicit) when available.

### 6. Name ≥1 leading demand signal
Read `references/demand-signals.md`. Identify at least one MEASURABLE LEADING INDICATOR that would surface a demand shift before it appears in share data. Required format:

- **Signal name** — what to watch
- **Measurement source** — where the indicator lives (Google Trends, app-store rank, GitHub stars, distributor reorder cadence, regulatory filing keyword frequency, expert-interview language shift, job-posting taxonomy)
- **Threshold** — what level of change constitutes a meaningful shift
- **What it would mean** — the structural shift the signal would imply

Lagging indicators (revenue, share, NPS) fail this check. A demand signal is something you could observe BEFORE the market noticed.

### 7. Cross-reference Five Forces (orchestrator mode)
If `working/five-forces.md` exists in the same industry folder, reconcile: every substitution threat flagged in Five Forces "Threat of Substitutes" must appear here with deeper treatment. If Five Forces flagged a threat that this analysis cannot find a JTBD basis for, flag for Gate 2 — one of the two is wrong. If standalone mode, add note: "Five Forces cross-reference deferred — five-forces.md not present."

### 8. Append structured `next_skills` YAML block
End the output file with:

```
---
next_skills:
  - map-competitive-arena    # demand-side findings inform supply-side competitive mapping
  - analyze-trajectory    # cross-category substitution candidates often signal trajectory shifts
  - assess-moat-sources    # WTP drivers reveal which moat types matter most in this industry
---
```

At least one skill must be listed.

### 9. Validate + write output
Run `python scripts/validate_demand.py --output-path <path>` — checks: ≥1 JTBD with all 3 components, ≥2 JTBD-based segments (no demographic-only names), ≥1 named substitution risk with switching cost + likelihood, WTP drivers per segment, ≥1 named demand signal with measurement source, V/C/A/I tag coverage, `next_skills:` YAML block. Write to `working/demand.md` (orchestrator) or `standalone/analyze-demand-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

## Gotchas

- **Symptom:** segments named "Enterprise buyers," "SMBs," "Gen-Z consumers." **Cause:** demographic/firmographic segmentation imported from marketing. **Fix:** validator flags demographic-only segment names and fails. Restate segments by the JOB the buyer is hiring the product to do.
- **Symptom:** B2B JTBD lists only functional job; emotional and social marked "N/A." **Cause:** drafter believes B2B is purely rational. **Fix:** validator requires all three components named. Career-risk minimization is an emotional job; "modernizer / cost-conscious procurement" is a social job. State explicitly even when modest.
- **Symptom:** substitution section lists only direct in-category competitors. **Cause:** substitute defined too narrowly. **Fix:** at least one cross-category substitute or "do-nothing" candidate is expected. The validator requires named substitute candidates (not "general competition") with switching cost AND likelihood.
- **Symptom:** WTP stated as a single price ($X per seat per month). **Cause:** confused product pricing with industry WTP-driver analysis. **Fix:** state DRIVERS that explain why the segment's price ceiling sits where it sits — regulation, ROI, reference pricing, procurement friction, etc.
- **Symptom:** demand signal listed as "revenue growth" or "market share." **Cause:** lagging indicator confused with leading. **Fix:** signal must be observable BEFORE the shift hits financial results — search trends, channel checks, expert-interview language, job-posting taxonomy, regulatory filings.
- **Symptom:** product-design-flavor JTBD ("user wants the button to be blue"). **Cause:** Ulwick/Christensen applied at wrong altitude. **Fix:** at industry-analysis level the JOB aggregates across the buyer population — it is the question the industry exists to answer, not a feature spec.

## Rules

- Never accept demographic/firmographic segmentation as a substitute for JTBD-based segmentation.
- Never omit emotional or social jobs from B2B analyses — state them explicitly, even if modest.
- Never list substitutes as "general competition" or "other vendors" — name candidates with switching cost and likelihood.
- Never rename the substitution section heading. The exact wording `## Substitution Risk` is required for downstream consumer consistency.
- Never state WTP as a single number without driver decomposition.
- Never present lagging indicators (revenue, share) as demand signals.
- Every fact-claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.

## Old patterns

None yet — v1 (2026-05-18 initial build, Phase 2 of industry-analysis collection).

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
