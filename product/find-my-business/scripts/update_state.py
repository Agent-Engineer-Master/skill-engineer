#!/usr/bin/env python3
"""
update_state.py — Initialize or update the business search state file.

Adapted from log_run.py archetype. Manages the persistent state.json that tracks
the founder's progress through the idea discovery process.

Usage:
  python scripts/update_state.py --action init
  python scripts/update_state.py --action update --phase ideation --data '{"ideas_active": 5}'
  python scripts/update_state.py --action add-idea --data '{"name": "AI tutoring", "angle": "personal_pain", "status": "active"}'
  python scripts/update_state.py --action kill-idea --data '{"name": "AI tutoring", "reason": "violates anti-goal: operational grind"}'
  python scripts/update_state.py --action log-stuck --data '{"pattern": "analysis_paralysis", "intervention": "forced_decision"}'

Output: Updated state summary to stdout.

Error taxonomy:
  exit 0 — state updated successfully
  exit 1 — file write failed (permissions, disk)
  exit 2 — bad arguments or invalid JSON
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# State file lives in the project exploration directory, not the skill folder.
# This keeps state with the founder's work, not the skill's code.
DEFAULT_STATE_PATH = "03-exploration/business-search/state.json"  # relative to project root


def load_state(path: Path) -> dict:
    """Load existing state or return empty dict."""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read state at {path}: {e}. Starting fresh.", file=sys.stderr)
        return {}


def save_state(path: Path, state: dict) -> None:
    """Write state atomically (write to tmp, rename)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def init_state() -> dict:
    """Create a fresh state file for a new business search."""
    return {
        "version": 1,
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "modified": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "phase": "profile",  # profile | ideation | validation | deep-validation | committed
        "sessions": 1,
        "ideas": [],  # list of idea objects
        "decisions": [],  # list of decision log entries
        "stuck_patterns": [],  # list of detected stuck patterns
    }


