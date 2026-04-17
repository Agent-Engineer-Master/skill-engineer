---
name: audit-brand
description: >
  Audits and evolves brand positioning, voice consistency, and messaging for an existing brand.
  Works across personal brands and DTC/ecommerce store brands. Runs a structured audit across
  positioning, voice, visual direction, and content pillars, then produces a scorecard with
  specific fix recommendations. Also develops reusable messaging frameworks (positioning
  statements, value propositions, pillar definitions). Use for brand health checks, positioning
  refreshes, and messaging framework development. Do NOT invoke for building a brand from scratch
  (use /build-brand), content creation, or product copy.
argument-hint: "[personal-brand | dtc-store] [optional: specific focus area]"
---

# /audit-brand — Brand Positioning Audit & Evolution

Audit brand consistency, refresh positioning, and develop messaging frameworks for an existing brand.

**Usage:**
- `/audit-brand personal-brand` — full audit of personal brand
- `/audit-brand dtc-store` — full audit of DTC store brand
- `/audit-brand personal-brand voice` — voice-only audit
- `/audit-brand dtc-store positioning` — positioning-only refresh

---

## Overview

5 audit modules that can run independently or as a full suite. Each module produces a scorecard section and specific recommendations.

| Module | What It Checks | Output |
|--------|---------------|--------|
| 1. Positioning | Is positioning still differentiated? Has competition shifted? | Positioning scorecard + refresh recommendations |
| 2. Voice | Does content match voice guidelines? Drift detection. | Voice consistency score + specific fixes |
| 3. Visual | Do visual touchpoints match brand guidelines? | Visual consistency checklist |
| 4. Pillars | Are content pillars still resonating? Any gaps or drift? | Pillar health report |
| 5. Coherence | Wolff Olins 3-pillar check: behavior + communication + design aligned? | Overall coherence verdict |

**Full audit:** Run all 5 modules sequentially, present combined scorecard.
**Focused audit:** Run only the specified module(s).

---

## Step 0 — Load Context and Identify Brand

Determine which brand from the argument. If ambiguous, ask.

**personal-brand:**
1. Read your brand summary file — current state, pillars, thesis
2. Read your LinkedIn voice guidelines file
3. Read your X/social voice guidelines file (if it exists)
4. Read your founder/about-me context file
5. Read your anti-goals or what-to-avoid file
6. Glob your recent published posts directory — scan the 5 most recent

**dtc-store:**
1. Read your store state/context file — current store state
2. Read your brand guidelines file (if missing, stop: "No brand guidelines found. Run /build-brand first.")
3. Read any recent brand strategy notes or memory files

Set `BRAND` to `personal-brand` or `dtc-store`.

---

## Module 1 — Positioning Audit

Read `references/positioning-audit-guide.md`.

### 1a. Current Positioning Snapshot

Extract and document the brand's current positioning:
- Positioning statement (explicit or inferred from content)
- Target audience definition
- Key differentiators claimed
- Competitive frame of reference
- Brand pillars / messaging themes

### 1b. Competitive Landscape Check

**Web search** for current competitors:
- Has any competitor shifted positioning since last audit?
- Any new entrants occupying similar space?
- Has the market category changed?
- Are the brand's claimed differentiators still defensible?

### 1c. Positioning Stress Test

Read `references/positioning-audit-guide.md` — Stress Test section.

Run 5 diagnostic questions:
1. **Specificity:** Can you swap in a competitor's name and the positioning still works? If yes, it's too generic.
2. **Defensibility:** Can competitors replicate this differentiation within 6 months?
3. **Relevance:** Does the target customer still have this need? Has the need evolved?
4. **Clarity:** Can someone unfamiliar with the brand state the positioning after reading 30 seconds of content?
5. **Consistency:** Do the last 5 pieces of content all reinforce the same positioning?

### 1d. Score and Recommend

| Criterion | Score (1-5) | Evidence | Recommendation |
|-----------|-------------|----------|----------------|
| Specificity | | | |
| Defensibility | | | |
| Relevance | | | |
| Clarity | | | |
| Consistency | | | |
| **Total** | **/25** | | |

