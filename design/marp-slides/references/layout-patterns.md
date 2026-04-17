# MARP Layout Patterns Reference

## Table of contents
1. [Layout rotation rule](#layout-rotation-rule)
2. [Layout inventory](#layout-inventory)
3. [Slide count heuristics](#slide-count-heuristics)
4. [Composition principles](#composition-principles)
5. [Speaker notes protocol](#speaker-notes-protocol)

---

## Layout rotation rule

**Never use the same layout type 3+ slides in a row.** Visual fatigue sets in immediately when the audience can predict the next slide's structure. Rotate through at least 3 different layout types across any 5-slide run.

**Recommended rotation example (10-slide deck):**
1. Hero (title)
2. Stats row (3 metric cards)
3. Text + image split
4. SVG chart + bullet insight
5. Full-bleed background image
6. Card grid (2×2 or 3×1)
7. Timeline or before/after
8. Text-heavy (but ≤6 bullets)
9. Terminal / code mockup
10. CTA / close

Adapt to content — but ensure visual variety every 2–3 slides.

---

## Layout inventory

### Hero / title slide
```markdown
<!-- _class: lead -->
# Main Title
## Subtitle line — thin, grey
```
Best used at: deck open, major section transitions. Use sparingly — max 2 in a 10-slide deck.

### Stats row (metric cards)
3 metric cards side-by-side using flex layout (see `components.md` → Metric card).
Best used at: opening summary, KPI snapshots, before/after comparisons.

### Text + image split
```markdown
![bg right:40%](./image.png)
## Slide Title
- Point one
- Point two
- Point three
```
Best used at: product shots, case studies, testimonials.

### Chart slide
SVG chart full-width + one insight bullet below. Keep the bullet to one line — the chart carries the detail.
Best used at: trend data, comparisons, survey results.

### Full-bleed background
```markdown
![bg brightness:0.12](./photo.jpg)
<!-- _class: lead -->
# Headline
```
Best used at: section dividers, emotional beats, quotes.

### Card grid
2×2 or 3×1 cards using flex layout (see `components.md` → Card row).
Best used at: feature comparisons, process steps, category breakdowns.

### Timeline
Vertical timeline component (see `components.md` → Timeline).
Best used at: roadmaps, history, step-by-step processes.

### Before / after
Two-panel split with red/green top borders (see `components.md` → Before/after split).
Best used at: problem/solution, old/new state, hypothesis/result.

### Terminal / code
Dark terminal mockup or fenced code block.
Best used at: technical demos, command examples, output samples.

### List slide
Standard markdown list. Hard limit: 6 bullets, one line each.
Best used at: requirements, decisions, options — when no visual fits better.

### CTA / close
Minimal centered layout with a single call to action or next step.
Best used at: deck close only.

---

## Slide count heuristics

Use these when the user hasn't specified slide count:

| Content volume | Suggested slides |
|---|---|
| Brief overview, one topic | 5–8 |
| Standard presentation, single theme | 8–12 |
| Deep dive, multi-section | 12–18 |
| Full workshop or course module | 18–25 |

Add 1 slide per major section transition. Subtract if content is sparse — blank-looking slides are worse than fewer slides.

---

## Composition principles

**One idea per slide.** If a slide needs a heading and more than 6 bullets to express the idea, it contains multiple ideas — split it.

**Visual element required on every slide.** A slide with only text is a word document. Every slide should have at least one of: image, SVG chart, styled card, code block, or icon.

**Titles are headlines, not labels.** Bad: "Revenue Overview". Good: "Revenue grew 40% in Q1". Keep to ≤35 characters. A title that's a complete sentence with an insight is always stronger.

**Breadcrumb headers.** Add `header: "[Deck Title] > [Section]"` or use per-slide `<!-- _header: "..." -->` overrides to keep the audience oriented.

**60-30-10 on every slide.** Background = 60%, neutral elements (cards, borders) = 30%, accent = 10%. One or two accented elements per slide maximum.

---

## Speaker notes protocol

Speaker notes are not optional decoration — they are where 80% of the content lives.

Every slide should have a note block:
```markdown
<!-- 
Speaker note: The headline says revenue grew 40%. The detail: this was driven by the enterprise segment, not SMB. Three accounts closed in Q1 that had been in pipeline since Q3 2025. The SMB trend is actually flat — don't lead with that in Q&A.
-->
```

What belongs in notes: supporting data, context, anticipated questions, talking points, transition cues.
What does NOT belong in notes: repetition of the slide title, generic filler ("This slide covers...").
