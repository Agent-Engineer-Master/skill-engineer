# Compliance Report Template

Copy this template to `15-store-context/compliance-reports/YYYY-MM-DD-[product-slug].md`.
Replace every `[placeholder]` with real values. Do not leave placeholders in the saved file.

---

```markdown
---
product: [PRODUCT_NAME]
input: [PRODUCT_INPUT]
category: [Regulatory category — e.g. Children's Toy | Electronics | Cosmetics | Pet Product | Apparel | Kitchen | General Consumer]
date: YYYY-MM-DD
verdict: [🟢 Strong Evidence | 🟡 Likely Compliant | 🟠 Uncertain | 🔴 High Risk]
confidence: [High | Medium | Low]
agent: product-buyer
---

# Compliance Assessment: [PRODUCT_NAME]

**Date:** YYYY-MM-DD
**Input:** [original input]
**Category:** [regulatory category]
**Verdict:** [verdict emoji + label]
**Confidence:** [High / Medium / Low]

---

## Product Profile

| Field | Value |
|-------|-------|
| Product type | [Toy / Electronics / Cosmetic / Pet Accessory / Apparel / Kitchen / Other] |
| Regulatory regime | [CPSC/CPSIA | FCC | FDA Cosmetics | FDA DSHEA | AAFCO | CPSC Apparel | FDA Food Contact | General/Prop 65] |
| Target user | [e.g. children ages 3–8 | adults | pets | general consumer] |
| Key materials | [wood, plastic, silicone, fabric, etc.] |
| Key characteristics | [painted, electronic, consumable, food-contact, etc.] |
| Weight | [Xg — from supplier data or estimate] |
| Dimensions | [L×W×H cm — from supplier data or estimate] |

---

## Required Tests

| Standard | Required | Reason | Est. Cost |
|----------|----------|--------|-----------|
| [Standard name] | Yes / No / Uncertain | [reason based on product characteristics] | $X–$Y |
| [Standard name] | Yes / No / Uncertain | [reason] | $X–$Y |
| CA Prop 65 | Yes / No / Uncertain | [reason] | $X–$Y |

**Estimated total if independent testing required:** $X–$Y

---

## Market Evidence

### Amazon
[For each listing found:]
- **[Brand name]** ([ASIN: xxx if available]) — Active / Inactive
  - Compliance standard cited: [Yes — "ASTM F963" / FCC ID / etc. | No]
  - Certificate or document linked: [Yes — URL | No]
  - Safety/warning labels: [Yes — describe | No]
  - Compliance self-claim: [Yes — quote | No]

[If nothing found:]
- No active Amazon listings found for this product.

### Major Retailers (Walmart / Target / Best Buy / etc.)
[Results or "Not found"]

### Specialist Channels
[Category-appropriate channels — Sephora, Chewy, iHerb, Faire, etc. — or "Not applicable"]

### Editorial Sources
[Results or "Not found"]

### Direct Compliance References
[Any standard name + compliance terms found in web search — or "None found"]

---

## Compliance Verdict

**Verdict:** [emoji + label]
**Confidence:** [High / Medium / Low]

**Evidence summary:**
[2–3 sentences: what was found and why the verdict was assigned. Be specific about sources.]

**Key risks:**
- [Risk 1 — specific to this product's characteristics]
- [Risk 2]
- [Risk 3 if applicable]

---

## Recommended Actions

- [ ] [Primary action — e.g. "Request [Standard] test report + [Certificate type] from supplier"]
- [ ] [If active Amazon listing found: "Reference [Brand] ASIN [xxx] — likely same factory; supplier has documentation"]
- [ ] [If FCC: "Verify FCC ID at fccid.io before requesting docs"]
- [ ] [If independent testing needed: "Commission at accredited lab — reference compliance-matrix.md for cost estimate"]
- [ ] [If Prop 65 relevant: "Request California Prop 65 declaration and restricted substances list"]

**Estimated timeline:**
- Supplier document request: 3–7 business days
- Independent testing (if needed): 2–4 weeks
- Estimated cost: $[X]–$[Y]
```
