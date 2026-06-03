---
name: html-output
description: Renders complex information as a single self-contained HTML file — dashboards, analytical reports, comparison tables, timelines, flow/sequence diagrams, and data explainers — using Antony Evans's brand tokens (forest green / off-white / amber, Space Grotesk + Inter). Triggers on "build/render/make this as HTML", "create a dashboard", "show me a visual report", "turn this into a one-pager", "render with diagrams", or when another skill says "use html-output for the deliverable". Also activates when the artifact has 3+ dimensions of data, needs diagrams or interactive export buttons, or would be clearly more legible in a browser than in markdown. Does NOT trigger for short chat replies, markdown notes for the Obsidian vault, code files, slide decks (use pptx), spreadsheets (use xlsx), PDFs (use pdf), logos or images (use generate-image), or plain text answers. Output is one styled .html file with optional Mermaid or Chart.js via CDN when justified.
---

# HTML Output

Produce a single self-contained `.html` file as the deliverable when complex information would be clearer in a browser than in markdown. Designed to be invoked directly by a human (`/html-output`) or as a styling/format layer by another skill that needs to ship an HTML artifact.

## When to use HTML over markdown

Use HTML when ANY of the following is true:
- The information has ≥3 dimensions that benefit from spatial layout (dashboards, comparison matrices, decision tables).
- The deliverable includes a diagram (flowchart, sequence, tree, timeline, architecture map).
- The reader will want to **copy, export, print, or filter** sections.
- The output is a one-off shareable artifact (report, brief, explainer) — not a doc that lives in the vault.
- Another skill explicitly hands off to this one.

Otherwise, stay in markdown.

## Process

### 1. Classify the request into an archetype
Pick exactly one starting template from `assets/templates/`:

| Archetype | Template | When |
|-----------|----------|------|
| Dashboard | `dashboard.html` | KPIs + multi-panel status (3+ metric tiles) |
| Report | `report.html` | Long-form analysis with sections, pull quotes, charts |
| Comparison | `comparison-table.html` | Side-by-side options, scoring matrices, vendor evaluation |
| Mermaid diagram | `diagram-mermaid.html` | Flowcharts, sequence diagrams, state machines, mind maps |
| SVG diagram | `diagram-svg.html` | Custom diagrams Mermaid cannot express, hand-crafted layouts |
| Timeline | `timeline.html` | Chronological events, roadmaps, project history |
| Data explainer | `data-explainer.html` | One chart + narrative — Chart.js-driven story |
| Consulting deck | `slide-deck.html` | McKinsey/BCG-style 16:9 slides with action titles, exhibit chrome, 2×2 / waterfall / MECE layouts |

If the request blends two archetypes (e.g. dashboard + diagram), pick the dominant one and embed the secondary as a section.

**For consulting decks specifically:** also read `references/consulting-patterns.md` — action titles, MECE structure, chart archetypes (2×2, waterfall, Marimekko), exhibit-numbering rules.

### 2. Load the brand tokens and decide the mode
- **Always read** `references/brand-tokens.md` and inline its `<style>` block in the `<head>`. Brand consistency is non-negotiable — never substitute generic colors.
- **Decide self-contained vs CDN mode** using `references/libraries.md`:
  - *Self-contained mode* (default): pure HTML/CSS/SVG, no network calls. Use when the artifact must travel (email attachment, archive, air-gapped review).
  - *CDN mode*: load Mermaid and/or Chart.js from CDN. Use only when the diagram/chart genuinely needs it AND the reader will open in a connected browser.
- The reasoning principle: portability beats prettiness. When in doubt, self-contained.

### 3. Render the file
- Single `.html` file, complete and standalone. No external CSS, no `<link>` to local files.
- `<head>` includes: charset, viewport, title, brand `<style>` block, optional CDN `<script>` tags, optional `<script type="application/json">` data block.
- `<body>` follows the chosen template's structure. Adapt copy and data; do not rewrite the layout from scratch.
- Typography: load Inter and Space Grotesk via Google Fonts. Fall back to system fonts gracefully.
- Print-friendly: include `@media print` rules (already in `brand-tokens.md` snippet).

### 4. Always include an export footer
Per Anthropic's HTML guidance, every HTML artifact ends with an export affordance. Use the snippet in `assets/snippets/export-footer.html`. Minimum buttons:
- Copy as JSON (raw data block)
- Copy as markdown (text version of headings + key content)
- Print / Save as PDF

