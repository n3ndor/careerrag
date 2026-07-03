---
id: post-jobradar-launch
title: LinkedIn post - JobRadar launch (July 3, 2026)
type: post
updated: 2026-07-03
---

Published on LinkedIn on July 3, 2026:

I built a radar for the tech job market.

Job boards show you one listing at a time. JobRadar watches the whole market.

Every 6 hours, an automated pipeline pulls fresh postings from Remotive,
Arbeitnow, Greenhouse, RemoteOK, We Work Remotely and the Hacker News "Who is
hiring" thread, dedupes them across sources, and tags every role by region,
remote policy, seniority and tech stack. 1,150+ live tech roles, sliceable. And
every search is a shareable URL.

The part I'm most proud of is the AI layer. An LLM reads every posting's full
description and does three things no regex ever could:

- Compresses walls of recruiter prose into one-line summaries
- Finds "80-95k EUR depending on experience" buried in paragraph four and turns
  it into filterable salary data (never invented; if no salary is stated, the
  field stays honest and empty)
- Catches job boards lying. Postings flagged "remote" while the text says "an
  unseren Standorten" or "Available Locations: Munich" get corrected
  automatically.

And the whole thing runs on 0 euros per month: Python 3.12 pipeline (httpx +
pydantic) on a GitHub Actions cron, Next.js 16 + TypeScript + Tailwind on Vercel,
Supabase Postgres behind row level security, LLM enrichment via Groq free tier
(provider swappable with one env var), 60 pytest tests running in CI.

Built with Claude Code as my pair programmer, from empty folder to production in
48 hours.

Live: https://jobradar.nagysolution.com
Code: https://github.com/n3ndor/jobradar
