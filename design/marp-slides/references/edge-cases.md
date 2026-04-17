# Edge Cases — MARP Slides

Factual exceptions and environment-specific quirks discovered during real runs. Distinct from learnings (behavioral patterns) — these are specific technical facts.

Format: `- [exception] — [YYYY-MM-DD or context]`

---

- Obsidian preview (obsidian-marp-slides plugin) does not render `<details>` collapsible elements — they appear as raw HTML. Works correctly in exported HTML and browser preview. — 2026-04-11
- `marp --pdf` requires Chrome or Chromium to be installed. On WSL without a browser, export fails silently with exit code 1. Use `marp --html` as fallback, then print-to-PDF from browser. — 2026-04-11
- Google Fonts imports (`@import url(...)`) do not load in PDF export mode — MARP runs headless and may not have network access. Fonts fall back to system sans-serif. Acceptable for internal decks; for client-facing, bundle fonts locally. — 2026-04-11
- `--pptx-editable` mode (v3.4+) generates editable text boxes but they are often too narrow in LibreOffice. Standard `--pptx` mode (image-based) is pixel-perfect and preferred for final delivery. — 2026-04-11
