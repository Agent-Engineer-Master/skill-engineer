---
name: compliance-check
description: >
  Assesses US regulatory compliance likelihood for any consumer product before listing for US sale.
  Accepts a CJ product PID/URL, Amazon ASIN, or product name/description as input. Classifies
  the product into a regulatory category (children's toys, electronics, cosmetics, supplements,
  pet products, apparel, kitchen/food-contact, or general consumer goods), determines which US
  standards apply, gathers market evidence, and produces a structured verdict (🟢/🟡/🟠/🔴).
  Saves report to a compliance-reports directory. Do NOT use for non-US markets or to produce legal opinions.
argument-hint: "[CJ PID | CJ URL | Amazon ASIN | product name or description]"
---

# /compliance-check — US Regulatory Compliance Assessment

Assess compliance likelihood for any consumer product before listing for US sale.

**Usage:** `/compliance-check [input]`

**Accepted inputs:**
- CJ product PID (UUID like `E581D9BF-BCBC-421B-B12D-3762565A1C50`, or numeric 18+ digit string)
- CJ product URL (`https://cjdropshipping.com/product/xxx`)
- Amazon ASIN (`B08GFK757R`)
- Product name or free text description (`"bamboo cutting board with juice groove"`)

---

## CRITICAL: Role and Scope

This skill produces **evidence-based assessments**, not legal opinions. A 🟡 verdict means "market evidence suggests the supplier has documentation — request it." It does not mean the product is safe to list without obtaining actual certificates.

No product advances past `rfq-sent` status without a compliance verdict from this skill.

---

## Step 1 — Parse Input and Resolve Product Identity

Determine input type:

**CJ PID** (UUID pattern `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`, numeric 18+ digits, or `CJHD` prefix):
If you have a CJ lookup script in your project, run it with `--pid [PID] --pretty`.
Otherwise, use the CJ product URL directly or the product name as a search anchor.
Extract: `name`, `category`, `description`, `weight_g`, `length_cm`, `width_cm`, `height_cm`, `variants[].price`.

**CJ product URL:** Extract PID from URL path, then proceed as CJ PID above.

**Amazon ASIN** (`B0` prefix + alphanumeric, 10 chars):
`WebFetch https://www.amazon.com/dp/[ASIN]` — extract title, description, age rating, compliance signals.

**Product name / free text:** Use as search anchor directly. Skip CJ API lookup.

Store these for use throughout:
- `PRODUCT_NAME` — resolved product name
- `PRODUCT_INPUT` — original input as-is
- `PRODUCT_CATEGORY` — assigned in Step 2
- `SEARCH_ANCHOR` — best 3–5 word phrase for searches (e.g. "bamboo cutting board" not the full CJ title)

---

## Step 2 — Classify Product and Load Compliance Requirements

Read `references/compliance-matrix.md`.

Identify which category applies based on product name, description, and intended use. Match at least two classification signals before committing. If a product spans two categories (e.g., an electronic toy for children), apply both sections and use the stricter requirement for any overlap.

**Categories:**
1. Children's Toys & Games
2. Electronics & Gadgets
3. Cosmetics & Personal Care
4. Food Supplements & Nutraceuticals
5. Pet Products
6. Apparel & Textiles
7. Kitchen & Food-Contact Items
8. General Consumer Goods

Set `PRODUCT_CATEGORY` to the matched category name(s).

---

## Step 3 — Build Required Tests Table

Using the relevant section(s) from `references/compliance-matrix.md`:

1. Answer each trigger condition YES / NO / UNCERTAIN based on the product data
2. Mark UNCERTAIN only if genuinely unclear — default to the stricter interpretation
3. Build a Required Tests table: Standard | Required (Yes/No/Uncertain) | Reason | Estimated Cost
4. Calculate the estimated total testing cost if independent testing were required

Do not hallucinate compliance requirements. Use only what is in the reference file.

---

