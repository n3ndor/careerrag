"""Review what real visitors asked the bot and what it answered.

The feedback loop: run this periodically, spot bad or refused answers, and
fix them by adding or improving knowledge-base files (never by hand-editing
answers; the knowledge base is the single source of truth).

Usage:
    python evals/review_questions.py [--days 7] [--refused-only]

Env vars: SUPABASE_URL, SUPABASE_SECRET_KEY
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timedelta, timezone

import httpx


def main() -> int:
    parser = argparse.ArgumentParser(description="Review logged visitor questions")
    parser.add_argument("--days", type=int, default=7, help="lookback window")
    parser.add_argument(
        "--refused-only",
        action="store_true",
        help="only show questions the bot could not answer",
    )
    args = parser.parse_args()

    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SECRET_KEY", "")
    if not url or not key:
        print("error: SUPABASE_URL and SUPABASE_SECRET_KEY must be set", file=sys.stderr)
        return 1

    since = (datetime.now(timezone.utc) - timedelta(days=args.days)).isoformat()
    params = {
        "select": "created_at,question,answered,answer,sources",
        "created_at": f"gt.{since}",
        "order": "created_at.desc",
        "limit": "200",
    }
    if args.refused_only:
        params["answered"] = "eq.false"

    resp = httpx.get(
        f"{url}/rest/v1/careerrag_questions",
        params=params,
        headers={"apikey": key, "Authorization": f"Bearer {key}"},
        timeout=30,
    )
    resp.raise_for_status()
    rows = resp.json()

    print(f"{len(rows)} questions in the last {args.days} days"
          + (" (refused only)" if args.refused_only else "") + "\n")
    for row in rows:
        stamp = row["created_at"][:16].replace("T", " ")
        flag = "ok     " if row["answered"] else "REFUSED"
        print(f"[{stamp}] {flag} Q: {row['question']}")
        answer = row.get("answer") or "(not logged; asked before answer logging)"
        print(f"                       A: {answer[:300]}")
        if row.get("sources"):
            print(f"                       sources: {', '.join(row['sources'])}")
        print()

    refused = [r for r in rows if not r["answered"]]
    if refused and not args.refused_only:
        print(f"--> {len(refused)} refused answers. Knowledge-base gaps or trolling?"
              " Add missing docs for the legitimate ones.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