**Scoring guide:**
- 20-25: Strong — maintain current positioning
- 15-19: Adequate — targeted fixes recommended
- 10-14: Weak — positioning refresh needed
- Below 10: Critical — consider full repositioning via /build-brand

Present scorecard with specific fix recommendations for any criterion scoring 3 or below.

**Wait for review before next module.**

---

## Module 2 — Voice Audit

Read `references/voice-audit-guide.md`.

### 2a. Voice Guidelines Extraction

Extract the defined voice from guidelines:
- Core voice adjectives
- Tone dimensions (formality, attitude, authenticity, complexity)
- Banned words / preferred alternatives
- Platform-specific adaptations

### 2b. Content Sample Analysis

Read the 5 most recent pieces of content. For each:
- Does it match the defined voice adjectives?
- Does it violate any banned word rules?
- Does the tone match the expected register for the platform?
- Does it feel like the same "person" across all 5?

### 2c. Voice Drift Detection

Identify patterns of drift:
- **Tonal drift** — voice becoming more formal/casual than guidelines specify
- **Vocabulary drift** — banned words creeping in, or approved words disappearing
- **Platform bleed** — LinkedIn voice showing up on X, or vice versa
- **AI tells** — generic AI vocabulary appearing ("tapestry", "delve", "nuanced", "testament")

### 2d. Score and Recommend

| Criterion | Score (1-5) | Evidence | Recommendation |
|-----------|-------------|----------|----------------|
| Adjective fidelity | | [which adjectives present/missing] | |
| Banned word compliance | | [violations found] | |
| Platform fit | | [platform-specific issues] | |
| Cross-content consistency | | [does it feel like one person?] | |
| AI-tell absence | | [any AI vocabulary detected?] | |
| **Total** | **/25** | | |

Present scorecard. For any violations found, provide the specific sentence and a rewritten version.

**Wait for review before next module.**

---

## Module 3 — Visual Consistency Audit

*DTC store only. Skip for personal-brand (no visual guidelines to audit against).*

Read brand guidelines — visual identity sections.

### 3a. Touchpoint Checklist

Check each touchpoint for visual consistency:

| Touchpoint | Color match? | Type match? | Photography match? | Logo correct? | Notes |
|-----------|-------------|------------|-------------------|--------------|-------|
| Website (homepage) | | | | | |
| Product pages | | | | | |
| Email templates | | | | | |
| Social profiles | | | | | |
| Social posts (last 5) | | | | | |
| Packaging (if applicable) | | | | | |

### 3b. Score and Recommend

Count compliant vs. non-compliant touchpoints. Provide specific fix instructions for each non-compliant item (e.g., "Email header uses #3B82F6 instead of brand primary #2B4C7E — update template").

---

## Module 4 — Content Pillar Health

### 4a. Current Pillar Map

Extract defined content pillars (from `_summary.md` for personal brand, or brand guidelines for DTC store).

### 4b. Content Distribution Analysis

Read the last 10-15 pieces of content. Map each to a pillar:

| Content | Date | Pillar | Engagement (if available) |
|---------|------|--------|--------------------------|
| [title] | | [pillar or "off-pillar"] | |

### 4c. Pillar Health Diagnosis

For each pillar:
- **Volume:** How many of the last 15 posts mapped to this pillar?
- **Recency:** When was the last post in this pillar?
- **Resonance:** Any engagement signals (comments, shares, saves)?
- **Relevance:** Is this pillar still aligned with where the market/audience is moving?

### 4d. Recommend

Present a pillar health table:

| Pillar | Posts (last 15) | Last Post | Health | Recommendation |
|--------|----------------|-----------|--------|----------------|
| [name] | X/15 | [date] | [strong/weak/dormant] | [action] |

Flag:
- **Dormant pillars** (0 posts in last 30 days) — retire or reactivate?
- **Dominant pillars** (>60% of content) — over-indexed, diversify?
- **Missing topics** — are there audience-relevant themes not covered by any pillar?

