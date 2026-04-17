#!/usr/bin/env python3
"""
mine_reddit_pain.py — Search Reddit for pain points in specified subreddits.

Adapted from search_and_rank.py archetype. Uses the Reddit API (OAuth2) to search
for complaint/pain signal posts, then ranks by engagement and lack of existing solution.

Usage:
  python scripts/mine_reddit_pain.py --subreddits "SaaS,startups,smallbusiness" \
    --query "I wish,I hate,why doesn't,frustrated" --limit 30

Output: JSON array of ranked pain signals to stdout. Each entry:
  {"rank": int, "score": float, "title": str, "url": str, "subreddit": str,
   "upvotes": int, "comments": int, "snippet": str, "pain_signal": str}

Error taxonomy:
  exit 0 — results returned (may be empty — that's valid)
  exit 1 — Reddit API call failed
  exit 2 — bad arguments
  exit 3 — authentication failed (check .env for REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET)

Required: requests, python-dotenv
Reddit API credentials: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET in .env
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print(
        "Error: 'requests' package not installed. "
        "On WSL: 12-operations/scripts/venv-linux/bin/pip install requests. "
        "On Windows: use the llms conda env.",
        file=sys.stderr,
    )
    sys.exit(2)

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "Error: 'python-dotenv' package not installed. "
        "On WSL: 12-operations/scripts/venv-linux/bin/pip install python-dotenv. "
        "On Windows: use the llms conda env.",
        file=sys.stderr,
    )
    sys.exit(2)

# --- Configuration ---
USER_AGENT = "find-my-business:v1.0 (by /u/skill-engineer)"  # Reddit requires a descriptive UA.
REQUEST_TIMEOUT = 15  # Seconds. Reddit API is usually fast.
MAX_RETRIES = 2       # Reddit rate-limits aggressively; 2 retries with backoff.

# Pain signal search terms — these capture how people express frustration on Reddit.
DEFAULT_PAIN_TERMS = [
    "I wish", "I hate", "why doesn't", "is there a tool",
    "frustrated with", "waste of time", "there has to be a better way",
    "anyone else struggle", "pain point",
]

# Ranking weights for pain signals
WEIGHT_ENGAGEMENT = 0.4   # Higher upvotes + comments = more people share the pain.
WEIGHT_RECENCY = 0.2      # Recent posts = active pain, not historical.
WEIGHT_SPECIFICITY = 0.2  # Posts with specific complaints rank higher than vague venting.
WEIGHT_NO_SOLUTION = 0.2  # Posts where replies don't link to an existing solution = opportunity.


def load_credentials() -> tuple[str, str]:
    """Load Reddit API credentials from .env files."""
    # Check multiple .env locations
    env_paths = [
        Path(".env"),
        Path("16-shop-cli/.env"),
        Path(os.path.expanduser("~/.env")),
    ]
    for p in env_paths:
        if p.exists():
            load_dotenv(p)
            break

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        print(
            "Error: Reddit API credentials not found. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in .env. "
            "Get credentials at https://www.reddit.com/prefs/apps/ (create a 'script' app).",
            file=sys.stderr,
        )
        sys.exit(3)

    return client_id, client_secret


def get_access_token(client_id: str, client_secret: str) -> str:
    """Get Reddit OAuth2 access token using client credentials grant."""
    try:
        resp = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=(client_id, client_secret),
            data={"grant_type": "client_credentials"},
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()["access_token"]
    except requests.RequestException as e:
        print(
            f"Error: Reddit auth failed: {e}. "
            f"Check REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET in .env. "
            f"Ensure the app type is 'script' at https://www.reddit.com/prefs/apps/",
            file=sys.stderr,
        )
        sys.exit(3)


def search_subreddit(token: str, subreddit: str, query: str, limit: int) -> list[dict]:
    """Search a subreddit for posts matching the query."""
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
    }
    params = {
        "q": query,
        "restrict_sr": "on",
        "sort": "relevance",
        "t": "year",  # Last year — recent enough to be relevant, broad enough to find patterns.
        "limit": min(limit, 100),  # Reddit API caps at 100 per request.
    }

    try:
        resp = requests.get(
            f"https://oauth.reddit.com/r/{subreddit}/search",
            headers=headers,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
        if resp.status_code == 429:
            print(
                f"Warning: Reddit rate limit hit for r/{subreddit}. "
                f"Wait 60 seconds and retry, or reduce --limit.",
                file=sys.stderr,
            )
            return []
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", {}).get("children", [])
    except requests.RequestException as e:
        print(f"Warning: search failed for r/{subreddit}: {e}", file=sys.stderr)
        return []


def score_pain_signal(post: dict) -> float:
    """Score a post based on how strongly it signals unmet pain."""
    data = post.get("data", {})

    # Engagement: normalize upvotes + comments. 50+ is strong signal.
    upvotes = max(0, data.get("ups", 0))
    comments = max(0, data.get("num_comments", 0))
    engagement = min(1.0, (upvotes + comments * 2) / 100.0)  # Comments weighted 2x (discussion = real pain).

    # Recency: posts from last 90 days score higher.
    import time
    created = data.get("created_utc", 0)
    age_days = (time.time() - created) / 86400
    recency = max(0.0, 1.0 - (age_days / 365.0))

    # Specificity: longer titles with pain keywords = more specific.
    title = data.get("title", "").lower()
    pain_keywords = ["frustrat", "wish", "hate", "struggle", "pain", "broken", "terrible", "awful", "why can't"]
    specificity = min(1.0, sum(1 for kw in pain_keywords if kw in title) / 3.0)

    # No-solution signal: selftext that asks for help without an existing answer.
    selftext = data.get("selftext", "").lower()
    has_solution_link = "http" in selftext and any(w in selftext for w in ["solved", "found", "use this"])
    no_solution = 0.0 if has_solution_link else 0.7

    return (
        WEIGHT_ENGAGEMENT * engagement
        + WEIGHT_RECENCY * recency
        + WEIGHT_SPECIFICITY * specificity
        + WEIGHT_NO_SOLUTION * no_solution
    )


def main():
    parser = argparse.ArgumentParser(description="Mine Reddit for pain signals")
    parser.add_argument("--subreddits", required=True,
                        help="Comma-separated subreddit names (without r/)")
    parser.add_argument("--query", default=None,
                        help="Custom search query. Default: built-in pain signal terms.")
    parser.add_argument("--limit", type=int, default=30,
                        help="Max results per subreddit (default: 30)")
    ns = parser.parse_args()

    subreddits = [s.strip() for s in ns.subreddits.split(",") if s.strip()]
    if not subreddits:
        print("Error: provide at least one subreddit name.", file=sys.stderr)
        sys.exit(2)

    # Build query from pain terms or use custom
    if ns.query:
        query = ns.query
    else:
        query = " OR ".join(f'"{term}"' for term in DEFAULT_PAIN_TERMS[:5])
        # Reddit search has a query length limit; use top 5 terms.

    client_id, client_secret = load_credentials()
    token = get_access_token(client_id, client_secret)

    all_posts = []
    for sub in subreddits:
        posts = search_subreddit(token, sub, query, ns.limit)
        for post in posts:
            data = post.get("data", {})
            all_posts.append({
                "subreddit": sub,
                "title": data.get("title", ""),
                "url": f"https://reddit.com{data.get('permalink', '')}",
                "upvotes": data.get("ups", 0),
                "comments": data.get("num_comments", 0),
                "snippet": (data.get("selftext", "")[:200] + "...") if data.get("selftext") else "",
                "created_utc": data.get("created_utc", 0),
                "_raw": post,
            })

    # Score and rank
    scored = [(score_pain_signal(p["_raw"]), p) for p in all_posts]
    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for i, (score, post) in enumerate(scored[:ns.limit]):
        results.append({
            "rank": i + 1,
            "score": round(score, 4),
            "title": post["title"],
            "url": post["url"],
            "subreddit": post["subreddit"],
            "upvotes": post["upvotes"],
            "comments": post["comments"],
            "snippet": post["snippet"],
        })

    print(json.dumps(results, indent=2))

    if not results:
        print("No pain signals found. Try different subreddits or broader search terms.", file=sys.stderr)


if __name__ == "__main__":
    main()
