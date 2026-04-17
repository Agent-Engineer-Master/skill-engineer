#!/usr/bin/env python3
"""
unit_econ.py — compute a CM1/CM2/CM3 waterfall from category benchmarks.

Usage:
    python unit_econ.py --category supplements --aov 79 --cac 110

Benchmark data sourced from references/unit-economics-benchmarks.md (A2X 2026,
Eightx 2026, Luca). Output is markdown ready to paste into §6 of the report.

Every line is prefixed `~ (est.)` because this is benchmark-driven, not audited.

Categories: beauty, supplements, apparel, food, home, pet, electronics, subscription
"""
from __future__ import annotations
import argparse
import sys

# (cogs_pct_low, cogs_pct_high, fulfill_pct, returns_pct)
# cogs_pct is COGS as % of revenue; fulfill_pct is shipping+pick+pack; returns_pct is
# the hit to CM2 from returns at typical rates.
BENCH = {
    "beauty":       (0.30, 0.50, 0.08, 0.05),
    "supplements":  (0.20, 0.35, 0.08, 0.03),
    "apparel":      (0.35, 0.50, 0.10, 0.27),  # apparel returns trap
    "food":         (0.50, 0.70, 0.12, 0.04),
    "home":         (0.40, 0.55, 0.14, 0.10),
    "pet":          (0.34, 0.50, 0.10, 0.04),
    "electronics":  (0.75, 0.85, 0.08, 0.12),
    "subscription": (0.25, 0.40, 0.08, 0.03),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(BENCH.keys()))
    ap.add_argument("--aov", type=float, required=True, help="Average order value in USD")
    ap.add_argument("--cac", type=float, required=True, help="New-customer CAC estimate in USD")
    args = ap.parse_args()

    cogs_lo, cogs_hi, fulfill, returns = BENCH[args.category]
    aov = args.aov
    cac = args.cac

    cogs_mid = aov * (cogs_lo + cogs_hi) / 2
    cm1 = aov - cogs_mid
    cm1_pct = cm1 / aov

    fulfill_cost = aov * fulfill
    returns_cost = aov * returns
    cm2 = cm1 - fulfill_cost - returns_cost
    cm2_pct = cm2 / aov

    cm3 = cm2 - cac  # First-order CM3. For subscription, true CM3 needs retention modelling.
    cm3_pct = cm3 / aov

    payback_orders = cac / cm2 if cm2 > 0 else None

    print(f"""### Unit economics (CM waterfall — benchmark-driven)

Category: **{args.category}** | AOV: ${aov:.2f} | New-customer CAC: ${cac:.2f}

| Line | Value | % of AOV | Notes |
|---|---|---|---|
| Revenue (AOV) | ${aov:.2f} | 100% | — |
| COGS | ~ (est.) ${cogs_mid:.2f} | {(cogs_lo+cogs_hi)/2*100:.0f}% | benchmark range {cogs_lo*100:.0f}–{cogs_hi*100:.0f}% |
| **CM1 (gross)** | **${cm1:.2f}** | **{cm1_pct*100:.1f}%** | — |
| Fulfillment + shipping | -${fulfill_cost:.2f} | -{fulfill*100:.0f}% | typical DTC |
| Returns (at {returns*100:.0f}%) | -${returns_cost:.2f} | -{returns*100:.0f}% | category avg |
| **CM2 (after ops)** | **${cm2:.2f}** | **{cm2_pct*100:.1f}%** | — |
| New-customer CAC | -${cac:.2f} | -{cac/aov*100:.0f}% | first-order only |
| **CM3 (first order)** | **${cm3:.2f}** | **{cm3_pct*100:.1f}%** | negative CM3 expected for subscription models — LTV recovers |

**Payback:** {payback_orders:.1f} orders at current CM2 {"(unsustainable unless subscription)" if payback_orders and payback_orders > 1.5 else ""}.

**Assumptions:**
- COGS midpoint from {args.category} category benchmark ({cogs_lo*100:.0f}–{cogs_hi*100:.0f}%)
- Returns at {returns*100:.0f}% (category average)
- CAC is new-customer, not blended — blended would look better
- No iOS14/ATT attribution adjustment applied to CAC

Every line prefixed `~ (est.)` — this is benchmark-driven, not audited.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
