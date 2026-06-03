---
name: map-competitive-arena
description: "Produces a Porter strategic-group map overlaid with McKinsey Arenas framing for an industry. Identifies ≥3 strategic groups via 2-axis visualization, profiles each (size, members, basis of competition, profitability), names a winner archetype (consolidator / innovator-specialist / platform-orchestrator / vertically-integrated / asset-light / none-emerging), and assesses mobility barriers between adjacent groups. Output: competitive-arena.md with map, profiles, archetypes, mobility-barrier matrix, arenas overlay, V/C/A/I tags, next_skills YAML. Sub-skill of analyze-industry; standalone-invocable. Triggers on 'strategic group map for [industry]', 'competitive groups in [industry]', 'who competes with whom in [industry]', 'winner archetypes in [industry]', 'competitive landscape for [industry]'. Do NOT activate for industry forces (use map-five-forces), market sizing or whole-market arenas (use size-market), firm-specific moat (use assess-moat-sources), demand analysis (use analyze-demand)."
---

# Map Competitive Arena

For a defined industry, produce a strategic-group map (Porter) overlaid with the McKinsey Arenas-of-Competition framing where applicable. Output: `competitive-arena.md` that names the actual competitive clusters within the industry, what makes leaders in each cluster win, and what prevents firms from moving between clusters.

**The discipline:** firms within one industry rarely compete uniformly. They form clusters that share strategic posture (scope, channel, asset model) and compete primarily within-cluster. Strategic-group analysis surfaces that structure. McKinsey's arenas framing adds dynamism — in high-growth, high-dispersion markets the group structure shifts, mobility barriers erode, and winner archetypes multiply.

**Iron rules:**
- Every evidence claim carries a V/C/A/I tag — see `../_shared/provenance-tagging.md`.
- ≥3 strategic groups identified. Single- or two-group analysis is almost always a failure of discrimination — see `references/strategic-groups.md`.
- 2-axis visualization mandatory (markdown table or coordinate notation). Axes must be uncorrelated, discriminating, and strategic-choice variables (not outcomes like share or profitability).
- Each group has a named **basis of competition** (the variable on which leaders win — e.g., scale, brand, channel access, data depth).
- Each group has a named **winner archetype** OR explicit statement "no clear winner archetype emerging" with reason — see `references/winner-archetypes.md`.
- Mobility barriers assessed per adjacent-group pair (≥1 named barrier per pair) — see `references/mobility-barriers.md`.
- If the upstream `size-market` arenas screen classified the market as Arena / Pre-arena / Contested mature, run the arenas overlay — see `references/arenas-overlay.md`.

## Process

### 1. Intake — lock the frame
Confirm: industry slug, geographic scope, **focal value-chain layer** (same convention as `map-five-forces`), and whether the upstream `size-market` output is available. If `working/market-sizing.md` exists in the same industry folder, read it and extract the arenas classification. Standalone mode: ask whether the market should be treated as Arena / Pre-arena / Mature / Contested mature / Declining (defaults to Mature if unknown).

### 2. Select the two axes
Read `references/strategic-groups.md`. Apply the three-test axis-selection rubric:
- **Discriminating** — produces ≥3 visibly distinct clusters
- **Uncorrelated** — the two axes capture different strategic dimensions
- **Choice-based** — axes are strategic decisions firms made, not outcomes (no "share" or "profitability" as axes)

Default candidate axes: scope (broad ↔ narrow), integration (full-stack ↔ specialist), price (premium ↔ value), service (high-touch ↔ self-serve), channel (direct ↔ indirect), geographic reach, asset model (heavy ↔ light), data position (rich ↔ poor). Pick the pair that best discriminates THIS industry. State the axis-selection rationale in the output.

### 3. Identify ≥3 strategic groups
Place named firms (≥3 per group where possible) on the 2-axis map. Read `assets/strategic-group-template.md` for the visualization format. The 2-axis viz is a markdown table where rows = one axis, columns = the other, and cell entries are firm names. Cluster firms that occupy similar coordinates.

If only 2 groups appear, re-run step 2 with different axes — the chosen axes are not discriminating. If everyone collapses into one group, the industry may genuinely lack strategic differentiation (rare — flag as a Bar Test risk in output) OR the analysis is wrong (more common — re-axis).

### 4. Profile each group
Per group, write a profile block (≥3 groups):
- **Members** — named firms in the group
- **Estimated size** — % of industry revenue/volume in this group, tagged V/C/A/I
- **Basis of competition** — the variable on which group leaders win
- **Typical profitability** — margin band (high / moderate / low) with reasoning, tagged
- **Trajectory** — group growing, stable, or shrinking as % of industry

### 5. Name winner archetypes
Per group, name a winner archetype from `references/winner-archetypes.md`:
- **Consolidator** — wins via scale economics, M&A roll-up
- **Innovator/specialist** — wins via product/tech lead in defensible niche
- **Platform orchestrator** — wins via network effects, two-sided economics
- **Vertically-integrated player** — wins by owning critical layer
- **Asset-light operator** — wins via capital efficiency, partner leverage
- **None emerging** — explicit when the winning pattern hasn't crystallized (acceptable in pre-arena chaos, deeply commoditized industries)

