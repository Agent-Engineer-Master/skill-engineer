# AI as Named Force

In 2026, AI is a structural force in nearly every industry. The Five Forces analysis must assess AI explicitly, with three named sub-checks. Inferred from librarian research on current MBB practice (May 2026).

## The three sub-checks

### 1. Cost-structure impact

**Question:** Which activities in this industry's value chain does AI automate or compress? What % of cost base is affected?

**How to assess:**
- List the top 3-5 cost activities (often: sales, customer support, content production, code/engineering, design, analysis/research)
- For each: is AI automating it now, plausibly within 2 years, or unlikely?
- Estimate the % of total cost base subject to AI compression

**Severity scale:**
- **Low:** <10% of cost base affected, automation gradual
- **Moderate:** 10-30% affected, automation active
- **High:** >30% affected, incumbents restructuring

### 2. New-entry vector

**Question:** Is there an AI-native entrant in this industry with a fundamentally lower cost structure or differentiated product? Named, funded, and active?

**How to assess:**
- Search recent Series A/B funding announcements + Y Combinator batches for "AI-native [industry]"
- Identify entrants that did NOT exist before 2022
- For each: funding raised, team size, traction signal (revenue, customers, partnership)

**Severity scale:**
- **Absent:** no material AI-native entrants identified
- **Present:** one or more AI-native entrants with documented traction

### 3. Data-intermediary position

**Question:** Who owns the data needed to train AI models for this industry? Is that position concentrated, contested, or unowned?

**How to assess:**
- Identify the data assets that would train a superior AI model for this industry (e.g., historical medical records for medtech AI, claims data for insurance AI, transaction data for fintech AI)
- Assess concentration: is it held by incumbents (high data moat), held by platforms (concentrated intermediation), or available to all (no moat)?

**Severity scale:**
- **None:** data is publicly available or unowned by industry players
- **Contested:** multiple players hold partial data assets; no dominant intermediary
- **Concentrated:** one or two players hold the strategically critical data

## Output

A section in `five-forces.md`:

```markdown
## AI as Named Force

| Sub-check | Severity | Evidence |
|-----------|----------|----------|
| Cost-structure impact | Low/Moderate/High | [description + V/C/A/I tag] |
| New-entry vector | Absent/Present | [named entrants + traction + V/C/A/I tag] |
| Data-intermediary position | None/Contested/Concentrated | [data assets + holders + V/C/A/I tag] |

**Aggregate AI intensity:** Low | Moderate | High
**Direction:** intensifying | stable | weakening
**Structural reason:** [one sentence]
```

## When "AI not material" is acceptable

Rare but possible. Industries where:
- Cost base is dominated by physical capital/materials (e.g., bulk shipping, real estate ownership)
- AI cannot meaningfully compress cost or differentiate product
- No identified AI-native entrant in 3+ years of opportunity

State this explicitly: "AI not material because [reason]." Don't skip the section.

## Why this is a separate section, not absorbed into Substitutes or New Entry

AI functions simultaneously as substitute threat AND new-entry vector AND cost compressor on incumbents. Treating it as a sub-bullet under one classical force misses the other two effects. The separate section forces the analyst to consider all three.

## AI as transforming overlay — inline per force (primary) + reshape matrix (summary)

The WEF "New Five Forces" (Sep 2025) and current McKinsey practice converge on one point: AI is not just a sixth force, it **reconfigures the existing five**. The standalone AI section is necessary but not sufficient — the analyst must also state how AI reshapes each classical force.

**Primary placement: inline per force.** Each of the five classical force sections in `five-forces.md` must include an AI-reshape subsection — direction of change (intensifying / weakening / no material effect) plus one tagged evidence claim when the effect is non-trivial. The validator enforces that the word "AI" appears within ~500 chars of every classical force section header. This is where the analytical work happens.

**Secondary placement: consolidated matrix.** After the per-force assessments and the standalone AI section, restate the inline conclusions as a one-table summary so a reader can scan the cross-cutting picture in 10 seconds. The matrix below summarizes what was already written inline; it does not replace it.

```markdown
## AI Reshape Matrix — How AI is Transforming Each Force

| Classical force | AI mechanism | Direction of change | Evidence |
|-----------------|-------------|---------------------|----------|
| Rivalry | [e.g., shifts competition from feature parity to learning-loop speed] | intensifying / stable / weakening | [V/C/A/I tag] |
| Supplier Power | [e.g., AI-driven alt-sourcing reduces specialist supplier leverage] | ↑ / ↔ / ↓ | [tag] |
| Buyer Power | [e.g., AI shopping agents collapse buyer search costs, intensify price comparison] | ↑ / ↔ / ↓ | [tag] |
| Threat of New Entry | [e.g., AI compresses capital + headcount required to MVP] | ↑ / ↔ / ↓ | [tag] |
| Threat of Substitutes | [e.g., generative AI displaces category outright] | ↑ / ↔ / ↓ | [tag] |
```

**Per-force expected reshape patterns (as a starting hypothesis to falsify, not a default to copy):**

- **Rivalry** — usually intensifying. Compute and model access democratize; competition shifts to data and learning speed.
- **Supplier Power** — usually weakening. AI enables alternative sourcing, synthetic substitutes, and supplier-side automation.
- **Buyer Power** — usually intensifying. AI-mediated shopping/search reduces buyer information asymmetry.
- **Threat of New Entry** — usually intensifying. AI-native entrants achieve cost structures incumbents cannot match without restructuring.
- **Threat of Substitutes** — usually intensifying. Cross-category substitution accelerates; AI-native alternatives appear faster.

If your analysis shows AI weakening any force, that is an interesting finding — interrogate it carefully and tag the evidence with extra rigor.

## When the reshape matrix can be light

If the standalone AI section concludes "AI not material because [physical capital dominates / no AI-native entry vector / data unavailable]," then the reshape matrix entries can read "No material AI effect on this force because [reason]." Skipping the matrix entirely is not allowed even in that case — the agent must explicitly state non-impact, not silently omit.

## Why this matters

In v1 of the skill, AI was a sidecar section. Senior reviewers reading the output came away thinking "AI is happening over there, the rest of the industry is unchanged." That conclusion is structurally wrong in 2026 for nearly every industry. The reshape matrix forces the analyst to state the cross-cutting effects, even if some entries are "no material effect."
