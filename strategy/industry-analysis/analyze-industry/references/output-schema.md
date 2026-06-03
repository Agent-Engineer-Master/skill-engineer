# Output Schema — `industry-brief.yaml`

Machine-readable filter file written alongside `industry-brief.html`. Downstream skills (`build-company-model`, `building-buyer-shortlists`, `stress-test`) consume these fields.

## Schema

```yaml
---
industry_slug: string                        # e.g., "industrial-robotics-na"
date_analyzed: YYYY-MM-DD
mode: quick | deep
analyst: claude-analyze-industry
brief_path: string                           # relative path to industry-brief.html

# Scope
scope_question: string                       # the strategic question this brief answers
market_definition:
  sub_sector: string
  geography: string
  customer_segment: string
  size_band: string                          # optional
  framing_chosen: broad | sharpened | surgical

# Strategic environment (BCG Palette)
strategic_environment: Classical | Adaptive | Visionary | Shaping | Renewal
environment_reasoning: string                # one paragraph

# Market sizing (from size-market)
sizing:
  tam_usd_b: number
  sam_usd_b: number
  som_usd_b: number                          # nullable for early-stage analyses
  cagr_pct: number
  cagr_years: string                         # e.g., "2024-2029"
  arena_classification: Arena | Pre-arena | Mature | Declining
  sub_segments:
    - name: string
      size_usd_b: number
      cagr_pct: number
      source_tag: string                     # e.g., "[C: IBISWorld 2025 + Statista 2024]"

# Five Forces (from map-five-forces)
five_forces:
  governing_force: string                    # the single most important force, one phrase
  governing_force_sentence: string           # the causal sentence explaining profit distribution
  rivalry: low | moderate | high
  supplier_power: low | moderate | high
  buyer_power: low | moderate | high
  threat_new_entry: low | moderate | high
  threat_substitutes: low | moderate | high
  complementors: low | moderate | high       # sixth force
  ai_as_force:
    cost_structure_impact: low | moderate | high
    new_entry_vector: present | absent
    data_intermediary_position: contested | concentrated | none

# Value chain + profit pools (from map-value-chain-profit-pools)
profit_pools:
  total_industry_ebit_usd_b: number
  concentration_stage: string                # which stage holds most EBIT
  structural_protection: switching_costs | scale_economies | network_economies | regulatory_barrier | cornered_resource | process_power | counter_positioning | none
  stages:
    - name: string
      ebit_usd_b: number
      ebit_share_pct: number

# Strategic conclusion (from synthesis)
where_to_play: string                        # the chosen segment/layer to focus
how_to_win: string                           # the capability + power combination
verdict: attractive | conditionally_attractive | unattractive
verdict_one_line: string                     # one-sentence summary

# Quality
bar_test_passed: true | false
bar_test_path: string
provenance_tag_coverage_pct: number          # 0-100, must be 100 to ship
---
```

## Rules

- Every field must be present (use `null` for legitimately unknown).
- `provenance_tag_coverage_pct` must be 100 to ship.
- `bar_test_passed` must be `true` to ship.
- `verdict` and `verdict_one_line` are required even for diagnostic briefs without an explicit investment decision — they capture the "so what."

## Downstream consumers

- `build-company-model`: reads `sizing`, `profit_pools`, `five_forces.governing_force` as priors.
- `building-buyer-shortlists`: reads `where_to_play`, `verdict`, `strategic_environment` to filter buyer logic.
- `stress-test`: reads `verdict`, `where_to_play`, `how_to_win` as the proposition to pressure.
