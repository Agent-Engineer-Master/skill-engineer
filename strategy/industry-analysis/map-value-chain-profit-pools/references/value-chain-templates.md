# Value Chain Templates

Sector-adapted value chain decompositions. Pick the template closest to your industry; adapt as needed. Avoid the generic Porter template (Inbound Logistics → Operations → Outbound Logistics → Marketing/Sales → Service) — it is too abstract for most modern industries.

## Manufacturing / Industrial

```
Raw materials → Components → Sub-assembly → Final assembly → Distribution → Sales/integration → Service & support
```

Example (industrial robotics):
- Raw materials (steel, motors, semiconductors)
- Components (servo motors, controllers, sensors)
- Sub-assembly (arm modules, end-effectors)
- Final assembly (OEM robotic units)
- Distribution (regional distributors, direct)
- Sales/integration (system integrators — design, install, program)
- Service & support (preventive maintenance, repair, software updates)

## Consumer goods / DTC

```
Sourcing → Manufacturing → Brand → Distribution → Retail → Customer service & retention
```

Example (specialty apparel):
- Sourcing (raw fabric, trim, accessories)
- Manufacturing (cut & sew, often offshore)
- Brand (design, marketing, brand IP)
- Distribution (3PL, logistics)
- Retail (DTC web, wholesale, marketplaces)
- Customer service & retention (returns, loyalty, repeat)

## Software / SaaS

```
Infrastructure → Platform → Application → Channel → Implementation → Customer success
```

Example (vertical SaaS):
- Infrastructure (cloud, compute, storage — usually outsourced to hyperscalers)
- Platform (data layer, AI/ML services, integrations)
- Application (the vertical-specific software product)
- Channel (direct sales, partners, marketplace)
- Implementation (onboarding, configuration, training)
- Customer success (account management, expansion, retention)

## Pharma / Medtech

```
R&D → Regulatory → Manufacturing → Distribution → Clinician access → Patient delivery → Post-market surveillance
```

Example (medical devices):
- R&D (research, design, clinical trials)
- Regulatory (FDA/CE submissions, post-market reporting)
- Manufacturing (contract manufacturing or in-house)
- Distribution (GPO contracts, distributors, direct)
- Clinician access (sales reps, KOL engagement, training)
- Patient delivery (hospital procurement, ambulatory clinics)
- Post-market surveillance (adverse events, real-world evidence)

## Financial services

```
Origination → Underwriting → Capital → Servicing → Distribution → Customer relationship
```

Example (consumer lending):
- Origination (lead-gen, marketing, application)
- Underwriting (risk assessment, decisioning)
- Capital (balance sheet, securitization, partner banks)
- Servicing (payment processing, collections)
- Distribution (direct, broker, partner)
- Customer relationship (ongoing engagement, cross-sell, retention)

## Platform / marketplace

```
Supply acquisition → Supply curation → Trust/safety → Discovery → Transaction → Fulfillment → Post-transaction
```

Example (two-sided marketplace):
- Supply acquisition (seller onboarding, supply ops)
- Supply curation (catalog quality, search ranking)
- Trust/safety (verification, fraud, dispute)
- Discovery (search, recommendations, advertising)
- Transaction (payment, escrow)
- Fulfillment (logistics — varies by category)
- Post-transaction (reviews, returns, support)

## Adapting a template

When no template fits cleanly:
1. Start with the closest match
2. Add or remove stages based on the actual sector
3. Aim for 5-9 stages — fewer than 5 is usually too abstract; more than 9 is unwieldy
4. Every stage must have ≥2 representative players you can name

## Where to put the customer

The customer is **after** the last stage of the value chain, not a stage themselves. The value chain decomposes how value is created for the customer, not what the customer does.

## Vertically-integrated players — collapse stages or keep separate?

Some industries are dominated by vertically-integrated players who internalise multiple stages (e.g., Apple owns design + supply-chain orchestration + retail; Amazon owns marketplace + fulfilment + ads). Two options:

1. **Keep stages separate** — preferred when listed pure-plays exist for each stage AND the integrated player publishes segment reporting. Lets you compare integrated-player segment margins vs. pure-play margins (the gap reveals integration benefit).
2. **Collapse adjacent integrated stages** — preferred when the integrated player does not publish segment data AND no listed pure-plays exist (so the stages are not estimable independently). Disclose the collapse in a footnote.

Never silently merge stages — the value-chain shape is the diagnostic.

## Platform / "Z-shape" value chains

Platforms do not have linear value chains in the Porter sense — they coordinate supply-side and demand-side activities across a two-sided structure. For platforms use the **platform/marketplace template above** but be aware:

- The platform itself sits between supply and demand stages; revenue and profit accrue to the platform layer disproportionately when network economies are strong
- Supply-side stages and demand-side stages should be analysed separately on the value chain
- Cross-reference Cicero's "Z-shape value chain" framing for platforms where stages reverse direction (consumer co-creates supply)

The output should still produce a horizontal-bar pool — the platform layer is one stage, supply-side stages are upstream, demand-side stages downstream.

## Modern sector-specific notes (2026)

- **AI-native applications** — treat foundation-model API as a distinct cost/value-chain stage (rented intelligence). The platform layer that wraps the model often captures more profit than the application itself when switching costs are high.
- **Agentic commerce** — agent layer is a new stage between consumer and retailer; if material, model it as a distinct stage with its own profit pool (currently emerging, often pre-monetised).
- **Vertical SaaS rolling up services** — the "implementation services" stage may be larger profit than "software" itself in the early years; do not under-size services.
