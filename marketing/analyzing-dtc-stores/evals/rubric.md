# Evaluation Rubric — DTC Teardown

Subjective scoring. 8 dimensions, each scored 1–3. Based on librarian research across 15 publicly available teardowns (Sacra, 2PM, Hahnbeck, Drivepoint, Particl). A mediocre teardown must score 1–2 on at least two dimensions; if the rubric rewards everything, it is broken.

**Minimum pass bar:** Score ≥3 on dimensions 1 (Evidence rigor), 2 (Source diversity), and 6 (Verdict sharpness) regardless of total. Failing any of these three = structural failure, not a quality issue.

Structural completeness (all 16 sections present, sources non-empty, ImportYeti cited) is NOT a rubric dimension — it is handled by `evals.json` assertions and `validate_report.py`.

---

## Dimension 1 — Evidence rigor

Are numeric claims cited or clearly marked as estimates with method shown?

- **1** — Multiple numbers stated without source or estimate marker. Revenue, CAC, or margins asserted as fact with no trace.
- **2** — Most numbers cited, but at least one analytical section has unsourced or undefended figures.
- **3** — Every numeric claim is either [N]-cited to an external source or prefixed `~ (est., method: …)` with the math visible.

## Dimension 2 — Source diversity

How many independent sources, how varied?

- **1** — Fewer than 5 sources, or >50% of sources are brand-owned (about page, press releases, founder interviews).
- **2** — 5–9 sources, mostly third-party but missing at least one of: ImportYeti, Meta Ad Library, independent review aggregator.
- **3** — 10+ sources spanning at least 6 categories: store, third-party market, competitor discovery, supply chain (ImportYeti), ads (Meta Ad Library), reviews, tech stack, financial comps.

## Dimension 3 — Competitive insight

Is the strategic group articulated, not just listed?

- **1** — Competitor list only, no positioning logic. Or competitor set is taken from the brand's own "vs" page.
- **2** — Competitor table with price/positioning columns, but no articulated "what game is being played."
- **3** — Strategic group explicitly named. Independently discovered (search intent + category overlap). Identifies the adjacent-category threat the brand hasn't noticed.

## Dimension 4 — Unit economics realism

Does the math hold up, with assumptions stated?

- **1** — Gross margin only, no CM2/CM3 waterfall. Or "healthy margins" with no number.
- **2** — CM1 and CM2 shown with assumptions, but CM3/CAC/payback glossed over.
- **3** — Full CM1 → CM2 → CM3 waterfall. CAC is new-customer not blended. Apparel brands properly penalised for return-rate collapse. Internal consistency check against stated revenue and headcount.

## Dimension 5 — Supply chain depth

Forensics or speculation?

- **1** — Generic statements ("likely manufactured overseas") with no source.
- **2** — At least one independent data point (FDA, label photo, LinkedIn employee title).
- **3** — ImportYeti findings with named suppliers, country concentration, and explicit manufacturer-direct risk assessment. Or, if ImportYeti has no records, the fact is cited and alternative forensics (labels, LinkedIn, job ads) substitute.

## Dimension 6 — Verdict sharpness

Does the verdict take a position with a "what would change my mind"?

- **1** — Hedged verdict ("interesting brand, execution risk at scale"). No numerical anchor. No falsifiability.
- **2** — Clear bull/bear cases, but "change my mind" is qualitative or missing.
- **3** — Falsifiable verdict with at least one numerical anchor ("investable below $X valuation") AND a specific condition that would flip the verdict. Forces commitment.

## Dimension 7 — Tone discipline

Skeptical analyst voice, no hype?

- **1** — Any banned hype word (`revolutionary`, `disruptive`, `game-changing`, etc.). Or >3 analytical claims that could be sourced from the brand's own About page in a 2,000-word report.
- **2** — No hype words, but the voice drifts into marketing restatement in some sections.
- **3** — Senior analyst voice throughout. Skeptical but fair. Zero unverified brand-claim restatements in analytical sections.

## Dimension 8 — Insight density

Surprising / non-obvious observations vs restatements?

- **1** — Report could have been written from the brand's homepage alone. No "I wouldn't have noticed that without this memo" moments.
- **2** — At least one non-obvious observation per major section (5+ total).
- **3** — Consistent surprise. The reader finishes understanding 2–3 things they'd never have seen by clicking around the site. Examples: the ImportYeti finding, the creative-fatigue pattern, the manufacturer-direct threat, the JSON-LD gap.

---

## Scoring

- **22–24** — publication-grade, could run in 2PM or Sacra
- **18–21** — solid investor memo, suitable for internal use
- **14–17** — draft needs sharpening on 2–3 dimensions before sharing
- **<14** — structural issues; re-run with better sources

Any score <3 on dimensions 1, 2, or 6 = structural failure, not a quality issue. Re-run required regardless of total.
