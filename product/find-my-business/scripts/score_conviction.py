#!/usr/bin/env python3
"""
score_conviction.py — Generate a conviction scorecard for an idea in deep validation.

Adapted from validate_output.py archetype. Reads validation data and produces
a weighted conviction score across 5 dimensions.

Usage:
  python scripts/score_conviction.py \
    --idea "AI tutoring for STEM" \
    --scores '{"problem_clarity": 4, "customer_pull": 3, "founder_fit": 5, "market_timing": 3, "competitive_moat": 2}'

Output: JSON conviction scorecard to stdout.

Error taxonomy:
  exit 0 — scorecard computed
  exit 1 — missing required dimensions
  exit 2 — bad arguments
"""

import argparse
import json
import sys

# --- Dimension weights (rationale per weight) ---
# Sum to 1.0. Problem clarity and customer pull dominate because
# the canonical frameworks (PG, Blank, Fitzpatrick) all say:
# "Is the problem real?" and "Do customers want this?" are the
# two questions that predict startup success most strongly.
DIMENSIONS = {
    "problem_clarity": {
        "weight": 0.25,
        "description": "Can you state the problem in one sentence a stranger would understand?",
        "scale": {
            1: "Vague sense something is broken, no specifics",
            2: "Problem identified but evidence is thin or secondhand",
            3: "Clear problem statement with 2-3 evidence sources",
            4: "Well-defined problem with multiple independent evidence sources",
            5: "Acute, well-defined problem with customer quotes confirming urgency",
        },
    },
    "customer_pull": {
        "weight": 0.25,
        "description": "Are customers pulling toward a solution, or are you pushing one at them?",
        "scale": {
            1: "No customer conversations, or only compliments received",
            2: "Conversations happened but signals are ambiguous",
            3: "3+ conversations, at least one asked 'when can I use this?'",
            4: "Multiple people willing to be design partners or test early versions",
            5: "Deposit, LOI, or someone willing to pay before product exists",
        },
    },
    "founder_fit": {
        "weight": 0.20,
        "description": "Does this play to your specific strengths, networks, and energy?",
        "scale": {
            1: "Generic opportunity anyone could pursue; no unique angle",
            2: "One founder advantage applies loosely",
            3: "Leverages 1-2 founder advantages (domain knowledge, network)",
            4: "Strong match across multiple advantages plus genuine excitement",
            5: "Deep domain expertise + network access + genuine excitement + unique insight",
        },
    },
    "market_timing": {
        "weight": 0.15,
        "description": "Why now? What changed that makes this possible/urgent today?",
        "scale": {
            1: "No clear 'why now' — could have been built 5 years ago",
            2: "Vague timing story ('AI is growing')",
            3: "Plausible timing story tied to a specific change",
            4: "Clear technology or market shift creating a window",
            5: "Clear inflection point that didn't exist 2 years ago + closing window",
        },
    },
    "competitive_moat": {
        "weight": 0.15,
        "description": "What stops a well-funded competitor from copying this in 6 months?",
        "scale": {
            1: "Thin wrapper, no proprietary asset, easily replicated",
            2: "One weak defensibility element",
            3: "One solid defensible element (domain data, workflow integration, compliance)",
            4: "Two reinforcing defensibility elements",
            5: "Multiple reinforcing moats (network effects + proprietary data + switching costs)",
        },
    },
}


def compute_scorecard(idea: str, scores: dict) -> dict:
    """Compute weighted conviction scorecard."""
    missing = [d for d in DIMENSIONS if d not in scores]
    if missing:
        print(f"Error: missing dimension scores: {', '.join(missing)}. "
              f"Provide all 5 dimensions.", file=sys.stderr)
        sys.exit(1)

    weighted_total = 0.0
    dimension_results = []

    for dim_name, dim_config in DIMENSIONS.items():
        raw_score = scores[dim_name]
        if not isinstance(raw_score, (int, float)) or raw_score < 1 or raw_score > 5:
            print(f"Error: {dim_name} score must be 1-5. Got {raw_score}.", file=sys.stderr)
            sys.exit(2)

        weighted = dim_config["weight"] * raw_score
        weighted_total += weighted

        # Find the scale description for this score
        scale_desc = dim_config["scale"].get(int(raw_score), "")

        dimension_results.append({
            "name": dim_name,
            "score": raw_score,
            "weight": dim_config["weight"],
            "weighted_score": round(weighted, 3),
            "description": dim_config["description"],
            "scale_description": scale_desc,
        })

    # Interpretation bands
    if weighted_total >= 4.0:
        interpretation = "Strong conviction — ready to commit"
        recommendation = "commit"
    elif weighted_total >= 3.0:
        interpretation = "Promising — address specific gaps before committing"
        recommendation = "continue_validating"
        # Find lowest-scoring dimensions to flag
        lowest = sorted(dimension_results, key=lambda d: d["score"])[:2]
        interpretation += f". Focus on: {lowest[0]['name']} ({lowest[0]['score']}/5), {lowest[1]['name']} ({lowest[1]['score']}/5)"
    elif weighted_total >= 2.0:
        interpretation = "Weak — needs significant validation or pivot"
        recommendation = "pivot_or_kill"
    else:
        interpretation = "Kill — redirect energy elsewhere"
        recommendation = "kill"

    return {
        "idea": idea,
        "composite_score": round(weighted_total, 2),
        "max_possible": 5.0,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "dimensions": dimension_results,
    }


def main():
    parser = argparse.ArgumentParser(description="Generate conviction scorecard")
    parser.add_argument("--idea", required=True, help="Idea name/description")
    parser.add_argument("--scores", required=True,
                        help="JSON object with dimension scores (1-5 each): "
                             "problem_clarity, customer_pull, founder_fit, market_timing, competitive_moat")
    ns = parser.parse_args()

    try:
        scores = json.loads(ns.scores)
    except json.JSONDecodeError as e:
        print(f"Error: --scores is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    scorecard = compute_scorecard(ns.idea, scores)
    print(json.dumps(scorecard, indent=2))


if __name__ == "__main__":
    main()
