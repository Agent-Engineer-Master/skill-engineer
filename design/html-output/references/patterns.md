# Output patterns — when to use which archetype

Pick one starting template per file. Blending two archetypes (e.g. "dashboard + report") makes both worse — embed the secondary as a section inside the dominant one.

## Dashboard
**Signal:** "show me the state", "give me a status overview", "build a dashboard", multiple KPIs across workstreams.
**Structure:** Top hero with overall status • 3–6 KPI tiles in a grid • optional trend mini-charts • a status table beneath.
**Density target:** Reader gets the headline in 5 seconds.

## Report
**Signal:** "write me a research report", "render this analysis", "long-form brief".
**Structure:** Eyebrow + title + dek • table of contents • 3–6 numbered sections, each with optional pull-quote • appendix with sources.
**Density target:** Reads like a McKinsey/Bain brief — scannable but substantive.

## Comparison table
**Signal:** "compare options", "vendor evaluation", "decision matrix", side-by-side feature lists.
**Structure:** Criteria column on left • options as columns • cells use ✓/✗/partial pills or 1–5 scores • bottom row with overall scores + recommendation.
**Density target:** Reader can pick a winner without reading body copy.

## Mermaid diagram
**Signal:** "draw the flow", "show the process", "sequence diagram", "mind map".
**Structure:** Title + one-paragraph context • one main Mermaid block • legend / key beneath.
**Type cheat sheet:**
- `flowchart TD` (top-down) for processes
- `sequenceDiagram` for interactions over time
- `stateDiagram-v2` for state machines
- `mindmap` for concept trees
- `gantt` for project timelines
- `journey` for user journeys

## SVG diagram
**Signal:** Hand-crafted layout Mermaid cannot express — layered architecture, spatial map, custom illustration.
**Structure:** Title + context • one main `<svg>` with a viewBox • labelled regions with `<text>` elements inside.
**Style:** Use brand colors via `fill="#1E3A2F"` etc. or `class="..."` with CSS. Stroke weight 2px, rounded line caps.

## Timeline
**Signal:** "roadmap", "history", "what happened when", "milestones".
**Structure:** Vertical or horizontal timeline • dated events as cards • optional phase bands (Q1, Q2…) as background colors.

## Data explainer
**Signal:** "explain this chart", "one number, one story", a single hero metric supported by narrative.
**Structure:** Eyebrow + headline number (huge) • one-sentence interpretation • Chart.js chart • 2–3 paragraphs of context • methodology footnote.

## Universal rules across all archetypes
- **Hero element first**: every artifact opens with the single thing the reader most needs to know.
- **One typeface hierarchy**: Space Grotesk for headings + labels, Inter for everything else.
- **Don't fill the canvas**: white space is the brand. Use the `.container` class (max 1100px).
- **Always include the export footer** at the bottom: copy-as-JSON, copy-as-markdown, print.
- **No images unless essential**: prefer inline SVG icons. If a raster image is needed and under 200KB, base64 it.
