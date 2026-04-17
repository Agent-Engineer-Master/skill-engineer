# Learnings — MARP Slides

Behavioral patterns and preferences accumulated from real runs. Read at startup; summarize the 3 most relevant bullets for the current task.

Consolidate at 80 lines. Hard cap: 100 lines. When an entry is reinforced 2+ times, promote to a rule in SKILL.md.

---

## What Has Worked

- Reading 2–3 example decks before generating consistently produces better composition and visual rhythm than generating from the theme template alone
- The 4-question intake (topic/count/theme/brand) prevents the most common wasted cycle: generating a full deck and then being asked to change the style
- SVG charts inline (not as image embeds) produce cleaner rendering across both Obsidian preview and PDF export
- Light/dark slide switching via CSS classes (`section.light`) is cleaner than per-slide background overrides — apply `<!-- _class: light -->` to each light slide
- Outfit 800 + Raleway 200 is a confirmed working font pairing for personal brand carousels — Outfit for headlines, Raleway for body
- `npx @marp-team/marp-cli` is the correct invocation on this system — `marp` command alone is not found

## What Has Failed

- Generating without an outline approval step often results in decks with inconsistent narrative flow — the user expects a story arc, not just slides about the topic
- Using `*` bullets instead of `-` hyphens silently breaks animation behavior in live preview mode (user confusion when demoing)
- Putting too much text on slides and too little in speaker notes — the default tendency is to over-write slides
- `justify-content: center` on any slide (cover, CTA, or otherwise) anchors content at mid-canvas — if content is tall, the bottom half overflows and is clipped. Use `justify-content: flex-start` for ALL slide classes and control vertical rhythm with margins instead. This applies to `section.cover`, `section.cta`, and any other class overrides — never use `center` on a slide that has more than a single centered element
- When all slides share a dark `section` base and only some slides should be light, forgetting to add `<!-- _class: light -->` to each light slide silently renders them dark — check every slide's class after any global CSS change
- Using `height:100%` wrapper divs inside a flex column causes overflow past the slide boundary — use `flex:1` or explicit pixel heights instead

## Patterns and Preferences

- Personal brand carousels (Antony Evans): dark Forest Green `#1E3A2F` for cover/level7/CTA slides, Off-White `#F4F1EB` for content (level) slides. Cover and level 7 always dark.
- Progress bar pattern: 7 narrow `height:3px` flex divs across the full width, with `gap:9px`. On light slides: active = `#1E3A2F`, inactive = `#E0D8C8`. On dark slides: active = `#E8A838`, inactive = `rgba(255,255,255,0.1)`. CTA slide uses all-amber at `opacity:0.25` (journey complete, faded).
- All slides should have `margin-top:16px` on the progress bar div so it sits just inside the top padding — keeps vertical rhythm consistent across light and dark slides
- CTA/cover slides: use `justify-content: flex-start` not `center`. Progress bar + content will naturally fill the top half, leaving breathing room at the bottom — this is correct.
- `section.cover`, `section.cta`, `section.light` are the three slide class variants. Don't add more without a clear reason.
- Inline `<!-- _class: cover -->` + `<!-- _class: cta -->` directives let specific slides override the default dark base without touching the base CSS

## Open Questions

- How to best handle brand decks when brand-guidelines.md specifies colors that conflict with WCAG AA contrast requirements?
- Should the outline approval step show slide-level detail (title + layout type) or just section headers?
