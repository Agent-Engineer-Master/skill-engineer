#!/usr/bin/env python3
"""
score_idea.py — Score a business idea against founder profile, anti-goals, and market signals.

Adapted from validate_output.py archetype. Produces a structured score object
that Claude uses to rank and present ideas.

Usage:
  python scripts/score_idea.py --idea "AI tutoring for STEM" \
    --profile 03-exploration/business-search/founder-profile.md \
    --anti-goals 02-vision/anti-goals.md \
    --signals '{"market_size": "large", "competition": "moderate", "timing": "strong"}'

Output: JSON score object to stdout with dimension scores and composite.

Error taxonomy:
  exit 0 — score computed
  exit 1 — file read failed
  exit 2 — bad arguments
"""

import argparse
import json
import re
import sys
from pathlib import Path

# --- Scoring weights (rationale documented per weight) ---
# Weights sum to 1.0 for a normalized composite score in [0, 1].
WEIGHT_FOUNDER_FIT = 0.30    # Highest weight: ideas that don't fit the founder fail regardless of market.
WEIGHT_ANTI_GOAL = 0.25      # Hard filter — any violation should tank the score. High weight ensures this.
WEIGHT_MARKET_SIGNAL = 0.20  # Market evidence matters but can be gathered later. Medium weight.
WEIGHT_TIMING = 0.15         # "Why now?" — important but less controllable. Lower weight.
WEIGHT_DEMAND_SHAPE = 0.10   # Narrow-and-deep vs broad-and-shallow. Tiebreaker weight.

# Anti-goal keywords — loaded dynamically from the anti-goals file.
# These are patterns that, if present in the idea description, flag a violation.
ANTI_GOAL_PATTERNS = []


def load_text(path: Path) -> str:
    """Read a file as UTF-8 text."""
    try:
        return path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Error: could not read {path}: {e}. Check path and permissions.", file=sys.stderr)
        sys.exit(1)


def extract_anti_goals(text: str) -> list[str]:
    """Extract anti-goal items from the anti-goals markdown file.
    Looks for list items (lines starting with - or *) and headings."""
    goals = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")):
            # Strip markdown formatting
            clean = re.sub(r"\*\*|__", "", line[2:]).strip()
            if clean:
                goals.append(clean.lower())
    return goals


def check_anti_goal_violation(idea: str, anti_goals: list[str]) -> tuple[float, list[str]]:
    """Check if the idea violates any anti-goals.
    Returns (score 0-1 where 1 = no violations, list of violated goals)."""
    idea_lower = idea.lower()
    violations = []

    # Common anti-goal signal words mapped to typical anti-goal categories
    signal_map = {
        "operational grind": ["24/7", "always on", "operations heavy", "manual fulfillment", "warehouse"],
        "low margin": ["commodity", "race to bottom", "low margin", "thin margin", "price war"],
        "large workforce": ["hiring spree", "large team", "hundreds of employees", "low-skilled"],
        "over-leverage": ["heavy debt", "leveraged", "large loan", "mortgage"],
    }

    for goal in anti_goals:
        # Direct keyword match
        for word in goal.split():
            if len(word) > 3 and word in idea_lower:
                violations.append(goal)
                break

    # Score: 1.0 if no violations, 0.0 if any violation (hard filter)
    score = 0.0 if violations else 1.0
    return score, violations


def score_founder_fit(idea: str, profile_text: str) -> float:
    """Heuristic score for founder-idea fit based on keyword overlap.
    Returns 0-1. Claude should override this with judgment — this is a baseline."""
    idea_words = set(idea.lower().split())
    profile_words = set(profile_text.lower().split())

    # Count overlap as a rough proxy for domain relevance
    overlap = len(idea_words & profile_words)
    # Normalize: 5+ overlapping words = strong fit
    return min(1.0, overlap / 5.0)


