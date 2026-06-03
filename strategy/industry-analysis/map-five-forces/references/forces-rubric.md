# Five Forces Rubric

For each of the 5 classical forces, the assessment must answer 4 questions:
1. **Intensity** — Low / Moderate / High?
2. **Direction of travel** — intensifying / stable / weakening over next 3-5yr?
3. **Structural reason** — WHY is this force at this intensity (one causal sentence)?
4. **AI reshape (inline)** — how is AI reshaping this specific force? intensifying / weakening / no material effect, with a tagged evidence claim when the effect is non-trivial. This is required inline per force; the consolidated reshape matrix later in the document is a summary, not a substitute.

The structural reason matters more than the intensity rating. A Moderate force with no causal explanation is a useless rating. The inline AI-reshape commentary is what makes the analysis defensible in 2026.

## Rivalry

**Anchors:**
- Number of competitors and concentration (HHI, CR4)
- Industry growth rate (low growth intensifies rivalry)
- Differentiation level (commoditized → high rivalry)
- Exit barriers (high exit barriers → trapped capacity → rivalry)
- Switching costs to customers

**Common failure mode:** rating "moderate" without naming the specific basis of competition (price vs feature vs service vs ecosystem).

**Anchored evidence to capture:**
- Top-4 share and direction of travel
- 5-year price trend (real, not nominal)
- Capacity utilization trends
- Notable share shifts (winners/losers)

## Supplier Power

**Anchors:**
- Supplier concentration vs buyer concentration (industry as buyer)
- Substitute inputs available
- Importance of industry's volume to suppliers
- Switching costs for the industry to change supplier
- Threat of forward integration by suppliers

**Common failure mode:** treating all suppliers as monolithic. Often one supplier category has high power (e.g., specialty chemicals) while another has none (commodity logistics).

**Anchored evidence to capture:**
- Top supplier in each major input category, their share of industry's supply
- Recent supplier price moves (last 3 years)
- Any forward integration moves

## Buyer Power

**Anchors:**
- Buyer concentration vs industry concentration
- Buyer purchase volume relative to seller revenue
- Switching costs
- Buyer's threat of backward integration
- Price sensitivity (commoditized purchase → high buyer power)
- Information asymmetry (informed buyer → higher power)

**Common failure mode:** confusing "many small customers" with "low buyer power." If switching is trivial and the product is undifferentiated, many small customers still produce high effective buyer power.

**Anchored evidence to capture:**
- Top customer concentration (top-3, top-10)
- Recent buyer-driven price compression episodes
- Channel mix and channel power

## Threat of New Entry

**Anchors:**
- Capital requirements
- Economies of scale (incumbents)
- Network effects (incumbents)
- Switching costs (customer-side stickiness)
- Access to distribution
- Regulatory barriers, licenses, patents
- Brand equity required
- **New (2026):** AI-native entry vectors — assessed separately in `ai-as-force.md`

**Common failure mode:** focusing on classical capital/scale barriers and missing modern entry vectors (open-source software, marketplace distribution, AI-enabled cost compression).

**Anchored evidence to capture:**
- Named recent entrants (last 5 years) — who, funded, traction
- Failed entrants — who, why
- Specific named regulatory barriers

## Threat of Substitutes

**Anchors:**
- Substitute product or service offering equivalent JTBD
- Relative price-performance of substitute
- Switching cost to substitute
- Buyer's propensity to substitute

**Common failure mode:** defining substitutes too narrowly (same-category alternatives) and missing cross-category substitutes (Zoom substitutes for business travel, Airbnb substitutes for hotels).

**Anchored evidence to capture:**
- Named substitute categories
- Substitute growth rate vs industry growth rate
- Specific switching examples documented

## Naming the governing force

After assessing all 5, identify THE force that explains why profits sit where they sit in this industry. One causal sentence. Examples:

- "Buyer concentration governs this industry because three retail chains represent 60% of demand and have re-priced annually."
- "Switching costs govern this industry because vendor lock-in via proprietary protocols means installed-base wins repeat business at 90%+ retention."
- "AI-driven new entry governs this industry because three AI-native entrants with 1/10th the cost structure have captured 15% share in 24 months."

If no single force can be named, the analysis is incomplete. Go back and look harder.

## When Five Forces breaks down

Five Forces is a structural-snapshot tool. It is the wrong primary tool when:

- **Industry boundaries are fluid** — platform/ecosystem industries where supplier/buyer/competitor lines shift in months. Use `references/platform-extensions.md` to extend the analysis; don't apply the classical template unmodified.
- **The unit of competition is the firm-specific moat, not industry structure** — when the question is "can company X defend its 60% share?", use Helmer's 7 Powers (the Phase 2 `assess-moat-sources` skill), not Five Forces.
- **The environment is Visionary or Shaping** (BCG Strategy Palette) — when the industry is being created/recreated, snapshotting forces of a not-yet-existing structure is futile. Use scenario sets.
- **Demand-side / JTBD shifts are the primary driver** — if the structural question is "what job are customers actually hiring this category for?", JTBD precedes Five Forces.