def update_phase(state: dict, phase: str, extra: dict) -> dict:
    """Update the current phase and merge extra data."""
    valid_phases = ["profile", "ideation", "validation", "deep-validation", "committed"]
    if phase not in valid_phases:
        print(f"Error: phase must be one of {valid_phases}. Got '{phase}'.", file=sys.stderr)
        sys.exit(2)
    state["phase"] = phase
    state["modified"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    state["sessions"] = state.get("sessions", 0) + 1
    # Merge any extra top-level keys from data
    for k, v in extra.items():
        if k not in ("phase", "version", "created"):  # protect core fields
            state[k] = v
    return state


def add_idea(state: dict, idea_data: dict) -> dict:
    """Add a new idea to the tracker."""
    if "name" not in idea_data:
        print("Error: idea must have a 'name' field.", file=sys.stderr)
        sys.exit(2)
    idea = {
        "name": idea_data["name"],
        "angle": idea_data.get("angle", "unknown"),  # which generation angle produced it
        "status": "active",  # active | testing | killed | committed
        "added": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "score": idea_data.get("score"),
        "notes": idea_data.get("notes", ""),
    }
    state.setdefault("ideas", []).append(idea)
    state["modified"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return state


def kill_idea(state: dict, kill_data: dict) -> dict:
    """Mark an idea as killed with a reason."""
    name = kill_data.get("name")
    reason = kill_data.get("reason", "no reason given")
    if not name:
        print("Error: kill-idea requires a 'name' field.", file=sys.stderr)
        sys.exit(2)
    found = False
    for idea in state.get("ideas", []):
        if idea["name"].lower() == name.lower():
            idea["status"] = "killed"
            idea["killed_reason"] = reason
            idea["killed_date"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            found = True
            break
    if not found:
        print(f"Warning: idea '{name}' not found in state. Logging decision anyway.", file=sys.stderr)
    state.setdefault("decisions", []).append({
        "action": "kill",
        "idea": name,
        "reason": reason,
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    })
    state["modified"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return state


def log_stuck(state: dict, stuck_data: dict) -> dict:
    """Log a detected stuck pattern and intervention."""
    entry = {
        "pattern": stuck_data.get("pattern", "unknown"),
        "intervention": stuck_data.get("intervention", ""),
        "outcome": stuck_data.get("outcome", "TBD"),
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    state.setdefault("stuck_patterns", []).append(entry)
    state["modified"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return state


def summarize(state: dict) -> str:
    """One-paragraph summary of current state."""
    phase = state.get("phase", "unknown")
    sessions = state.get("sessions", 0)
    ideas = state.get("ideas", [])
    active = [i for i in ideas if i.get("status") == "active"]
    testing = [i for i in ideas if i.get("status") == "testing"]
    killed = [i for i in ideas if i.get("status") == "killed"]
    committed = [i for i in ideas if i.get("status") == "committed"]

    parts = [f"Phase: {phase} | Sessions: {sessions}"]
    if active:
        parts.append(f"Active ideas: {len(active)} ({', '.join(i['name'] for i in active)})")
    if testing:
        parts.append(f"Testing: {len(testing)} ({', '.join(i['name'] for i in testing)})")
    if killed:
        parts.append(f"Killed: {len(killed)}")
    if committed:
        parts.append(f"Committed: {committed[0]['name']}")
    return " | ".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Manage business search state")
    parser.add_argument("--action", required=True,
                        choices=["init", "update", "add-idea", "kill-idea", "log-stuck", "summary"],
                        help="Action to perform")
    parser.add_argument("--state-file", default=DEFAULT_STATE_PATH,
                        help="Path to state.json (default: 03-exploration/business-search/state.json)")
    parser.add_argument("--phase", default="",
                        help="Phase to set (for 'update' action)")
    parser.add_argument("--data", default="{}",
                        help="JSON string with extra data to merge")
    ns = parser.parse_args()

    try:
        extra = json.loads(ns.data)
    except json.JSONDecodeError as e:
        print(f"Error: --data is not valid JSON: {e}. Pass a valid JSON object.", file=sys.stderr)
        sys.exit(2)

    state_path = Path(ns.state_file)
    state = load_state(state_path)

    if ns.action == "init":
        if state:
            print(f"Warning: state file already exists at {state_path}. Use 'update' to modify.", file=sys.stderr)
            print(summarize(state))
            return
        state = init_state()
        save_state(state_path, state)
        print(f"Initialized: {summarize(state)}")

    elif ns.action == "update":
        if not state:
            print(f"Error: no state file at {state_path}. Run --action init first.", file=sys.stderr)
            sys.exit(1)
        phase = ns.phase or state.get("phase", "profile")
        state = update_phase(state, phase, extra)
        save_state(state_path, state)
        print(f"Updated: {summarize(state)}")

    elif ns.action == "add-idea":
        if not state:
            print(f"Error: no state file at {state_path}. Run --action init first.", file=sys.stderr)
            sys.exit(1)
        state = add_idea(state, extra)
        save_state(state_path, state)
        print(f"Added idea: {extra.get('name', '?')} | {summarize(state)}")

    elif ns.action == "kill-idea":
        if not state:
            print(f"Error: no state file at {state_path}. Run --action init first.", file=sys.stderr)
            sys.exit(1)
        state = kill_idea(state, extra)
        save_state(state_path, state)
        print(f"Killed: {extra.get('name', '?')} | {summarize(state)}")

    elif ns.action == "log-stuck":
        if not state:
            print(f"Error: no state file at {state_path}. Run --action init first.", file=sys.stderr)
            sys.exit(1)
        state = log_stuck(state, extra)
        save_state(state_path, state)
        print(f"Logged stuck pattern: {extra.get('pattern', '?')}")

    elif ns.action == "summary":
        if not state:
            print("No state file found. Run /find-my-business to start.")
            return
        print(summarize(state))


if __name__ == "__main__":
    main()
