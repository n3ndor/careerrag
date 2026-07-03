"""Regenerate knowledge/github/repos.md from the public GitHub API.

Runs on a weekly cron (see .github/workflows/github-refresh.yml). The commit
it produces triggers the index workflow, so the chat stays current about
public repos with zero manual work.

Usage:
    python -m indexer.github_refresh
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import httpx

USER = "n3ndor"
MAX_REPOS = 12


def fetch_repos() -> list[dict]:
    resp = httpx.get(
        f"https://api.github.com/users/{USER}/repos",
        params={"sort": "pushed", "per_page": 100, "type": "owner"},
        headers={"Accept": "application/vnd.github+json"},
        timeout=30,
    )
    resp.raise_for_status()
    repos = [r for r in resp.json() if not r["fork"] and not r["private"]]
    return repos[:MAX_REPOS]


def render(repos: list[dict]) -> str:
    today = date.today().isoformat()
    lines = [
        "---",
        "id: github-repos",
        "title: Public GitHub repositories (auto-generated)",
        "type: github",
        f"source_url: https://github.com/{USER}",
        f"updated: {today}",
        "---",
        "",
        f"Nandor's public repositories at github.com/{USER}, most recently active",
        f"first. This list is regenerated automatically every week (last: {today}).",
        "",
    ]
    for r in repos:
        desc = (r["description"] or "No description.").strip()
        lang = r["language"] or "n/a"
        pushed = (r["pushed_at"] or "")[:10]
        stars = r["stargazers_count"]
        lines += [
            f"## {r['name']}",
            "",
            f"{desc}",
            f"Main language: {lang}. Last activity: {pushed}."
            + (f" Stars: {stars}." if stars else ""),
            f"Link: {r['html_url']}",
            "",
        ]
    return "\n".join(lines)


def main() -> int:
    repos = fetch_repos()
    out = Path(__file__).resolve().parents[2] / "knowledge" / "github" / "repos.md"
    out.write_text(render(repos), encoding="utf-8")
    print(f"wrote {out} ({len(repos)} repos)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