Present 3 options for pillar evolution if changes are needed:
1. Keep current pillars, adjust content mix
2. Retire [pillar], add [new pillar]
3. Reframe [pillar] to encompass [emerging topic]

**Wait for decision before next module.**

---

## Module 5 — Coherence Check (Wolff Olins)

Read `references/positioning-audit-guide.md` — Coherence section.

Run the 3-pillar coherence check:

| Pillar | Question | Aligned? | Evidence |
|--------|----------|----------|----------|
| **Behavior** | Does what the brand DOES match what it SAYS it stands for? | [Y/N] | [specific evidence] |
| **Communication** | Does the voice/tone match the positioning and archetype? | [Y/N] | [specific evidence] |
| **Design** | Does the visual identity match the personality and positioning? | [Y/N] | [specific evidence] |

If any pillar is misaligned:
- Identify the root cause (did positioning shift but voice didn't follow? Did visual evolve but positioning stayed static?)
- Recommend which element to adjust (usually: adjust the lagging element to match the leading one)

---

## Combined Scorecard (Full Audit)

After all modules, present a combined scorecard:

```
## Brand Audit Scorecard — [BRAND] — [DATE]

| Module | Score | Health | Top Issue |
|--------|-------|--------|-----------|
| Positioning | /25 | [Strong/Adequate/Weak/Critical] | [1-line] |
| Voice | /25 | [Strong/Adequate/Weak/Critical] | [1-line] |
| Visual | [N/A or /N] | [Compliant/Issues] | [1-line] |
| Pillars | — | [Healthy/Needs attention] | [1-line] |
| Coherence | — | [Aligned/Misaligned] | [1-line] |

### Priority Actions (ranked)
1. [Highest impact fix]
2. [Second priority]
3. [Third priority]

### Recommended Next Audit: [date — typically 30-90 days]
```

---

## Messaging Framework Development

When invoked specifically for messaging work (not a full audit), develop reusable frameworks:

### Positioning Statement
"For [audience] who [need], [Brand] is the [category] that [benefit], unlike [competitor] who [limitation]."

### Value Proposition (3 tiers)
- **Feature:** [what it does]
- **Benefit:** [what it means]
- **Emotional benefit:** [how it makes them feel]

### Elevator Pitch (30 seconds)
[1-paragraph pitch derived from positioning]

### Content Pillar Definitions
For each pillar: name, description, audience need it serves, content types it includes, content types it excludes.

### Messaging Do/Don't
| Do | Don't |
|----|-------|
| [approved message] | [prohibited message] |

Save messaging frameworks to your project's appropriate location:
- Personal brand: your brand content directory (e.g. `brand/content/_messaging-framework.md`)
- DTC store: your store context directory (e.g. `store/messaging-framework.md`)

---

## Output Logging

Optionally log audit results to your memory or notes system:

```yaml
---
type: recall
date: YYYY-MM-DD
brand: [personal-brand | dtc-store]
tags: [audit-brand, positioning, voice, visual, pillars, coherence]
---

Ran [full/focused] brand audit for [brand].
Positioning: [score]/25 ([health]). Voice: [score]/25 ([health]).
Top issue: [1-sentence]. Priority action: [1-sentence].
Next audit recommended: [date].
```

---

## Rules

1. Reference files are required — read the specified guide before producing any module output.
2. Every score must cite specific evidence — no unsupported ratings.
3. Every issue must include a specific fix recommendation, not just identification.
4. For voice violations, provide the original sentence AND a rewritten version.
5. Never recommend a full repositioning lightly — only when score is below 10/25. Most brands need targeted fixes, not overhauls.
6. Present numbered options at all human decision points.
7. Cross-check all recommendations against the brand's anti-goals or strategic constraints.
8. When the user flags something to never do again, update the relevant reference file immediately.
9. When the user approves an audit output, save it to `assets/approved-examples/`.
10. Never mix brands in a single audit — run separate audits for personal-brand and dtc-store.
