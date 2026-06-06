# Dataset Schema — Human-Readable Explainer

The authoritative schema is `dataset-schema.yaml` (v1.0). This file explains how to populate each block and what failure modes the schema is designed to prevent.

## Why a structured dataset

The dataset is the **load-bearing data structure** of the reimagine-industry workflow. Every venture concept generated in Phase 5 traces back to specific dataset entries — that traceability is what allows the bar test to verify concepts are grounded and not free-associated.

Disruption ideation that skips structured grounding produces concepts that feel compelling in the room and collapse on stress test. The schema is the discipline that prevents that.

## Block-by-block guide

### `industry` (Phase 1)
The industry-wide context. Required before any analysis.

- **`definition`** is the most important field. Write what's in scope AND what's not. "DTC ecommerce" is too broad; "DTC ecommerce for physical consumer goods sold in the US via Shopify, excluding marketplaces and B2B" is usable.
- Numeric fields (`total_market_size`, `growth_rate`) MUST have V/C/A/I tags. Untagged numerics fail validation.

### `value_chain` (Phase 1)
Every node in the chain from raw supply to end consumer, with margin ranges and the two critical booleans: who owns the customer relationship, who owns the data. Disruption typically comes from displacing the relationship-owner or data-owner — those booleans are diagnostic.

- **`flows`** matter as much as nodes. A flow with `friction_level: high` is a candidate disruption surface.
- Node `type: intermediary` is the most disruption-prone node type — Stripe replacing payment intermediaries, Plaid replacing data brokers.

### `market_structure` (Phase 1)
- **`information_asymmetries`** is the highest-leverage block in Phase 1. Most digital disruptions exploit asymmetric information (suppliers know what customers don't, brokers know what both sides don't). If this block is empty, Phase 1 is incomplete.
- `fragmentation: highly_fragmented` strongly suggests Aggregation Theory will fit in Phase 4.

### `value_chain_pain` (Phase 2)
**Keyed by entity type, not just customers.** The widest design choice in the schema — it broadens the disruption surface beyond end-customer pain to supplier pain (Shopify pattern), intermediary pain (Stripe), and non-consumer pain (Christensen new-market footholds).

Per entity:
- **Segments are behavioral or situational, never demographic.** "First-time buyer within 7 days of a gift-giving event" is usable; "women 25-34" is not.
- **JTBD requires all three types per segment.** Functional jobs are easy to find; emotional and social jobs are where disruption opportunities hide.
- **`workaround` is the load-bearing field for pain points.** If a customer cobbles together a workaround, the pain is real and the workaround is the proto-product. "No workaround — pain may be hypothetical" is acceptable but flagged.
- **Non-consumption must be populated.** Most teams skip this; non-consumers are where new-market disruption (Christensen) lives.

### `enabling_conditions` (Phase 3)
Five axes (tech, cost, behavioral, regulatory, supply). The block lists individual conditions, but the **`intersections`** sub-block is where the load-bearing why-now lives. Single-condition why-nows are almost always weak; 2-3-way intersections are what create disruption windows.

- **`window_timing`** classifies how much time remains before consolidation. "Wide-open" with 0-12 months gone since the intersection became true is the strongest. "Closed" forces a sharper counter-positioning thesis.
- **`why_now_paragraph`** is generated at Phase 3 end and quoted verbatim in every Phase 6 stress test. It's the single most-cited field in the dataset.
- **`capability_seeds`** is the Phase 3 **seed step** — the change that makes Phase 3 feed *generation*, not just validation. For each intersection, list jobs that become *possible* (not merely cheaper) now that the capabilities co-exist — jobs no incumbent serves because they couldn't exist before. Each seed cites the capability, NOT an incumbent. These feed Phase 5 Move 8 (capability-first) and the Phase 4.6 Thiel Secret reframe. Without this block, the skill triangulates from existing players because the only generative inputs are incumbent-anchored. ≥1 seed is required.

### `incumbents` (populated in Phase 4)
Per major player:
- **`profit_pool_source`** is the critical field for counter-positioning. The incumbent's load-bearing revenue line is the thing a counter-position threatens.
- **`structural_constraints`** are why the incumbent can't easily copy. Without this block, counter-positioning analysis is impossible.

### `framework_signals` (Phase 4)
The intermediate output between dataset and concepts. Each signal cites specific Phase 1-3 dataset paths so concepts in Phase 5 inherit that traceability.

- Path syntax: `phase2.customers.gifting-shoppers.pain[evaluate]` — dot-walks the dataset.
- Framework-specific fields are documented in `frameworks-cheatsheet.md`.

### `venture_concepts` (Phase 5-6)
The final output. Concept fields populated in Phase 5; stress test fields populated in Phase 6; `final_status` set at Gate 3.

- **Every concept ships as a bet.** `load_bearing_hypothesis` (the single claim that, if false, kills it), `validation_test` (cheapest experiment + pass/fail thresholds + time-to-signal), and `value_if_true` are required on every concept in both lanes. This is what turns the Phase 5 human gate from an unanswerable "is this true?" into a fundable "which tests are worth running?"
- **`origin`** tags the generation lane: `capability-first` (Move 8 or a Secret-derived concept) or `incumbent-first` (Moves 1-7). The kept set MUST contain ≥1 `capability-first` concept — the first-principles lane has to survive the filter, not just be generated.
- **`why_unknown`** is required for `capability-first` concepts: why the hypothesis can't be settled by desk research (usually a behavioural fact that doesn't exist in the data yet, needing a forward test). `incumbent-first` concepts may mark this `desk-researchable`.
- `move` now ranges 1-8 (Move 8 = capability-first / new-to-the-world).
- `rejection_rationale` is required for any concept with `final_status: rejected`. This goes into `signals-log.md` so future runs don't re-propose without reconsidering.

## Validation philosophy

Validation is **hard-fail, not warn**. The validator (`scripts/validate_dataset.py`) refuses to mark a phase complete if any required field is missing or any provenance tag is absent. This is deliberate: warnings get ignored; hard-fails force the iteration that produces better concepts.

The validator runs after each phase. If it fails, the skill loops back into the phase to fix the specific field that failed — not the whole phase.

## What goes in working/ vs. the root

- **Working files** (`working/value-chain-pain-audit.md`, `working/enabling-conditions-scan.md`, etc.) — raw librarian output, sub-skill output. Source material.
- **Root files** (`disruption-dataset.yaml`, `venture-concepts.md`, `reimagination-brief.md`) — synthesized, structured, the skill's actual deliverables.

This separation matches the convention in `../_shared/output-conventions.md`.
