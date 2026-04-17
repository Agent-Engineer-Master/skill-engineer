# Market Evidence Guide — Compliance Signal Strength

## Signal Strength Ranking

Ranked strongest to weakest. Stop searching once you have 🟢-level evidence.

| Rank | Signal | Strength | Notes |
|------|--------|----------|-------|
| 1 | Official compliance document linked (CPC PDF, FCC certificate, CoA) | ★★★★★ | Best possible evidence |
| 2 | Active listing on Amazon with explicit standard cited (e.g. "ASTM F963-23", "FCC Part 15") | ★★★★ | Amazon's marketplace enforcement implies documentation exists |
| 3 | FCC ID found on fccid.io for electronics | ★★★★ | Public government database — definitive for FCC compliance |
| 4 | Active Amazon listing (standard not cited, but product is live) | ★★★ | Amazon has enforced CPC (toys, 2021) and basic safety standards — active = documentation likely |
| 5 | Active listing on Walmart.com or Target.com | ★★★ | Retailer compliance teams vet suppliers before onboarding |
| 6 | Editorial listing on curated safety-vetting sites (Babylist, Wirecutter, Lucie's List, ConsumerReports) | ★★★ | Editorial review implies basic safety vetting |
| 7 | "Third-party tested", "CPSC compliant", "FDA registered", "FCC certified" in listing copy | ★★ | Self-reported — moderate; look for corroboration |
| 8 | Age rating or use-case rating present on listing | ★ | Basic compliance hygiene; all responsible sellers include this |
| 9 | Product only found on Etsy, AliExpress, or no-name DTC stores | ✗ | Negative signal — compliance status unknown |
| 10 | No marketplace presence found | ✗✗ | Strong negative signal — treat as 🔴 until docs confirmed |

---

## Category-Specific Search Channels

Use these in addition to Amazon when the product category has strong specialist channels.

### Children's Toys

```
site:amazon.com "[SEARCH_ANCHOR]"
site:walmart.com "[SEARCH_ANCHOR]"
site:target.com "[SEARCH_ANCHOR]"
site:babylist.com "[SEARCH_ANCHOR]"
site:etsy.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "ASTM F963" OR "CPC" OR "children's product certificate"
site:faire.com OR site:tundra.com "[SEARCH_ANCHOR]"
```

### Electronics & Gadgets

```
site:amazon.com "[SEARCH_ANCHOR]"
fccid.io [model number or brand]
site:bestbuy.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "FCC ID" OR "FCC certified" OR "CE marking"
site:bhphotovideo.com "[SEARCH_ANCHOR]"
```

Key check: search fccid.io directly for the model number. An FCC ID entry = strong compliance evidence.

### Cosmetics & Personal Care

```
site:amazon.com "[SEARCH_ANCHOR]"
site:sephora.com "[SEARCH_ANCHOR]"
site:ulta.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "FDA registered" OR "INCI" OR "dermatologist tested"
site:byrdie.com OR site:allure.com "[SEARCH_ANCHOR]"
```

Key check: FDA voluntary cosmetic registration can be verified at cosmeticsdatabase.ewg.org or fda.gov/cosmetics.

### Food Supplements

```
site:amazon.com "[SEARCH_ANCHOR]" supplement
site:iherb.com "[SEARCH_ANCHOR]"
site:vitacost.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "certificate of analysis" OR "cGMP" OR "NSF certified" OR "USP verified"
```

Key check: NSF Certified for Sport or USP Verified mark = highest compliance signal for supplements.

### Pet Products

```
site:amazon.com "[SEARCH_ANCHOR]" dog OR cat OR pet
site:chewy.com "[SEARCH_ANCHOR]"
site:petsmart.com "[SEARCH_ANCHOR]"
site:petco.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "FDA registered" OR "AAFCO" (for consumables)
```

### Apparel & Textiles

```
site:amazon.com "[SEARCH_ANCHOR]" clothing
site:nordstrom.com "[SEARCH_ANCHOR]"
site:zappos.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "flammability" OR "fiber content" OR "CPSIA" (for children's)
```

### Kitchen & Food-Contact

```
site:amazon.com "[SEARCH_ANCHOR]" kitchen
site:surlatable.com "[SEARCH_ANCHOR]"
site:williams-sonoma.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "FDA food safe" OR "BPA free" OR "NSF certified" OR "lead free"
site:consumerreports.org "[SEARCH_ANCHOR]"
```

### General Consumer Goods

```
site:amazon.com "[SEARCH_ANCHOR]"
site:walmart.com "[SEARCH_ANCHOR]"
"[SEARCH_ANCHOR]" "CA Prop 65" OR "Proposition 65" OR "California warning"
"[SEARCH_ANCHOR]" site:[relevant-specialist-retailer].com
```

---

## What to Extract From Each Listing

For every listing found during evidence gathering, record:

| Field | Look for |
|-------|----------|
| Listing status | Is it active and purchasable? (Not "Currently unavailable" or "Discontinued") |
| Applicable standard cited | ASTM F963, FCC ID, FDA registered, AAFCO, etc. |
| Certificate or document linked | Any PDF or "Product Safety Information" section |
| Compliance self-claims | "Third-party tested", "certified", "compliant" |
| Safety / warning labels | Choking hazard, Prop 65 warning, age restriction |
| Brand name | May help identify the same factory for document requests |
| ASIN / SKU | Record for supplier cross-reference (same ASIN factory = same test reports) |
