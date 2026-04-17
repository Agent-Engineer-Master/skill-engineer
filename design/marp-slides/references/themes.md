# MARP Themes Reference

## Table of contents
1. [Signal-to-theme mapping](#signal-to-theme-mapping)
2. [Dark starter template](#dark-starter-template)
3. [Light theme](#light-theme)
4. [Font pairings](#font-pairings)
5. [60-30-10 color rule](#60-30-10-color-rule)
6. [Heading hierarchy](#heading-hierarchy)
7. [CSS variables reference](#css-variables)

---

## Signal-to-theme mapping

Pick the closest match; default to dark/dashboard if unsure.

| Content signals | Recommended theme | Font pairing |
|---|---|---|
| data, metrics, dashboard, analytics, KPIs | dark/dashboard | Outfit 800 + Raleway 100 |
| executive summary, strategy, board deck | dark/minimal | Space Grotesk 700 + IBM Plex Mono 300 |
| product comparison, feature review | dark/comparison | Sora 700 + Sora 200 |
| editorial, lifestyle, food, culture | light/editorial | DM Serif Display + DM Sans 300 |
| tech, code, developer | light/technical | Space Grotesk 700 + IBM Plex Mono 300 |
| retro, team, internal | light/team | Plus Jakarta Sans 800 + Plus Jakarta Sans 200 |
| music, culture, Spotify-style | dark/culture | Urbanist 800 + Urbanist 100 |
| brand, marketing, campaign | dark/brand | use brand-guidelines.md accent color |

---

## Dark starter template (default)

```markdown
---
marp: true
theme: default
paginate: true
header: '![w:100](./logo.png)'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Raleway:wght@100;200;300&display=swap');

  :root {
    --accent: #ff6b1a; --accent-hover: #ff8c4a;
    --dark: #000; --card: #080808; --border: #111;
    --body: #999; --label: #666; --muted: #555; --light: #fff;
    --green: #22c55e; --red: #ef4444; --yellow: #f5a623;
  }
  section { background: var(--dark); color: var(--light); font-family: 'Raleway', sans-serif; font-weight: 200; padding: 56px 72px; }
  h1 { font-family: 'Outfit'; font-weight: 800; font-size: 3em; color: var(--light); }
  h2 { font-family: 'Raleway'; font-weight: 100; font-size: 1.3em; color: #888; }
  h3 { font-family: 'Outfit'; font-weight: 600; font-size: 0.6em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.2em; }
  strong { color: var(--accent); font-weight: 300; }
  section.lead { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
  header { text-align: right; } header img { margin: 0; }
  .row:hover { background: #0c0c0c; } .row { transition: background 0.2s; border-radius: 6px; }
  details { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 14px 18px; margin-top: 8px; }
  details summary { color: var(--accent); font-family: 'Outfit'; font-weight: 600; font-size: 0.8em; cursor: pointer; }
  details p { color: var(--body); font-size: 0.78em; margin-top: 8px; }
  .tag { font-family: 'Outfit'; font-weight: 600; font-size: 0.55em; letter-spacing: 0.12em; text-transform: uppercase; padding: 3px 10px; border-radius: 4px; }
  abbr { text-decoration: none; border-bottom: 1px dotted #333; cursor: help; }
---
```

To hide the header on a specific slide: `<!-- _header: '' -->`

---

## Light theme

Swap these variables into the dark template:

```css
--accent: #2563eb; --dark: #fafafa; --card: #fff;
--border: #eee; --body: #666; --label: #bbb; --light: #1a1a1a;
```

Recommended fonts: Space Grotesk 700 + IBM Plex Mono 300, or Plus Jakarta Sans 800 + Plus Jakarta Sans 200.

---

## Font pairings (tested)

| Heading | Body | Best for |
|---|---|---|
| Outfit 800 | Raleway 100 | Dashboard, data (default dark) |
| DM Serif Display | DM Sans 300 | Editorial, lifestyle, recipes |
| Space Grotesk 700 | IBM Plex Mono 300 | Travel, technical, light themes |
| Sora 700 | Sora 200 | Product comparisons |
| Urbanist 800 | Urbanist 100 | Music, Spotify-style |
| Plus Jakarta Sans 800 | Plus Jakarta Sans 200 | Retros, team decks |

---

## 60-30-10 color rule

Every theme palette should follow this ratio:
- **60%** — dominant neutral (background + large surfaces)
- **30%** — secondary color (cards, borders, secondary text)
- **10%** — accent (CTAs, highlights, key data points, bold text)

This ratio applies to visual weight, not literal pixel count. A single bright accent number in a field of gray follows the rule. Using accent for more than ~10% of visible elements dilutes its impact.

**WCAG AA contrast requirement:** Body text must achieve 4.5:1 contrast ratio against the slide background. `#999` on `#000` = 5.9:1 (passes). `#666` on `#fff` = 5.7:1 (passes).

---

## Heading hierarchy

| Level | Role | Style |
|---|---|---|
| h1 | Title slides only — full-bleed hero | white, extra-large, Outfit 800 |
| h2 | Main slide title — one per slide | white or light, Raleway 100 |
| h3 | Section label / category tag | muted (#555), uppercase, small, tracked |

Never stack h1 + h2 + h3 on the same slide. Use at most two heading levels per slide.

---

## CSS variables

| Variable | Default (dark) | Purpose |
|---|---|---|
| `--accent` | `#ff6b1a` | Primary brand / highlight |
| `--accent-hover` | `#ff8c4a` | Hover state for interactive elements |
| `--dark` | `#000` | Slide background |
| `--card` | `#080808` | Card / panel background |
| `--border` | `#111` | Card border, dividers |
| `--body` | `#999` | Body text |
| `--label` | `#666` | Secondary labels |
| `--muted` | `#555` | Tertiary / suppressed text |
| `--light` | `#fff` | Primary text on dark |
| `--green` | `#22c55e` | Positive / active status |
| `--red` | `#ef4444` | Negative / error status |
| `--yellow` | `#f5a623` | Warning / review status |

Per-slide overrides: `<!-- _backgroundColor: #0a0a0a -->`, `<!-- _header: '' -->`, `<!-- _paginate: false -->`

Custom portrait dimensions: use `section { width: 540px; height: 720px; }` in CSS — not `size:` frontmatter.