If the artifact has no extractable data (pure diagram), the print button alone is enough.

### 5. Save and report
- Default save location: where the calling skill or user specifies. If not specified and called by a routine, save to `00-inbox/html/YYYY-MM-DD-{slug}.html`.
- Report the file path and a one-line description of what was rendered.

## Calling this skill from another skill

A skill can invoke `html-output` for its final deliverable by:
1. Producing the content (data, sections, copy) in structured form.
2. Telling html-output: "Render this as a {archetype} using the html-output skill. Data: {...}".
3. html-output handles styling, brand tokens, template selection, and export footer.

The calling skill owns the *content*; html-output owns the *form*.

## Gotchas

- **Symptom:** Brand colors render but Inter/Space Grotesk fall back to system fonts. **Cause:** Google Fonts `@import` placed after other CSS rules, blocking the font swap. **Fix:** Put the `@import url(...)` line as the very first rule inside `<style>`, before `:root`.
- **Symptom:** Mermaid diagram shows raw code, not a rendered chart. **Cause:** Mermaid script loaded but `mermaid.initialize()` not called, or the diagram block uses `<pre><code class="language-mermaid">` instead of `<pre class="mermaid">`. **Fix:** Use `<pre class="mermaid">` and include `mermaid.initialize({ startOnLoad: true, theme: 'base', themeVariables: { primaryColor: '#1E3A2F', ... } });` from `assets/snippets/mermaid-cdn.html`.
- **Symptom:** Mermaid `timeline` block renders the "Syntax error in text" bomb icon. **Cause:** The timeline parser is fragile — em-dashes (`—`), parenthetical text containing commas (`(BestReviews, RTINGS)`), double-quotes inside event text, and `&amp;` HTML entities all trip it. **Fix:** Use plain ASCII in timeline event text. Replace em-dashes with periods or "to", spell out enumerations ("such as BestReviews and RTINGS"), drop quotes around branded terms, and write `and` instead of `&`. Other Mermaid diagram types (flowchart, sequence, etc.) tolerate these characters — the rule applies specifically to `timeline`.
- **Symptom:** Mermaid `timeline` title renders nearly invisible (off-white-on-off-white) under the brand theme. **Cause:** When `primaryTextColor` is set to the off-white brand bg for text-inside-primary-boxes, Mermaid uses the same variable for the timeline title, which sits on the off-white page background. **Fix:** Add `titleColor: '#1E3A2F'` and `textColor: '#1E3A2F'` to `themeVariables` alongside `primaryTextColor`, AND add a CSS override targeting the SVG: `pre.mermaid svg .titleText, pre.mermaid svg text.titleText { fill: var(--brand-primary) !important; font-weight: 700 !important; }`. Both are needed — the theme variable handles most renders, the CSS catches version-specific class names.
- **Symptom:** File opens in browser but copy-as-JSON button does nothing. **Cause:** Inline `onclick` handler references a function defined later in the file with `defer`. **Fix:** Define export helpers at the top of the `<script>` block, or wrap in `DOMContentLoaded`.
- **Symptom:** Self-contained file balloons to 5MB+ because a base64 image was embedded. **Cause:** Used base64 for a large raster image instead of an SVG or external image. **Fix:** Use inline SVG for diagrams/icons. For raster, keep under 200KB or use an external `https://` URL and accept the network dependency.
- **Symptom:** Amber `#E8A838` used as body-text color and fails WCAG. **Cause:** Amber is for CTAs/highlights only — it has ~3:1 contrast on off-white, fine for large UI elements but not for paragraphs. **Fix:** Use Forest Green or Slate for any text under 18px.

## Rules

- Always inline brand tokens — never substitute generic colors.
- Always single-file output — no external CSS/JS files in the same folder.
- Always end with an export footer (copy/print buttons).
- Never use `<link rel="stylesheet">` to a local file; use a `<style>` block.
- Never use banned brand words from `references/brand-tokens.md` in headings or body copy when content is human-facing.
- Prefer inline SVG over base64 images for diagrams and icons.
- When in doubt between self-contained and CDN mode, choose self-contained.
- One template per file — do not blend dashboard.html and report.html structures; pick one and adapt.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
