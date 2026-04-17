# MARP CLI Guide

## Table of contents
1. [.marprc.yml — project config (required)](#marprc)
2. [Export commands](#export-commands)
3. [Obsidian preview](#obsidian-preview)
4. [Known failure modes and fixes](#failure-modes)
5. [GitHub Actions CI/CD](#github-actions)

---

## .marprc.yml — project config (required)

Create at the project root. Without this file, every export needs manual flags and behavior varies unpredictably.

```yaml
# .marprc.yml
allow-local-files: true
html: true
theme-set:
  - ./themes/
```

**Why `allow-local-files: true` is non-negotiable:** Without it, all local image references (`./logo.png`, `./photo.jpg`) are silently absent in PDF and PPTX exports — no error, no warning, just blank image slots. This is the most common AI-generated MARP bug.

Save this template at project root any time a `.marprc.yml` is missing. Confirm with `marp --version` before generating.

---

## Export commands

```bash
# PDF (requires Chrome/Chromium)
marp slides.md --pdf --allow-local-files -o slides.pdf

# HTML (self-contained, animations and interactive elements work)
marp slides.md --html --allow-local-files -o slides.html

# PPTX (image-based, pixel-perfect layout)
marp slides.md --pptx --allow-local-files -o slides.pptx

# PPTX editable mode (v3.4+ stable, but text boxes may be narrow)
marp slides.md --pptx --pptx-editable --allow-local-files -o slides.pptx

# Watch mode (auto-recompile on save)
marp --watch slides.md

# Per-slide PNG images
marp --images png slides.md

# Input directory (batch)
marp --input-dir ./decks/ --output ./output/
# Warning: do NOT combine --input-dir with a filename --output — output becomes a directory
```

**Current stable version:** v3.4.1 (April 2026). CSS slide transitions available in v2+ CLI.

---

## Obsidian preview

Plugin: `obsidian-marp-slides` by samuele-cozzi (v0.46.1, April 2026). Install via Community Plugins.

Obsidian preview auto-reloads on save — iterate here before exporting. HTML mode shows animations. PDF export via `marp --pdf` is more reliable than the plugin's built-in export for production use.

---

## Known failure modes and fixes

| Failure | Symptom | Fix |
|---|---|---|
| Missing `--allow-local-files` | Images blank in PDF/PPTX, no error message | Add to `.marprc.yml` or pass flag explicitly |
| `--input-dir` + `--output filename` | Output written as directory, not file | Use `--output-dir` or don't specify output filename with `--input-dir` |
| Missing `/* @theme name */` comment | Custom theme not recognised by CLI | Add comment as first line of CSS file |
| SVG background in `cover` mode | Charts and visuals cropped at slide edges | Always use `contain` for SVG/data backgrounds |
| `*` bullets in source | Animation triggers in live HTML preview; invisible in PDF | Replace all `*` list items with `-` |
| Titles >35 characters | Title wraps or overflows slide bounds | Compress to ≤35 chars |
| `--pptx-editable` narrow text boxes | Text wraps/overlaps in LibreOffice/PowerPoint | Use python-pptx post-processing to widen boxes, or use standard `--pptx` mode |
| Google Fonts not loading | Fonts fall back to system fonts in PDF | Use `--allow-local-files` and serve fonts locally, or accept fallback in PDF mode |

---

## GitHub Actions CI/CD

Standard pattern for version-controlled decks:

```yaml
# .github/workflows/marp.yml
name: Build slides
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: marp-team/marp-cli-action@v2
        with:
          args: slides.md --pdf --allow-local-files -o output/slides.pdf
      - uses: actions/upload-artifact@v4
        with:
          name: slides
          path: output/
```
