# Edge cases — map-competitive-arena

## 1. Industry genuinely has only one group
Rare. Pure commodity industries (e.g., regional sand-and-gravel) where every firm competes identically. Verdict: re-axis first; if axes test passes and still one group, document explicitly with reason and flag as low-strategic-discrimination industry. Note that profitability differences must then come from execution, not positioning. Validator will fail single-group output — override requires the drafter to add a top-of-file note "single-group justified because [reason]" AND still split into ≥3 firm-tier groups (large / mid / small) so the validator passes.

## 2. Industry has 8+ groups
Indicates over-granular axes or hyper-fragmented industry. Coarsen axes (3-level scale instead of 5-level) or accept high group count. Don't force into 3-4 if the structure genuinely is fragmented (long tail of regional players).

## 3. Two industries collapsed into one frame
"The streaming industry" combining SVOD, AVOD, music streaming, and game streaming. Each is a separate industry with different group structures. Fix at intake: narrow the industry definition; produce one map per industry. Reference `size-market`'s definition-lock practice.

## 4. Focal layer differs from typical analysis
Industry analyzed at OEM layer has different groups than at distributor layer. State focal layer at intake; do not silently mix. (Same convention as `map-five-forces`.)

## 5. Pre-arena chaos with no winner archetype yet
Multiple firms attempting multiple models, none breaking out. Verdict "none emerging" per group is valid — state explicitly with timeline expectation ("watch for archetype crystallization in 12-18 months").

## 6. Group with a single firm
Common in arenas — a "Category Creator" group of one. Valid IF the firm operates with a distinct strategic posture from others. Don't force into a larger group for symmetry; note the single-firm group and watch whether others enter (signals group viability).

## 7. Axes selected but only 2 clusters emerge
Either axes are correlated (re-axis) OR industry is genuinely binary (e.g., open-source vs proprietary in early-stage developer tools). If genuinely binary, the analysis is incomplete — add a third axis-pair candidate and re-map; if still 2 groups, flag.

## 8. Mobility barriers all eroding at once
Indicates industry-level disruption (not just group-structure shift). Cross-reference with `map-five-forces` and `analyze-trajectory` (Phase 2) — the industry is mid-S-curve transition. Output should note the implication: group structure will be unrecognizable in 3-5 years.

## 9. Multi-archetype group (genuine bifurcation)
A group with leaders pursuing distinct archetypes (one consolidator, one innovator). Do not pick one; note the bifurcation. Predict group split at next analysis.

## 10. Cross-border industry with different group structures per region
US logistics groups differ from EU logistics groups. Either narrow geography at intake (US-only) or produce per-region mini-maps. Do not average — averaging destroys the strategic-group signal.
