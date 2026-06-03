# Edge Cases — reimagine-industry

Industry-specific exceptions and factual quirks accumulated during use.

## Industries with two-sided dynamics

(empty — populate when first encountered)

## Heavily regulated industries

(empty)

## B2B vs B2C application differences

(empty)

## Other exceptions

(empty)

---

## Hard rules (never-again, derived from user feedback)

These rules fail-loud if violated during a run. They override anti-patterns and quotas elsewhere in the skill.

### RULE-1: Concepts must carry a plain-English handle and a plain-English essence-distillation alongside the structured form

**Source:** `dtc-ecommerce-us` 2026-05-19 closing feedback gate. The user asked twice during the run for plain-English explanations of concepts and Thiel Secrets ("explain to me the key differences between M1 and M7"; "explain each of them in English, not just jargon"). The structured form (concept_id + signal citations + endorsed-secret dependencies) is for the dataset and bar test; human gate reviews require a layer up.

**Apply at:** every human-gate report (Gate 2, Gate 3) and any in-conversation review of concepts or Secrets.

**What it requires:**
- Each concept gets a 3-5 word memorable handle that captures the core idea, not just a `concept_id`. Example: "Wirecutter-for-niche, AI-citation-first" ✓ vs "AUTH-DTC" alone ✗.
- Each concept gets a one-sentence plain-English distillation of WHAT IT IS at the start of any review, before structured fields.
- Each Thiel Secret gets the same treatment — name the contrarian belief in one plain-English sentence before showing the evidence-for / evidence-against / falsifiable-by structure.

**Why:** structured-form concept descriptions read as "code" to senior readers — they require parsing rather than recognition. The handle + distillation is the recognition layer. Without it, the user has to ask twice, which is a sign the gate review failed.

### RULE-2: Thiel Secrets are scenario lenses, not conviction filters, unless the user explicitly signals high conviction

**Source:** `dtc-ecommerce-us` 2026-05-19 closing feedback gate. The user endorsed 6 of 10 Secrets but clarified: "this is not high conviction, I just think these are positions where the data is inconclusive either way... They are really great lynch points that define the strategy, but perhaps they are better as different lenses that suggest experiments to run rather than directly filter ideas."

**Apply at:** Phase 4.6 candidate generation, Gate 2 endorsement step, Phase 5 concept generation.

**What it requires:**
- At Gate 2 Thiel endorsement, frame the prompt explicitly as: "Which of these contrarian positions do you want to use as STRATEGIC LENSES that suggest experiments to run? Endorsing here doesn't filter out concepts that bet against the Secret — it surfaces the Secret as a defining hypothesis the brief should explicitly engage with."
- Phase 5 concept generation should generate concepts that span both sides of each endorsed Secret where the Secret-bet matters. Each concept's `endorsed_secrets_dependency` block already captures "depends-on / survives-falsification / counter-bet" — preserve that, but interpret a `depends-on` as "this is the concept that wins if Secret is true," not "this Secret is required to be true for the concept to be considered."
- The Phase 5 filter should compose a portfolio that is robust across the Secret hypothesis space rather than concentrated on Secrets being true.
- If the user explicitly signals high conviction on a Secret (e.g., "I genuinely believe X and would bet the company on it"), THEN apply the original Thiel filter discipline. Default is scenario-lens framing.

**Why:** the literal Thiel framing of "Secret = load-bearing belief you'd stake the venture on" is correct for late-stage founder commitment, but at the brief-writing stage most contrarian positions are open empirical bets. Treating them as filters risks over-filtering Phase 5 and producing a thin or single-thesis concept set.

### RULE-3: Y1 metrics must be bottoms-up, not goal-seeked to clear an industry projection

**Source:** `dtc-ecommerce-us` 2026-05-19 bar-test first pass. M1-DTC's original Y1 metric (40% agent-channel share by month 12) was flagged as contradicting the Bain 15-25%-by-2030 industry-wide diffusion curve. The fix (lower to 25% top-of-band with bottoms-up justification) survived second-pass bar test but the reviewer still flagged the calibration as goal-seeked.

**Apply at:** Phase 5 enrichment step (year_one_metric field on every concept).

**What it requires:**
- If a Y1 metric implies the venture will outperform industry-wide projections cited in the same dataset (Phase 3 enabling conditions), it MUST include explicit bottoms-up justification for the niche-vs-industry-average delta. Cite specific data points: conversion deltas, competing-merchant counts in the SKU set, precedent operators who achieved comparable concentration and over what timeline.
- If the metric still reads as goal-seeked after justification, add a Y2 ramp or lower the Y1 floor. Industry projections are floors when used as comparisons; concepts that imply they'll exceed them within 12 months need to defend that explicitly.

**Why:** bar-test reviewers reading cold will flag any metric that contradicts the brief's own data. Goal-seeked metrics are the most common avoidable bar-test ITERATE trigger.