## Step 4 — Market Evidence: Primary Search

Read `references/market-evidence-guide.md` for the signal strength ranking and category-specific search channels.

Run the searches listed under the matched category in the guide. For each relevant result, `WebFetch` the product page.

For each listing found, extract the fields from the "What to Extract" table in the guide: listing status, compliance standard cited, certificate linked, self-claims, safety labels, brand, ASIN/SKU.

Stop early if 🟢-level evidence is found (official compliance document located).

---

## Step 5 — Market Evidence: Secondary Search

Run the cross-category search:
```
"[SEARCH_ANCHOR]" "[primary standard for PRODUCT_CATEGORY]" OR "certified" OR "compliant" OR "third-party tested"
```

Run one additional broad search without site filter to surface DTC brand sites and editorial coverage:
```
"[SEARCH_ANCHOR]" -site:amazon.com -site:walmart.com -site:target.com
```

Extract the same fields as Step 4. Combine all evidence before assigning a verdict.

---

## Step 6 — Compliance Verdict

Based on all evidence, assign one verdict:

| Verdict | Criteria |
|---------|----------|
| 🟢 **Strong Evidence** | Official compliance document found (CPC PDF, FCC ID on fccid.io, CoA, etc.) OR active major-retailer listing with explicit standard cited |
| 🟡 **Likely Compliant** | Active Amazon or major retailer listing found (retailer enforcement implies documentation exists), but no direct certificate located. Product type has a well-understood compliance path. |
| 🟠 **Uncertain** | Limited marketplace presence (DTC-only or sparse results); compliance docs not confirmed; category is moderately complex or has multiple applicable standards |
| 🔴 **High Risk** | Not found on Amazon or major retailers; compliance-sensitive category; no compliance references found; or product characteristics trigger high-risk flags (e.g. loose magnets for children, consumable for infants, mains-powered without FCC ID) |

Set **Confidence:** High / Medium / Low based on how many sources were searched and how current the results appear.

List **Key risks:** 2–4 specific risk factors for this product based on its characteristics.

---

## Step 7 — Write Report and Update Records

### 7a. Create compliance report

Read `references/report-template.md`.

**Directory:** `compliance-reports/` (adjust to your project's path)
**Filename:** `YYYY-MM-DD-[product-slug].md` (slug = lowercase-hyphenated product name)

Follow the template exactly. Do not leave placeholders. Add a `category` field in the frontmatter matching `PRODUCT_CATEGORY`.

### 7b. Update catalog record (if product is in catalog)

If this product appears in the active product catalog, find its entry and update the `compliance-docs` field:
- Format: `[verdict emoji] [verdict label] — [[YYYY-MM-DD-product-slug]]`
- Example: `🟡 Likely Compliant — [[2026-03-28-bamboo-cutting-board]]`

### 7c. Write recall (optional)

Optionally log to your memory or notes system:

```yaml
---
type: recall
date: YYYY-MM-DD
tags: [compliance-check, product-assessment]
---

Ran compliance assessment for [PRODUCT_NAME] (input: [PRODUCT_INPUT]).
Category: [PRODUCT_CATEGORY]. Verdict: [emoji + label] — [1-sentence evidence summary].
Key risks: [comma-separated list].
Recommended action: [top action item].
Report: compliance-reports/YYYY-MM-DD-[slug].md
```

---

## Rules

- Reference files are required. Do not hallucinate compliance standards or costs — use `compliance-matrix.md`.
- When the user flags an incorrect verdict, assessment error, or missing standard: update the relevant section of `references/compliance-matrix.md` immediately.
- When a report is confirmed accurate by the user: save it to `assets/approved-examples/`.
- Never state that a product "is compliant" — only that evidence suggests compliance. The supplier's documentation is the only proof.
- Never skip Step 2 classification. The wrong compliance path produces a meaningless report.
- If the CJ API lookup is unavailable: continue with product name / description as the search anchor. Note this in the report.
