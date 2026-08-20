#!/usr/bin/env python3
"""Rank pre-audited skill candidates from JSON without network access."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

WEIGHTS = {
    "task_fit": 30,
    "source_trust": 20,
    "security_fit": 15,
    "maintenance": 10,
    "validation": 10,
    "efficiency": 10,
    "adoption": 5,
}
HARD_GATES = ("license_ok", "inspectable", "pinned", "safe_actions", "rollback")


def rank(candidate: dict) -> dict:
    failed = [gate for gate in HARD_GATES if candidate.get(gate) is not True]
    values = candidate.get("scores", {})
    invalid = [
        key
        for key in WEIGHTS
        if not isinstance(values.get(key), (int, float)) or not 0 <= values[key] <= 1
    ]
    if failed or invalid:
        return {
            **candidate,
            "score": 0,
            "decision": "reject",
            "failed_gates": failed,
            "invalid_scores": invalid,
        }
    score = round(sum(values[key] * weight for key, weight in WEIGHTS.items()), 1)
    decision = "select" if score >= 75 else "experiment" if score >= 60 else "reject"
    return {
        **candidate,
        "score": score,
        "decision": decision,
        "failed_gates": [],
        "invalid_scores": [],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON array of audited candidates")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("input must be a JSON array")
    result = sorted(
        (rank(item) for item in data), key=lambda item: item["score"], reverse=True
    )
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
