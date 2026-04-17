---
name: marp-slides
description: Creates MARP presentation decks (.md files rendered to PDF/HTML/PPTX via marp CLI) with custom CSS themes, SVG inline charts, dashboard components, and speaker notes. Use when asked to create slides, build a deck, make a presentation, generate MARP output, design a theme, edit existing slides, or convert content into a slide format. Also handles read/summarize requests on existing MARP files. Do NOT use for standalone image generation, static infographics, or PowerPoint requests with no MARP involvement.
version: 3.0
updated: 2026-04-11
---

# MARP Slides

## Startup
1. Read `references/learnings.md` — summarize the 3 most relevant bullets for this task
2. Detect mode from the request (see Mode Selector)

## Mode Selector

| Request signals | Mode |
|---|---|
| "create", "build", "make slides", "new deck", "presentation" | **A: Create** |
| "edit", "update", "change slide N", "revise", "fix" | **B: Edit** |
| "theme only", "CSS only", "just the styles", "color palette" | **C: Theme** |
| "convert from", "turn this into slides", "import", "use this outline" | **D: Convert** |
| "summarize this deck", "what does this cover", "read this marp" | **E: Read** |

---

## Mode A: Create

### A1. Intake (ask all at once in a single message)
Present these 4 questions before generating anything:
1. **Topic + purpose** — what is the deck about, and who is the audience?
2. **Slide count** — how many slides? (if unsure, apply word-count heuristic from `references/quality-rules.md`)
3. **Theme** — dark (default) or light? Describe a vibe or brand if relevant.
4. **Brand context** — use existing brand colors/logo? (if yes, read your brand guidelines file)

Wait for reply before continuing.

**Why:** Generating before intent is locked is the #1 source of wasted cycles in deck authoring. The 4-question intake costs one round-trip and saves 3–5 regeneration loops.

### A2. Theme + outline
1. Select theme using signal-to-theme mapping table in `references/themes.md`
2. Draft a slide-by-slide outline: slide title, one key idea, layout type, visual element planned
3. Present **3 layout direction options** (e.g. minimal / data-heavy / editorial) — not full decks, just 3-slide skeleton previews as markdown
4. Wait for user to approve direction or request changes before generating the full deck

### A3. Generate
1. Read `references/components.md` for SVG chart and component patterns
2. Read `references/layout-patterns.md` for rotation rules and composition guidelines
3. Read 2–3 examples from `examples/` that most closely match the approved style
4. Generate the full `.md` MARP file

**Hard rules during generation (enforce silently — do not annotate violations):**
- Use `-` for list items, never `*` (asterisks trigger animation mode in Marp live preview)
- Rotate layout type every 2–3 slides — same template 3x in a row = quality failure
- Titles ≤35 characters; bullets ≤6 per slide; one key idea per slide
- Put context and detail in speaker notes (`<!-- note: ... -->`), not on slides
- Never add decorative accent lines directly under slide titles (telltale AI pattern)
- SVG backgrounds: always `contain`, never `cover` (cover crops charts at edges)

### A4. QA self-review
1. Load `references/quality-rules.md` — run SlideGauge checklist against the generated deck
2. Fix any slide that fails silently
3. Report only if a slide required significant structural redesign

### A5. Output + export
1. Save to `presentations/[slug].md` (or user-specified path)
2. Verify `.marprc.yml` exists at the project root — create from template in `references/cli-guide.md` if missing
3. Show the relevant export commands from `references/cli-guide.md`

---

## Mode B: Edit

1. Read the existing `.md` file — parse slide boundaries (`---`)
2. Identify the target slide(s) from the request
3. Apply edits; re-check modified slides against `references/quality-rules.md`
4. Confirm layout rotation rule is not broken across surrounding slides

---

## Mode C: Theme

1. Ask: brand colors? target mood? dark or light base?
2. Build CSS using 60-30-10 color rule and WCAG AA contrast — see `references/themes.md`
3. Present **3 palette directions** before committing
4. Save theme CSS with `/* @theme name */` header comment (required for CLI recognition)

---

## Mode D: Convert

1. Parse input format (plain text, outline, bullet list, document)
2. Determine slide boundaries by topic/section shift, not by line breaks
3. Generate MARP `.md` applying Mode A generation rules
4. Run A4 QA self-review

---

## Mode E: Read

1. Load the `.md` file
2. Parse slides, speaker notes, and frontmatter
3. Return: slide count, theme used, key idea per slide, layout types, SlideGauge quality flags

---

## Closing Feedback Gate

After final output, ask once: "Did this produce what you needed? Any corrections or preferences I should remember?"

Route the response:
| User says | Destination |
|---|---|
| Behavioral ("don't do X", "I prefer Y") | Append to `references/learnings.md` |
| Factual exception ("the flag is actually Z") | Append to `references/edge-cases.md` |
| "Never do X again" | Add rule to this SKILL.md |
| Explicit approval / "this was perfect" | Save output to `examples/approved/` |
| No response / "looks good" | Do nothing |

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