In these cases, run Five Forces as a supporting lens with explicit caveats, not as the spine.

## Good vs bad output — exemplars

For each force, what a strong vs weak assessment looks like. Use these as bar-check anchors when self-grading the output.

### Rivalry — STRONG
> **Rivalry — High, intensifying ↑.** Top-4 share fell from 78% to 61% over 2021-2025 [C: IBISWorld 2025 + company filings] as two AI-native entrants (Snorkel, Datacurve) captured 8% combined. Real list prices declined 14% over the same period [V: vendor pricing pages archived quarterly]. Structural reason: undifferentiated core offering + zero switching cost has shifted competition to AI-mediated workflow integration, where incumbents lack the data-engineering talent to keep pace [I: triangulation from team-build job-postings, Q4 earnings transcripts].

### Rivalry — WEAK
> **Rivalry — Moderate, stable.** There are several competitors in the market. Price competition exists but is not extreme. The market is competitive.

(No numbers, no tags, no structural reason, no direction-of-travel evidence, no specific basis of competition named.)

### Supplier Power — STRONG
> **Supplier Power — High, stable ↔ for specialty inputs; Low, stable for commoditized inputs.** TSMC + Samsung represent 92% of advanced-node foundry capacity globally [V: TrendForce 2025]; the industry's switching cost is 18-month redesign + qualification [C: industry expert interviews x3]. Commodity assembly is fragmented across 200+ providers and exerts no power. Structural reason: physical-capital and tacit-knowledge concentration at the foundry layer; assembly is engineering-cost-only.

### Supplier Power — WEAK
> **Supplier Power — Moderate.** Suppliers have some power. There are a few major suppliers.

(Doesn't disaggregate supplier categories — the most common failure mode in supplier-power assessments per the rubric above.)

### Threat of New Entry — STRONG
> **Threat of New Entry — High, intensifying ↑.** Three AI-native entrants raised >$50M each in 2024-2025 [V: Crunchbase + press releases]: Abridge ($150M Series C), Suki ($70M), Augmedix ($60M). Two of three have signed top-20 health-system contracts [C: customer press releases + system 10-K disclosures]. Classical barriers (regulatory, capital) remain but are bypassed by API/EHR-embedded delivery models. Structural reason: AI compresses time-to-MVP from years to months and the EHR-app-store distribution channel removes the legacy sales-force capital requirement.

### Threat of New Entry — WEAK
> **Threat of New Entry — Low.** Capital requirements are high and the regulatory burden is significant. Few new entrants are expected.

(Lists classical barriers, ignores modern bypasses, no named entrants, no funded-vs-failed split.)

## Common mistakes (combined)

1. **Universal-Moderate** — every force "Moderate," no governing force named. Validator rejects.
2. **Force as checklist** — sequence of forces walked through with no structural insight. Add the "why" sentence to every rating.
3. **Static snapshot** — no direction-of-travel arrows. Validator rejects (see `dynamism.md`).
4. **Boundary-blindness** — platform industry analyzed with classical boundaries. See `platform-extensions.md`.
5. **Profit-pool mismatch** — force assessment contradicts where dollars sit. Step 6 cross-reference required.
6. **AI sub-bullet trap** — AI mentioned under one classical force, not assessed as transforming overlay. See `ai-as-force.md` reshape matrix.
7. **Symmetric many-buyers fallacy** — "many small customers = low buyer power" without checking switching cost or differentiation.
8. **Complementor trivialization** — "none material" with no justification.
9. **No focal-layer specification** — Five Forces produced for "the semiconductor industry" without specifying fab/fabless/IP/equipment. Validator rejects.
10. **No Helmer handoff** — moat questions answered inside Five Forces instead of deferred to `assess-moat-sources`. Add the handoff note.

## Best combinations (analytical neighbours)

Five Forces pairs natively with:
- **Profit pools** (`map-value-chain-profit-pools`) — mandatory cross-reference at step 6. Force assessment without profit-pool reconciliation is half-finished.
- **Strategy Palette** (orchestrator step 2) — sets environment, which determines how heavily to weight trajectory vs snapshot.
- **7 Powers** (`assess-moat-sources`, Phase 2) — answers the "how to win in this industry" question that Five Forces does not. Pair sequentially: Five Forces tells you the pond, 7 Powers tells you the fish you can keep.
- **JTBD** (`analyze-demand`, Phase 2) — when substitute threat is the candidate governing force, JTBD provides the demand-side check on substitute boundaries.

Five Forces should NOT be paired with:
- SWOT — pre-strategic; if SWOT is in the analysis, replace it with Five Forces + value chain + arenas (per `_shared/2026-terminology.md`).
- BCG Growth-Share Matrix — superseded by Three Horizons; not a structural complement to Five Forces.
