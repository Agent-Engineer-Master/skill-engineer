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

### RULE-2: Thiel Secrets are hypothesis generators, never truth gates

**Source:** `dtc-ecommerce-us` 2026-05-19 closing feedback gate, then sharpened 2026-06-06. Original feedback: the user endorsed 6 of 10 Secrets but clarified "this is not high conviction... they are better as lenses that suggest experiments to run." The sharpening: asking the human *which secrets are true* is a broken gate — "I don't know the answers to those, that's why they are secrets." The useful move is to use the secret-generation process to **generate ideas**, carry forward the key assumption that would make each true, and produce a **test** to validate it.

**Apply at:** Phase 4.6 candidate generation, Gate 2, Phase 5 concept generation and filter.

**What it requires:**
- The human is **never** asked whether a Secret is true. No truth-endorsement, no conviction-endorsement at the brief stage.
- Each Secret is written in **grounded form** ("industry assumes X; held because Y; capability Z makes it false as of [date]") and **emits a venture concept** into the first-principles lane.
- The secret restated as a single falsifiable claim becomes that concept's `load_bearing_hypothesis`, and the Secret ships with a `validation_test` (cheapest experiment + pass/fail thresholds + time-to-signal) and `value_if_true`.
- The human gate is **test-worthiness**: "given the prize if true and the cost/speed of the test, which of these experiments are worth funding?" — answerable without possessing the secret.
- Conviction is the *output* of running the test, not an input. There is no longer a `lens` vs `conviction` endorsement type — both are obsolete.

**Why:** a secret you can endorse on the spot isn't a secret. The old gate collected noise (shrugs) or, worse, plausibility-matching that reintroduced the very triangulation-from-existing-startups bias the skill is meant to avoid. Reframing the secret as a bet (idea + load-bearing hypothesis + cheap test) gives the human a decision they can actually make, and turns the unknowable into a fundable experiment.

### RULE-3: Y1 metrics must be bottoms-up, not goal-seeked to clear an industry projection

**Source:** `dtc-ecommerce-us` 2026-05-19 bar-test first pass. M1-DTC's original Y1 metric (40% agent-channel share by month 12) was flagged as contradicting the Bain 15-25%-by-2030 industry-wide diffusion curve. The fix (lower to 25% top-of-band with bottoms-up justification) survived second-pass bar test but the reviewer still flagged the calibration as goal-seeked.

**Apply at:** Phase 5 enrichment step (year_one_metric field on every concept).

**What it requires:**
- If a Y1 metric implies the venture will outperform industry-wide projections cited in the same dataset (Phase 3 enabling conditions), it MUST include explicit bottoms-up justification for the niche-vs-industry-average delta. Cite specific data points: conversion deltas, competing-merchant counts in the SKU set, precedent operators who achieved comparable concentration and over what timeline.
- If the metric still reads as goal-seeked after justification, add a Y2 ramp or lower the Y1 floor. Industry projections are floors when used as comparisons; concepts that imply they'll exceed them within 12 months need to defend that explicitly.

**Why:** bar-test reviewers reading cold will flag any metric that contradicts the brief's own data. Goal-seeked metrics are the most common avoidable bar-test ITERATE trigger.
