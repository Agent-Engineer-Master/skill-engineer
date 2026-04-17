# MARP Quality Rules — SlideGauge Checklist

SlideGauge is the community standard for scoring AI-generated MARP decks. Score thresholds: 90+ excellent, 80–89 good, 70–79 passing, <70 failing.

Run this checklist against every generated slide during A4 QA self-review. Fix failures silently.

---

## Per-slide hard limits

| Rule | Limit | Failure |
|---|---|---|
| Bullets per slide | ≤6 | Overflow clips silently in MARP — reader can't see cut content |
| Title length | ≤35 characters | Longer titles wrap or truncate |
| Content per slide | ≤350 characters (body text only, excluding HTML) | Information overload |
| Code block | ≤10 lines | Longer blocks require font scaling that breaks layout |
| Layout repeat | ≤2 in a row | Same template 3× = visual fatigue |
| Heading levels per slide | ≤2 | Stacking h1+h2+h3 creates hierarchy confusion |

---

## Deck-level rules

- Every slide must have at least one non-text visual element (image, SVG, code block, styled card, or icon)
- Layout must rotate — no single layout type used for 3+ consecutive slides
- Breadcrumb headers or section context must be present on all non-title slides
- Speaker notes must be non-empty on all content slides
- Accent color used for ≤10% of visible elements per slide (60-30-10 rule)

---

## Content quality rules

| Bad pattern | Fix |
|---|---|
| Bullets starting with `*` | Replace with `-` — asterisks trigger animation mode in live preview |
| Slide titles as full sentences | Compress to ≤35 chars, headline style |
| Context dumped on slides | Move to speaker notes |
| Decorative accent line directly under title | Remove — telltale AI pattern, clutters hierarchy |
| Same insight stated in title AND bullets | Remove the bullet — title carries it |
| Generic title ("Overview", "Introduction") | Rewrite as an insight headline |

---

## Technical correctness rules

| Rule | Why |
|---|---|
| Use `-` for list items, never `*` | `*` triggers animation in Marp live mode; invisible in PDF but breaks HTML preview |
| Relative paths for all local images (`./img.png`) | Absolute paths break in Obsidian preview |
| SVG image backgrounds: use `contain` mode | `cover` crops charts and data visuals at slide edges |
| `--allow-local-files` required for PDF/PPTX with local images | Missing flag = silently absent images in exports |
| CSS theme files must start with `/* @theme name */` | Missing comment = theme not recognised by CLI |

---

## Word-count-to-slide-count heuristic

| Input word count | Suggested slides |
|---|---|
| <500 words | 5–8 |
| 500–1000 words | 8–12 |
| 1000–2000 words | 12–18 |
| >2000 words | 18–25 (consider splitting into multiple decks) |

---

## WCAG AA contrast minimums

| Element | Minimum contrast ratio |
|---|---|
| Body text (small) | 4.5:1 |
| Large text / headings | 3:1 |
| UI components, icons | 3:1 |

Quick checks:
- `#999` on `#000` = 5.9:1 ✓
- `#666` on `#000` = 3.9:1 ✗ (fails for small text — use `#888` minimum)
- `#666` on `#fff` = 5.7:1 ✓
- `#bbb` on `#fff` = 2.3:1 ✗ (fails — use `#888` minimum on white)
