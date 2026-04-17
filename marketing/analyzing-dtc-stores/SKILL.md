---
name: analyzing-dtc-stores
description: "Use when the user provides a DTC or ecommerce store URL and asks for a teardown, breakdown, brand analysis, competitor teardown, investor memo, store audit, deep dive, or 'what's going on with [brand]'. Produces an investor-grade markdown teardown report covering brand, market, unit economics, supply chain, channel mix, marketing, reviews, agentic-commerce readiness, risks, and a falsifiable verdict. Triggers: 'dtc teardown', 'brand teardown', 'store teardown', 'competitor teardown', 'analyze this store', 'investor memo on [brand]', 'break down [store url]'. Do NOT use for SEO-only audits, design-system extraction, lead-gen scraping, or general web scraping with no brand/investor focus."
---

# Analyzing DTC Stores

Produces an investor-grade teardown of a DTC brand from its public URL. Read-only — never writes to the store, sends email, or posts anywhere.

## Inputs

- **Required:** `store_url` — brand's primary storefront.
- **Optional:** `depth` — `quick` | `standard` (default) | `deep`.
- **Optional:** `focus` — free-text bias (e.g. "supply chain", "acquisition target fit").
- **Optional:** `--no-save` — return the report inline and skip saving.

## Process

### Step 1 — Intake

1. Parse `store_url`, `depth`, `focus`, `--no-save`.
2. Derive `brand_slug` from the domain (e.g. `brandname.com` → `brand-name`).
3. Copy `assets/report-template.md` to a working draft. Do not save to the final path yet.

### Step 2 — Recon sweep (scripted)

Run `scripts/recon.py --url <store_url>` to fetch homepage, robots.txt, sitemap, JSON-LD, and detect platform + apps (Shopify/Klaviyo/Gorgias/Recharge/Triple Whale signatures). Output cached in `.cache/recon-[slug].json`. Feeds the Tech Stack and Agentic Readiness sections.

### Step 3 — Fan-out research (scripted + reasoning)

Load `references/sources-playbook.md` — required reading, it maps each report section to prescribed sources.

Run every applicable script. Fail gracefully: if a source is unreachable, log `[source unavailable]` in the report's Sources section and continue — never halt.

**Mandatory scripts (all depths):**
- `scripts/meta_ad_library.py --brand <brand>` — active ad count, creative lifespan distribution.
- `scripts/importyeti_lookup.py --brand <brand>` — supplier + country-of-origin + shipment volume. **Mandatory — the #1 skipped source.**
- `scripts/similarweb_lookup.py --domain <domain>` — traffic with the 50K/mo accuracy floor flag.
- `scripts/store_leads_lookup.py --domain <domain>` — Shopify plan, app stack, revenue bracket.
- `scripts/reviews_scan.py --brand <brand> --domain <domain>` — Trustpilot + Amazon + YouTube review URLs.
- `scripts/reddit_search.py --brand <brand>` — Reddit sentiment via OpenAI web search (requires OPENAI_API_KEY). Returns structured JSON: thread_count, sentiment, top_praise_theme, top_complaint_theme. "0 threads" is a valid finding — log it in §10.

**Additional for `standard` and `deep`:**
- `scripts/amazon_bsr.py --brand <brand>` — BSR + est. monthly unit sales for top SKUs.

For the reasoning steps (brand story, competitive strategic group, verdict framing) use WebSearch + WebFetch directly.

### Step 4 — Unit economics

Read `references/unit-economics-benchmarks.md` for category COGS / CAC / LTV ranges. Run `scripts/unit_econ.py --category <cat> --aov <aov> --cac <cac>` to produce a CM1 → CM2 → CM3 waterfall. Every figure must carry stated assumptions and a `~ (est., method: …)` prefix.

### Step 5 — Draft the report

Fill the 16-section template in order. Principles:

- **Prefer "Insufficient public data" over speculation.** A 2-line section with the sources checked beats 8 lines of filler.
- **Cite inline** with `[1][2]` — the Sources section at the end is the numbered index.
- **Every numeric claim is either cited or prefixed `~` with method shown.** Non-negotiable.
- **Competitors must come from independent discovery**, not the brand's own "vs" page. If the brand lists competitors on its site, exclude them until resurfaced via search intent or category overlap.
- **Show the CM waterfall, not just gross margin.** Apparel especially — returns collapse CM2.
- **SimilarWeb under 50K/mo = directional only.** Quote a range, not a point estimate; triangulate with ad count + review velocity + headcount.

For `depth=deep`: after the draft, present three alternative verdict framings (bull, bear, contrarian) and let the user pick before finalising.

### Step 6 — Self-check (scripted, mandatory)

Run `scripts/validate_report.py --path <draft>`. The script fails loud with a remediation list if:

- Any of the 16 sections is missing or empty.
- Any numeric claim is unsourced and not prefixed `~`.
- The Sources section is empty or has fewer than 5 entries.
- The Verdict section lacks a numerical "what would change my mind" anchor.
- Any banned hype word appears (`revolutionary`, `disruptive`, `game-changing`, `cutting-edge`, `seamless`, `unparalleled`).
- The ImportYeti check is missing from the Sources section (even a "no records found" entry counts).

Fix every failure and re-run. Do not proceed to Step 7 until the validator exits 0.

### Step 7 — Save + return

Run `scripts/save_report.py --path <draft> --slug <brand_slug>` (honors `--no-save`). Returns the final path. Then output to chat: final path + a 5-bullet executive summary (≤120 words total).

### Step 8 — Closing feedback gate

Ask the user exactly once: *"Any corrections to this teardown before I log it?"*

Route the response:
- Behavioural feedback (tone, framing, depth preference) → append to `references/learnings.md`.
- Factual exception (platform quirk, blocked source) → append to `references/edge-cases.md`.
- "Never again" → add a rule to this SKILL.md.
- Approval with no changes → copy final report to `assets/approved-examples/`.

## Report structure (16 sections, exact order)

0. Research confidence & source map
1. Executive summary (5 bullets, ≤120 words)
2. Brand & positioning
3. Product & value proposition
4. Market & category (TAM/SAM, growth, tailwinds, regulatory)
5. Competitive landscape (5–10 competitors in a table; name the strategic group)
6. Pricing & unit economics (CM1/CM2/CM3 waterfall, CAC, payback — show the math)
7. Supply chain & sourcing (ImportYeti, FDA, LinkedIn, job ads)
8. Channel mix (DTC, Amazon, marketplaces, wholesale, international)
9. Marketing & traffic (Meta Ad Library, Similarweb, creative lifespan, SEO)
10. Customer voice & sentiment (review volumes, themes, NPS proxy)
11. Tech stack
12. Agentic / AI readiness (JSON-LD density, agentic storefront signals, checkout friction)
13. Risks & red flags (incl. manufacturer-direct threat, tariff exposure)
14. Financial summary & valuation (EV/Sales comps, buyer-type implications)
15. Investor verdict (bull case, bear case, numerical "change my mind" anchor)
16. Sources (numbered, with access dates)

Style: crisp, evidence-led, numerate, slightly sceptical. Voice of a senior analyst writing for a partner with 10 minutes. Length: 1,500–3,000 words for `standard`.

## Gotchas

- **Symptom:** report states "$X ARR" without a source. **Cause:** triangulation mistaken for fact. **Fix:** every revenue figure cites a filing/interview/press release, or prefix `~ (est., method: …)` and show the math.
- **Symptom:** competitor list matches the brand's own "vs" page. **Cause:** used brand marketing as source of truth. **Fix:** build the competitor set from search intent + category overlap; exclude any competitor named on the brand's own site until independently surfaced.
- **Symptom:** unit economics cite gross margin only. **Cause:** stopped at CM1. **Fix:** always show the CM1 → CM2 → CM3 waterfall with stated assumptions; apparel especially — 24–30% return rates collapse CM2.
- **Symptom:** SimilarWeb precise visitor count for a small brand. **Cause:** ignored the 50K/mo accuracy floor. **Fix:** below 50K/mo, quote a range and label "directional only"; triangulate with ad count, review velocity, LinkedIn headcount.
- **Symptom:** no ImportYeti entry in Sources. **Cause:** forgot the mandatory check — the single most commonly skipped DTC source. **Fix:** Step 3 blocks until `importyeti_lookup.py` has run; a "no shipment records found" result still counts.
- **Symptom:** verdict hedges ("interesting brand, execution risk at scale"). **Cause:** analyst avoided commitment. **Fix:** verdict must contain a numerical anchor (e.g. "investable below $80M valuation") AND a "what would change my mind" line. Validator fails otherwise.
- **Symptom:** Meta-reported ROAS cited without qualification. **Cause:** ignored post-iOS14 attribution collapse. **Fix:** treat brand-reported Meta ROAS as directional; note the ATT caveat; prefer MER or incrementality-adjusted estimates.
- **Symptom:** blended CAC cited instead of new-customer CAC. **Cause:** blended metric flatters because returning-customer spend is in the denominator. **Fix:** separate the two; new-customer CAC is the scaling metric investors care about.

## Rules

- SKILL.md is the routing layer. Domain knowledge lives in `references/` — load on demand, don't embed.
- `references/sources-playbook.md` is required reading at Step 3. Not optional.
- `scripts/validate_report.py` is a hard gate at Step 6. Not optional.
- ImportYeti check is mandatory even on `quick` depth — a "no records found" entry is an acceptable result, silence is not.
- Never call this skill "complete" until the validator exits 0.
- Read-only always. Never POST to the store, send email, or publish.
- Banned hype words in output: `revolutionary`, `disruptive`, `game-changing`, `cutting-edge`, `seamless`, `unparalleled`.

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