If multiple firms in a group fit different archetypes, that group is internally splitting — note it; the group may bifurcate.

### 6. Assess mobility barriers
Read `references/mobility-barriers.md`. Mobility barriers ≠ entry barriers. For each pair of adjacent groups on the map, name ≥1 barrier that prevents firms in group A from credibly repositioning to group B (or vice versa). Common barriers: scale-economy gap, brand position, channel access, data-asset accumulation, ecosystem position, regulatory license, cornered resource, capability stack. Tag evidence where the barrier has been tested (failed repositioning attempts are strong evidence).

### 7. Apply arenas overlay (if applicable)
Read `references/arenas-overlay.md`. If the market is classified Arena, Pre-arena, or Contested mature:
- Note expected group-structure signature for that classification
- Identify which group (if any) is positioned to "redefine the arena"
- Flag mobility barriers that are eroding (Arena dynamics specifically erode barriers)
- Name the McKinsey arena (one of 12 current / 18 future) if the industry maps to one

If market is Mature or Declining, skip the overlay and note "Arenas overlay not applicable — market classified [X]."

### 8. Bar Test the analysis
Read `../_shared/bar-test.md`. The two most common failures: (a) axes were correlated and produced a diagonal not clusters; (b) groups described but no winner archetype named. Both reduce strategic-group analysis to taxonomy. Fix before writing output.

### 9. Validate + write output
Run `python scripts/validate_arena.py --output-path <path>`. Checks: ≥3 strategic groups identified, 2-axis visualization present (markdown table), each group has a named basis of competition, winner archetypes named per group (or explicit "none emerging" with reason), ≥1 mobility barrier per adjacent-group pair, V/C/A/I tag coverage ≥6, focal-layer specified, arenas-overlay present-or-justified-absent, `next_skills:` YAML block at end. Write to `working/competitive-arena.md` (orchestrator) or `standalone/map-competitive-arena-YYYY-MM-DD.md` (standalone).

**HTML on request (standalone only):** markdown is the default and the only format the validator and the orchestrator consume. If the user explicitly asks for an HTML version of a standalone run, then after validation passes, also render the output via the `html-output` skill and review it per `../_shared/output-conventions.md` § "HTML deliverables and quality review". Never produce HTML automatically.

### 10. Append next_skills YAML
End the output with:

```
---
next_skills:
  - assess-moat-sources    # firm-specific durable-power (Helmer 7 Powers) for group leaders
  - map-five-forces        # if not yet run — industry-level forces context
---
```

Omit `map-five-forces` if `working/five-forces.md` already exists. At least one skill required.

## Gotchas

- **Symptom:** firms plotted on a diagonal rather than in clusters. **Cause:** axes are correlated (e.g., price × quality where premium-priced firms are also high-quality). **Fix:** re-axis. Pick orthogonal dimensions. The discriminating-axes test in `references/strategic-groups.md`.
- **Symptom:** "all firms compete in one group." **Cause:** axis-selection failure OR drafter unwilling to discriminate. **Fix:** validator rejects single-group outputs. Industries with genuinely-no-differentiation are rare; almost always re-axis.
- **Symptom:** "market share" or "profitability" used as an axis. **Cause:** outcome-as-input. **Fix:** axis-selection rubric in `references/strategic-groups.md` forbids outcomes.
- **Symptom:** group profiles written but no winner archetype named. **Cause:** drafter described what is, not what wins. **Fix:** every group requires `winner_archetype: <name>` or `winner_archetype: none-emerging` with reason.
- **Symptom:** mobility barriers and entry barriers conflated. **Cause:** drafter unfamiliar with Caves/Porter distinction. **Fix:** read `references/mobility-barriers.md`. Entry barrier = outside-in; mobility barrier = group-to-group within industry.
- **Symptom:** arenas overlay skipped despite upstream sizing classifying market as Arena. **Cause:** drafter treated arenas screen as size-market-only output. **Fix:** validator requires arenas-overlay section present (or explicit "not applicable because market is Mature").
- **Symptom:** "Big Tech" or "the incumbents" used as a group label. **Cause:** lazy grouping. **Fix:** groups labeled by strategic posture (e.g., "Full-stack premium enterprise vendors"), not by ownership or vague tier.

## Rules

- Never produce a strategic-group map with <3 groups.
- Never use outcome variables (share, profitability) as axes.
- Never describe groups without naming a winner archetype (or stating "none emerging").
- Never skip the mobility-barrier assessment between adjacent groups.
- Every evidence claim carries a V/C/A/I tag.
- All file reads use `encoding='utf-8'`.

## Old patterns

None yet — v1 (initial build 2026-05-18, Phase 2 sub-skill of analyze-industry).

---
<!-- Built with Agent Engineer Master — get your own production-ready skill: www.agentengineermaster.com/skill-engineer -->