def score_market_signals(signals: dict) -> float:
    """Score based on provided market signals. Each signal maps to a sub-score."""
    signal_scores = {
        "market_size": {"large": 1.0, "medium": 0.6, "small": 0.3, "unknown": 0.5},
        "competition": {"none": 0.3, "low": 0.5, "moderate": 0.8, "high": 0.7, "unknown": 0.5},
        # Crowded = good (proves demand), but very crowded with established players = harder.
        "timing": {"strong": 1.0, "moderate": 0.6, "weak": 0.2, "unknown": 0.5},
        "evidence_quality": {"customer_paid": 1.0, "workaround_built": 0.8, "public_complaint": 0.6,
                             "asked_for_tool": 0.4, "market_report": 0.2, "unknown": 0.3},
    }

    total = 0.0
    count = 0
    for key, value in signals.items():
        if key in signal_scores:
            score_map = signal_scores[key]
            total += score_map.get(str(value).lower(), 0.5)
            count += 1

    return total / max(1, count)


def main():
    parser = argparse.ArgumentParser(description="Score a business idea")
    parser.add_argument("--idea", required=True, help="One-line idea description")
    parser.add_argument("--profile", required=True, help="Path to founder profile markdown")
    parser.add_argument("--anti-goals", required=True, help="Path to anti-goals markdown")
    parser.add_argument("--signals", default="{}", help="JSON object with market signals")
    parser.add_argument("--demand-shape", default="unknown",
                        choices=["narrow-deep", "broad-shallow", "unknown"],
                        help="Demand shape assessment")
    ns = parser.parse_args()

    try:
        signals = json.loads(ns.signals)
    except json.JSONDecodeError as e:
        print(f"Error: --signals is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    profile_text = load_text(Path(ns.profile))
    anti_goals_text = load_text(Path(ns.anti_goals))
    anti_goals = extract_anti_goals(anti_goals_text)

    # Compute dimension scores
    founder_fit = score_founder_fit(ns.idea, profile_text)
    anti_goal_score, violations = check_anti_goal_violation(ns.idea, anti_goals)
    market_score = score_market_signals(signals)
    timing_score = signals.get("timing_score", 0.5)  # Allow explicit override
    if isinstance(timing_score, str):
        timing_score = {"strong": 1.0, "moderate": 0.6, "weak": 0.2}.get(timing_score, 0.5)
    demand_shape_score = {"narrow-deep": 1.0, "broad-shallow": 0.3, "unknown": 0.5}[ns.demand_shape]

    # Composite
    composite = (
        WEIGHT_FOUNDER_FIT * founder_fit
        + WEIGHT_ANTI_GOAL * anti_goal_score
        + WEIGHT_MARKET_SIGNAL * market_score
        + WEIGHT_TIMING * timing_score
        + WEIGHT_DEMAND_SHAPE * demand_shape_score
    )

    result = {
        "idea": ns.idea,
        "composite_score": round(composite, 3),
        "dimensions": {
            "founder_fit": {"score": round(founder_fit, 3), "weight": WEIGHT_FOUNDER_FIT,
                            "note": "Heuristic — Claude should refine with judgment"},
            "anti_goal_compliance": {"score": round(anti_goal_score, 3), "weight": WEIGHT_ANTI_GOAL,
                                     "violations": violations,
                                     "note": "HARD FILTER: any violation = kill the idea"},
            "market_signals": {"score": round(market_score, 3), "weight": WEIGHT_MARKET_SIGNAL,
                               "inputs": signals},
            "timing": {"score": round(timing_score, 3), "weight": WEIGHT_TIMING},
            "demand_shape": {"score": round(demand_shape_score, 3), "weight": WEIGHT_DEMAND_SHAPE,
                             "shape": ns.demand_shape},
        },
        "recommendation": "KILL — anti-goal violation" if violations else (
            "Strong candidate" if composite >= 0.7 else
            "Worth exploring" if composite >= 0.5 else
            "Weak — needs stronger signals"
        ),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
