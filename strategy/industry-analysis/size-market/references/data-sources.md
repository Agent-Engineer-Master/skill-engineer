# Data Sources — Canonical List for Market Sizing

Where to find sizing inputs, ranked by evidence weight (drives V/C/A/I tagging).

## Tier 1 — Primary / Validated (`[V]`)

Strongest evidence. Used directly without intermediation.

| Source | Coverage | Cost | Notes |
|--------|---------|------|-------|
| SEC EDGAR | All US-listed company filings | Free | 10-K segment disclosures = best public revenue split |
| EU Transparency Register / Companies House | EU + UK filings | Free | |
| FDA UDI / EUDAMED | Medtech device universe | Free | Authoritative device counts |
| FERC / EIA | US energy + utilities | Free | |
| US Census, BLS | Industry economic data (NAICS-level) | Free | Slow (1-2yr lag) but authoritative |
| Eurostat, ONS | EU + UK economic data | Free | Same speed caveat |
| WHO, OECD, World Bank | Cross-country health, economic | Free | |
| Industry trade bodies | Industry-specific units + revenue | Often free | IFR (robotics), SEMI (semis), IATA (aviation), BIO (biotech), RILA (retail), EIA (energy), AHA (hospitals) |

## Tier 2 — Syndicated paid research (`[C]` if ≥2; `[A]` if single)

Standard PE-CDD input. Tag with report name + year + section.

| Source | Best for | Notes |
|--------|---------|-------|
| IBISWorld | US + AU industry reports, competitor lists | $$ — strong for sub-industry depth |
| Statista | Cross-sector market data aggregation | $$ — verify underlying source |
| Frost & Sullivan | Tech, healthcare, industrial | $$$ |
| Euromonitor | Consumer markets, global | $$$ |
| Gartner / IDC / Forrester | Tech markets (software, hardware, IT services) | $$$ |
| Mordor Intelligence, MarketsAndMarkets, Grand View Research | Broad coverage | $$ — varying quality; cross-check |
| L.E.K. / Bain / McKinsey published insights | Sector POVs | Free public; full paywall for engagement |

## Tier 3 — Sell-side analyst notes (`[C]` if ≥2 corroborating; `[A]` if single)

Aggregator-mediated. Cite the underlying analyst, note the aggregator.

| Source | Coverage |
|--------|---------|
| Bernstein, Morgan Stanley, JPM, Jefferies, Goldman | Sector teams publish sizing periodically |
| Aggregators | AlphaSense, Tegus, Sentieo, Visible Alpha — search interface for the above |

**Tagging convention:** `[C: Bernstein European Industrials 2025-Q3 + Morgan Stanley Robotics Outlook 2026-Q1, via AlphaSense]`

## Tier 4 — Expert networks (`[A]` typically; `[C]` if ≥2 experts agree)

GLG, Tegus expert calls, Guidepoint, Third Bridge. Useful for granular sub-segment color and emerging-market sizing where syndicated data is thin.

**Tagging convention:** `[A: GLG expert call, former [Company] [Role], 2026-MM-DD]`

## Tier 5 — AI aggregators — NEVER cite as primary

Perplexity Finance, ChatGPT, Claude, Bard, Gemini. These re-state underlying sources without provenance — citing them is the 2026-era equivalent of citing Wikipedia for a market figure.

**Rule:** use AI aggregators to *discover* sources, then read and cite the source directly. The validator flags citations of these aggregators without an accompanying underlying source.

## Alternative data (2026-era addition)

Worth knowing about but rarely load-bearing for sizing:

- **Web scrape volumes** — SimilarWeb, SEMrush for digital markets.
- **Card-spend panels** — Yodlee, Earnest, Facteus for consumer DTC.
- **Job postings** — LinkedIn, Indeed, Revelio Labs as growth proxies.
- **Patent filings** — USPTO, Google Patents as innovation-velocity proxies.
- **Shipping data** — Panjiva, ImportGenius for cross-border physical goods.

Tag as `[C: AltData source name + window]` when used as triangulation evidence.

## Decision tree — which source for which question

| Question | First-choice source |
|---------|---------------------|
| Total US industry revenue, current year | Trade body or IBISWorld |
| Industry growth rate, 5yr forward | Sell-side analyst note (forward) + cross-check with trade body (trailing) |
| Sub-segment cut | Sell-side note or specialist syndicated (Frost, Gartner) |
| Customer counts | Census/BLS (count) + trade body (qualification) |
| Top-5 share | IBISWorld competitor profile or Bernstein/MS sector note |
| Top-5 share movement (5yr) | Bernstein/MS sector note (they track this explicitly) |
| Pricing | Trade body, public price lists, expert call |
| Penetration rate | Specialist syndicated (Gartner for tech, Euromonitor for consumer) |

## Stale-data threshold

A source dated more than 24 months before the analysis year is **stale by default**. Use only with explicit "still current" justification (e.g., "structurally unchanged sub-segment; trade-body 2023 data extrapolated by trailing CAGR"). Validator flags pre-2024 sources for 2026 analyses.
