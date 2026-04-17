# MARP Slides — Quality Rubric

Scoring dimensions for subjective output evaluation. 7 dimensions; score each 1–3. Overall = mean, rounded.

Score thresholds: 3.0 excellent, 2.5–2.9 good, 2.0–2.4 passing, <2.0 failing.

A mediocre AI-generated deck should score 1–2 on at least **Narrative arc**, **Visual variety**, and **Information density** — these three dimensions reliably discriminate.

---

## Dimensions

### 1. Narrative arc
Does the deck tell a story with a clear opening, body, and close? Does it have momentum — each slide setting up the next?

| Score | Description |
|---|---|
| 1 | Slides feel like a list of topics dumped in order. No through-line. Audience would not know what to take away. |
| 2 | Opening and close exist, but body slides feel disconnected or arbitrary in sequence. |
| 3 | Clear arc: setup → insight → evidence → implication → CTA/close. Each slide earns its position. |

### 2. Visual variety
Does the deck rotate through different layout types? Is there a mix of visual elements (charts, images, code, cards)?

| Score | Description |
|---|---|
| 1 | Same heading + bullets layout used on 3+ consecutive slides. No charts, images, or visual components. |
| 2 | Some variety exists but relies on 1–2 layout types throughout. Visual elements feel added as decoration rather than supporting the content. |
| 3 | Layout rotates every 2–3 slides. Visual element type (chart vs image vs code vs card) chosen to match slide content, not applied uniformly. |

### 3. Information density
Are slides focused on one idea? Is the right amount of content on-slide vs in speaker notes?

| Score | Description |
|---|---|
| 1 | Multiple ideas per slide. Bullets exceed 6. Speaker notes are empty or repeat the slide verbatim. |
| 2 | Most slides are focused but some are overloaded. Speaker notes exist but are generic ("This slide covers..."). |
| 3 | One clear idea per slide. Speaker notes add context, data, and talking points not present on the slide. |

### 4. Theme coherence
Is the CSS theme applied consistently? Does the visual identity (color, typography, spacing) hold across the deck?

| Score | Description |
|---|---|
| 1 | Inconsistent styling — multiple competing colors, mixed font weights, uneven spacing. |
| 2 | Theme is mostly consistent but has drift (one slide with different background, inconsistent heading sizes). |
| 3 | Consistent palette (60-30-10), typography hierarchy maintained throughout, accent used sparingly and correctly. |

### 5. Title quality
Do slide titles act as insight headlines rather than generic labels?

| Score | Description |
|---|---|
| 1 | Titles are generic labels ("Revenue", "Overview", "Next Steps"). Audience learns nothing from the title alone. |
| 2 | Some titles have insight but others are labels. Titles are within length limit but not memorable. |
| 3 | Every title is a specific insight or claim (≤35 chars). A reader skimming just titles would understand the deck's argument. |

### 6. Technical correctness
Are MARP-specific technical rules followed? (See `references/quality-rules.md` for full list.)

| Score | Description |
|---|---|
| 1 | Uses `*` bullets (animation trigger), absolute image paths, or SVG backgrounds in `cover` mode. Missing .marprc or allow-local-files. |
| 2 | Most technical rules followed but 1–2 violations present (e.g. a single slide with a title slightly over 35 chars). |
| 3 | All technical rules pass. No `*` bullets, relative image paths, SVG in `contain`, .marprc present, speaker notes on all content slides. |

### 7. Brand alignment
Does the deck use the correct brand colors, typography, and voice for the stated context?

| Score | Description |
|---|---|
| 1 | Deck uses default orange theme when brand guidelines specify different colors, or uses a mismatched font pairing for the content type. |
| 2 | Brand colors are present but typography or spacing doesn't match brand guidelines. |
| 3 | Deck correctly derives theme from brand-guidelines.md (or correctly uses default dark theme when no brand context is specified). |
| N/A | No brand context specified and no brand guidelines file available. Mark N/A with reason. |
