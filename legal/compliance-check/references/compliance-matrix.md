# Compliance Matrix — US Consumer Product Categories

## Table of Contents
- [How to use this file](#how-to-use)
- [Category 1: Children's Toys & Games](#category-1-childrens-toys--games)
- [Category 2: Electronics & Gadgets](#category-2-electronics--gadgets)
- [Category 3: Cosmetics & Personal Care](#category-3-cosmetics--personal-care)
- [Category 4: Food Supplements & Nutraceuticals](#category-4-food-supplements--nutraceuticals)
- [Category 5: Pet Products](#category-5-pet-products)
- [Category 6: Apparel & Textiles](#category-6-apparel--textiles)
- [Category 7: Kitchen & Food-Contact Items](#category-7-kitchen--food-contact-items)
- [Category 8: General Consumer Goods](#category-8-general-consumer-goods)
- [Cost Reference](#cost-reference)

---

## How to Use

1. Read the product name, description, and intended use to determine which category applies.
2. If a product spans two categories (e.g., an electronic toy for children), apply **both** sections — use the stricter requirement for any overlapping test.
3. Build a Required Tests table from the relevant section(s).
4. Use the cost reference at the bottom for report estimates.

**Classification signals** are the fastest way to assign a category. Match at least two signals before committing.

---

## Category 1: Children's Toys & Games

**Classification signals:** Marketed to or intended for children under 12 | "toy", "kids", "ages X+" in name or listing | Montessori, sensory, educational play items | Puzzles, building sets, play figures, playsets

**Regulatory regime:** CPSC / CPSIA / ASTM

| Test | Required | Trigger condition |
|------|----------|-------------------|
| ASTM F963-23 (toy safety, full) | Yes — baseline | Any toy for children under 12 |
| Lead in paint (16 CFR 1303, max 90 ppm) | Yes if painted | Any painted or coated surface |
| Small parts (16 CFR 1501) | Yes if applicable | Removable pieces, loose components, detachable accessories |
| Choking cylinder check | Yes if age 0–3 | Any component that could be mouthed |
| ASTM D-4236 (art materials toxicology) | Yes | Art supplies: sand, paint, clay, markers, crayons |
| XRF heavy metals screening | Yes | Mineral specimens, crystals, ores, raw stones |
| Magnetic flux index (ASTM F963 §4.40) | Yes | Any magnets or magnetic components |
| Electrical safety (ASTM F963 §4.25–4.26 + EMC) | Yes | Electronic components or battery power |
| Edge/point safety (ASTM F963 §4.7) | Yes | Sharp edges possible during normal use or abuse |
| Strangulation risk (ASTM F963 §4.14) | Yes | Strings, cords, elastic |
| Children's Product Certificate (CPC) | Required | All children's products sold in US — issued by manufacturer/importer based on test reports |

**Required supplier docs:** CPC + third-party lab test reports from CPSC-accepted lab + MSDS for chemical materials

**Compliance path notes:**
- Simplest path: painted wooden toy — ASTM F963 full + lead paint = $400–$800
- Highest complexity: STEM kits with electronics + glass components + small parts = $1,200–$2,500
- Amazon has enforced CPC requirements since 2021; active listing = CPC likely exists
- CPSC Small Batch Manufacturer registration (free, <$1.44M revenue) reduces testing frequency but does not eliminate it

---

## Category 2: Electronics & Gadgets

**Classification signals:** Battery-powered | USB charging | Wireless (Bluetooth, WiFi, RF) | LED displays | Electronic components | "smart", "wireless", "Bluetooth" in name

**Regulatory regime:** FCC + voluntary safety (UL/ETL/CE)

| Test | Required | Trigger condition |
|------|----------|-------------------|
| FCC Part 15 (unintentional radiators) | Yes | Any electronic device that emits RF (includes Bluetooth, WiFi, clocks, LED drivers) |
| FCC ID registration | Yes | Devices with intentional RF transmitters (Bluetooth, WiFi, 2.4GHz) — must display FCC ID |
| UL or ETL listing | Voluntary but market-expected | Any mains-powered or rechargeable-battery device — required by most retailers |
| CA Prop 65 (lead, cadmium, phthalates) | Yes if selling to CA | All consumer goods with listed substances — warning label required if above safe harbor levels |
| RoHS compliance (for EU cross-listing) | Voluntary for US | Restricts hazardous substances in electronics — relevant if any EU sales planned |

**Required supplier docs:** FCC ID certificate (check fccid.io) + CE declaration (EU) + UL/ETL test report if available + CA Prop 65 declaration

**Compliance path notes:**
- FCC ID can be verified at fccid.io — search by brand or model to find existing certification
- If FCC ID found on fccid.io: strong evidence supplier has obtained required certification
- Rechargeable Li-ion products need UN38.3 battery transport certificate for shipping
- Most Chinese electronics factories have CE + FCC as a package — ask for both

---

## Category 3: Cosmetics & Personal Care

**Classification signals:** Applied to human body | Skincare, haircare, makeup, fragrance, soap | Lotions, serums, oils, balms, scrubs | "beauty", "skin", "hair", "body" in name

**Regulatory regime:** FDA 21 CFR 700–740 (cosmetics) + MoCRA (2023)

| Test | Required | Trigger condition |
|------|----------|-------------------|
| Ingredient safety assessment | Yes (MoCRA 2023) | All cosmetics — responsible party must ensure safety |
| Label compliance (INCI names, net weight, manufacturer/distributor) | Yes | All cosmetics — FDA 21 CFR 701 |
| FDA Cosmetic Facility Registration | Yes (MoCRA, effective Dec 2024) | All facilities that manufacture/process cosmetics for US sale |
| FDA Product Listing | Yes (MoCRA, effective Dec 2024) | All cosmetic products sold in US |
| Allergen / "free from" claims | Yes if claimed | Must be substantiated; "fragrance-free" has specific meaning |
| CA Prop 65 (lead in lip products, formaldehyde releasers) | Yes if selling to CA | Common triggers: lead in lipstick, formaldehyde in hair straighteners |
| Color additive approval (FDA) | Yes | Any product using color additives — must be FDA-approved for cosmetic use |
| Preservative efficacy test (USP 51) | Recommended | Any water-based product to demonstrate shelf stability |

**Required supplier docs:** Safety Data Sheet (SDS) + full ingredient list (INCI) + FDA facility registration number + any claim substantiation + CA Prop 65 declaration

**Compliance path notes:**
- Cosmetics are not pre-approved by FDA — safety is the brand's responsibility
- MoCRA 2023 added registration requirements; non-compliant suppliers = legal exposure
- "Drug-cosmetic" crossovers (SPF sunscreen, anti-dandruff, antiperspirant) are regulated as OTC drugs — much higher bar

---

## Category 4: Food Supplements & Nutraceuticals

**Classification signals:** Capsules, tablets, gummies, powders for ingestion | "supplement", "vitamin", "probiotic", "protein" | Health claims in name/description | "immune support", "energy", "sleep"

**Regulatory regime:** FDA DSHEA (Dietary Supplement Health and Education Act) + 21 CFR 111 (cGMP)

| Test | Required | Trigger condition |
|------|----------|-------------------|
| cGMP compliance (21 CFR 111) | Yes | All dietary supplement manufacturers |
| Supplement Facts panel | Yes | All supplements — specific format required |
| Structure/function claim notification (FDA) | Yes if claimed | Any claim like "supports immune health" — must file with FDA within 30 days of marketing |
| New Dietary Ingredient (NDI) notification | Yes if applicable | Any ingredient not marketed before Oct 15, 1994 |
| Heavy metals testing (USP 2232) | Best practice | Common in botanical/herbal supplements — lead, arsenic, mercury, cadmium |
| Contaminant testing | Best practice | Pesticides, microbials, solvents — required by cGMP |
| CA Prop 65 | Yes if selling to CA | Heavy metals in supplements are a common trigger |

**Required supplier docs:** Certificate of Analysis (CoA) per lot + cGMP facility audit certificate + Supplement Facts panel proof + FDA facility registration number + any NDI notifications

**Compliance path notes:**
- Supplements are extremely high regulatory complexity — suppliers must be FDA-registered facilities
- Disease claims ("cures", "treats", "prevents") are prohibited and convert a supplement to a drug
- Dropshipping supplements requires careful supplier vetting — many overseas suppliers lack US cGMP compliance

---

## Category 5: Pet Products

**Classification signals:** Marketed for pets | "dog", "cat", "pet", "animal" in name | Collars, leashes, beds, toys, grooming | Pet food, treats, chews

**Regulatory regime:** Split — consumable vs. non-consumable

**Non-consumable pet accessories (toys, beds, collars, leashes):**

| Test | Required | Trigger condition |
|------|----------|-------------------|
| CA Prop 65 | Yes if selling to CA | Heavy metals, phthalates in dyes/materials common in pet accessories |
| ASTM F963 equivalent | No federal standard | No mandatory US safety standard for non-consumable pet products |
| Choking / strangulation risk assessment | Best practice | Small components, strings — no federal mandate but liability exposure |

**Consumable pet food, treats, chews:**

| Test | Required | Trigger condition |
|------|----------|-------------------|
| FDA registration (21 CFR 1) | Yes | Any facility that manufactures animal food for US sale |
| AAFCO nutritional adequacy | Yes if "complete and balanced" claimed | Full nutritional profile testing required |
| Ingredient labeling (AAFCO format) | Yes | All pet food — ingredient list by weight |
| CA Prop 65 | Yes if selling to CA | Heavy metals in fish-based products, treats |

**Required supplier docs:** For accessories: CA Prop 65 declaration + material safety data. For consumables: FDA facility registration + AAFCO statement + CoA

**Compliance path notes:**
- Non-consumable pet products have no federal safety standard — Prop 65 is the main gate
- Pet food dropshipping is extremely complex — FDA registration + AAFCO + state feed laws apply
- Default to non-consumable accessories for lowest compliance overhead

---

## Category 6: Apparel & Textiles

**Classification signals:** Worn on the body | Clothing, underwear, socks, hats, scarves | Fabric-based items | "shirt", "pants", "dress", "pajamas", "blanket" in name

**Regulatory regime:** CPSC + FTC + CPSIA (for children's)

| Test | Required | Trigger condition |
|------|----------|-------------------|
| Flammability (16 CFR 1610 — general) | Yes | All clothing for adults |
| Children's sleepwear flammability (16 CFR 1615/1616) | Yes | Sleepwear for children sizes 0–14 — either inherently flame-resistant or snug-fitting |
| CPSIA tracking label | Yes | All children's products — permanent label with manufacturer, date, batch |
| Lead content (CPSIA) | Yes | Children's apparel under 12 — substrate and surface coatings |
| Fiber content labeling (Textile Fiber Products ID Act) | Yes | All textile products — must disclose fiber composition % |
| Country of origin labeling | Yes | All textile/apparel products |
| CA Prop 65 (AZO dyes, lead, cadmium) | Yes if selling to CA | Common in dyed fabrics and metal hardware (zippers, buttons) |

**Required supplier docs:** Flammability test report + fiber content declaration + CA Prop 65 declaration + CPSIA tracking label spec (for children's)

**Compliance path notes:**
- Children's pajamas are the highest-risk subcategory — must be snug-fitting OR treated with flame retardant (treated is often more expensive and problematic for toxicity)
- Adult apparel: flammability test is the main gate; relatively low cost ($100–$300)
- AZO dyes in imported fabrics are a common Prop 65 trigger — request restricted substances declaration from supplier

---

## Category 7: Kitchen & Food-Contact Items

**Classification signals:** Used for food preparation, storage, or serving | Plates, bowls, cups, utensils, cutting boards, food storage containers | "BPA-free", "food safe" in listing | Cookware, bakeware

**Regulatory regime:** FDA 21 CFR food contact + CA Prop 65

| Test | Required | Trigger condition |
|------|----------|-------------------|
| FDA food contact compliance (21 CFR 176–186) | Yes | Any item that contacts food — material must be FDA-approved for food contact |
| Migration testing | Best practice / required for claims | Plastics, coatings, dyes — demonstrates substances don't migrate into food at unsafe levels |
| Heavy metals testing (lead, cadmium in ceramics/glazes) | Yes for ceramics | FDA CPG §555.425 limits lead/cadmium in ceramics — common in imported pottery |
| CA Prop 65 (lead, PFAS in non-stick, BPA) | Yes if selling to CA | Non-stick coatings (PFAS), glazes (lead), and plastic containers (BPA/BPS) are common triggers |
| NSF certification | Voluntary | Strong positive signal for food safety — NSF 51 for food equipment materials |

**Required supplier docs:** FDA food contact material declaration + migration test report (if plastics/coatings) + heavy metals test (if ceramics) + CA Prop 65 declaration

**Compliance path notes:**
- Ceramic/enamel products from China have historically failed FDA lead/cadmium limits — require test reports
- Non-stick coatings: PTFE (Teflon) is acceptable; PFOA (older non-stick) was phased out; PFAS-free claims need substantiation
- BPA-free plastics still need FDA food contact approval for the substitute material

---

## Category 8: General Consumer Goods

**Classification signals:** Does not fit categories 1–7 | Home décor, office supplies, stationery, storage, tools, sporting goods, fitness equipment, travel accessories

**Regulatory regime:** No single federal standard — CA Prop 65 is the primary gate for US sales

| Test | Required | Trigger condition |
|------|----------|-------------------|
| CA Prop 65 | Yes if selling to CA | Any product containing listed chemicals above safe harbor levels — warning label required |
| FTC labeling (environmental claims) | Yes if claimed | "Eco-friendly", "biodegradable", "recycled" claims must be substantiated per FTC Green Guides |
| ASTM / ANSI product-specific standard | Check by type | Sporting goods, bike helmets (CPSC 16 CFR 1203), luggage (none federal), etc. |
| CPSIA (if secondary use with children) | Yes | If product could be used by children under 12 even if not marketed to them |

**Required supplier docs:** CA Prop 65 declaration + any applicable ASTM/ANSI test report + material safety data

**Compliance path notes:**
- This is the lowest federal compliance overhead category — Prop 65 is the main practical gate
- For sporting goods with safety risk (helmets, protective gear): check for applicable CPSC or ASTM voluntary standard
- Travel accessories (bags, organizers, adapters): Prop 65 for hardware/zippers/fabrics is the main concern

---

## Cost Reference

| Test type | Estimated cost range | Notes |
|-----------|----------------------|-------|
| ASTM F963-23 full (toy) | $500–$1,800 / SKU | CPSC-accepted lab required |
| Lead in paint only (16 CFR 1303) | $100–$200 | Can be standalone or bundled |
| Small parts (16 CFR 1501) | $150 standalone | Usually bundled in F963 |
| ASTM D-4236 (art materials) | $200–$500 | |
| XRF heavy metals | $200–$400 | |
| FCC Part 15 testing | $800–$2,500 | Includes RF emissions + intentional radiator |
| Flammability (16 CFR 1610) | $100–$300 | Per fabric/garment construction |
| Children's sleepwear flammability | $300–$600 | Stricter standard |
| Migration testing (food contact) | $300–$800 | Per material/product type |
| Heavy metals (ceramics, FDA method) | $150–$400 | |
| CA Prop 65 screening panel | $200–$500 | Covers common triggers: lead, cadmium, phthalates |
| Full multi-category bundle | $1,500–$3,500+ | Complex products spanning multiple regimes |
