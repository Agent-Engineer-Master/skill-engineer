# Sources Playbook — section by section

Authoritative map from report section to data sources. Work through in order. For each source: if reachable, record findings + URL in the Sources section with access date. If unreachable or paywalled, still log the attempt — `[source: name, paywalled, not accessed, 2026-04-15]`.

## §0 Research confidence & source map

Not a research step — a transparency gate. Before writing any analytical section, fill the confidence preamble:
- Which sources were successfully accessed
- Which were attempted and failed (and why)
- Which data points are confirmed vs. triangulated vs. estimated
- 1-line self-assessment of overall confidence (high / medium / low)

A teardown with a "high confidence" label and no ImportYeti entry is structurally invalid. Validator checks this.

## §1 Executive summary

Derived last, not researched. Written after all other sections are drafted.

## §2 Brand & positioning

- Store's `/pages/about`, `/pages/our-story`, `/pages/founders`
- LinkedIn company page — founder bios, headcount, funding mentions
- YouTube — founder interviews, podcast appearances (My First Million, How I Built This, Lenny's, DTC Pod, Nik Sharma's Limited Supply)
- TechCrunch / Crunchbase free tier — funding rounds, founding date
- Press releases via Google News: `"[brand]" site:businesswire.com OR site:prnewswire.com`

## §3 Product & value proposition

- Store's `/collections/all` or `/products` — count SKUs, capture price ladder (low/median/high)
- Hero product = homepage hero + the SKU with the most reviews
- Jobs-to-be-done evidence: customer reviews, not brand's own copy

## §4 Market & category

- Statista, Grand View Research, Mordor Intelligence, IBISWorld — free abstracts only; do not fabricate numbers from paywalled pages
- Recent McKinsey / Bain / BCG consumer reports via Google Scholar or their insights hubs
- Google Trends for category search velocity
- **TAM must be bottom-up built** — number of addressable customers × AOV × purchase frequency. Top-down "$50B category" claims are the #1 market sizing failure mode.

## §5 Competitive landscape

- Google: `"alternatives to [brand]"`, `"[brand] vs"`, `"[brand] competitors"`
- Reddit: `site:reddit.com [brand] vs`
- Amazon: search the category, note brands with similar price points + review velocity
- **Explicitly exclude competitors the brand lists on its own site** until they resurface from independent search intent
- Name the strategic group: what competitive game is being played (e.g. "premium DTC supplements with physician endorsement") and who else is in it
- Build the comparison table: name | price band | positioning | channel mix | estimated scale

## §6 Pricing & unit economics

- Scrape the store for AOV components: price ladder, bundle discounts, subscribe-and-save discount %, free shipping threshold
- Infer COGS from `references/unit-economics-benchmarks.md` category table
- CAC estimation: Meta Ad Library active ad count × assumed CPM × assumed conversion rate. Show every assumption.
- **Always produce CM1/CM2/CM3.** Gross margin alone is analytically incomplete.
- Filed accounts: Companies House (UK), OpenCorporates, SEC EDGAR, state business filings
- Glassdoor for headcount proxy (revenue/employee ratio ≈ $400K–$800K for DTC)

## §7 Supply chain & sourcing (ImportYeti is MANDATORY)

- **ImportYeti** (free) — `importyeti.com/company/[brand]`. US customs records → suppliers, country of origin, shipment volume, frequency. 10 minutes. #1 skipped source in amateur teardowns.
- FDA import records for food / supplements / cosmetics
- Panjiva (freemium) — ImportYeti alternative
- LinkedIn employees with "supply chain", "sourcing", "operations" in title
- Brand's own job ads — "Supplier QA", "Manufacturing" roles reveal sourcing model
- Product label photos from Amazon listings — country of origin on the label
- **Score manufacturer-direct risk explicitly** if suppliers are identifiable and selling on TikTok Shop / Amazon directly.

## §8 Channel mix

- Own DTC: the store itself
- Amazon: search "[brand]" on amazon.com, check for brand registry storefront
- Faire: search the Faire marketplace
- TikTok Shop: search in the TikTok Shop tab
- Retail / wholesale: "Find us in store" / "Stockists" page; Google `"[brand]" site:wholefoodsmarket.com OR site:target.com OR site:sephora.com`
- International: country switcher + subdomain footprint
- **Presence ≠ revenue share.** A brand "available on Amazon" may do 5% or 60% there. Triangulate via Amazon BSR velocity vs. SimilarWeb DTC traffic.

## §9 Marketing & traffic

- **Meta Ad Library** (free, mandatory): https://www.facebook.com/ads/library — active ads, formats, creative lifespan. 90+ days = winner; 3 days = test.
- SimilarWeb free tier — monthly visits + source split. **Under 50K/mo = directional only**; quote a range.
- SEMrush / Ahrefs free preview — top organic keywords
- TikTok Creative Center — brand search for active creator content
- Google Ads Transparency Center — active paid ads
- Email/SMS: sign up, note cadence + sophistication
- **Do not cite brand-reported Meta ROAS without an iOS14-ATT caveat.**

## §10 Customer voice & sentiment

- Trustpilot — volume, average, top praise/complaint themes
- Amazon top reviews on the hero product
- Reddit: `site:reddit.com [brand] review`
- YouTube haul + review videos (sentiment proxy)
- Google reviews if the brand has retail presence
- **Review velocity** (new reviews per month) is a strong independent revenue signal — cross-check with SimilarWeb traffic.

## §11 Tech stack

- BuiltWith / Wappalyzer — platform, analytics, email, CRM, attribution, subscription
- View-source regex: Shopify (`cdn.shopify.com`), Klaviyo (`klaviyo.com/onsite`), Gorgias (`gorgias.chat`), Triple Whale, Recharge (`rechargepayments`), Skio, Northbeam
- `recon.py` handles most of this mechanically

## §12 Agentic / AI readiness

- JSON-LD structured data density (attributes per product)
- Presence of `llms.txt`
- Shopify Agentic Storefront default-on status (all eligible US Shopify merchants as of March 2026)
- Checkout friction — steps, guest checkout, Apple Pay / Shop Pay
- MCP / ACP / UCP signals

## §13 Risks & red flags

- Hero SKU concentration >60%
- Single supplier country (tariff exposure)
- Founder risk (single-founder + no ops depth)
- Review manipulation signals (sudden velocity spikes, generic language)
- Legal: `"[brand]" lawsuit` search, trademark disputes
- Manufacturer-direct competition threat (Chinese suppliers going DTC)
- Post-iOS14 CAC inflation if blended CAC is clearly degrading

## §14 Financial summary & valuation

- Comparable exits in category — Meridian IB, Hahnbeck, Admetrics multiples reports
- EV/Sales ranges: ~1.06x unprofitable DTC, ~1.84x profitable DTC, 2.83x median (2H 2024 data; update if newer)
- Buyer-type implications: individual acquirer (2–3.5x SDE), PE (5–8x EBITDA), strategic (10x+)
- State valuation range with explicit assumptions

## §15 Investor verdict

- Bull case (3 lines)
- Bear case (3 lines)
- "What would change my mind" — **must contain a numerical anchor** (e.g. "investable below $80M valuation; unattractive above $200M without demonstrated gross margin >55%")
- No score. Validator enforces the numerical anchor.
