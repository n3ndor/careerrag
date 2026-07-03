---
id: project-jobradar
title: JobRadar - automated tech-job market intelligence
type: project
source_url: https://jobradar.nagysolution.com
updated: 2026-07-03
---

JobRadar is a public portfolio project, live at https://jobradar.nagysolution.com
with code at https://github.com/n3ndor/jobradar. Built solo in about 48 hours in
July 2026, then hardened from real use.

## What it is

A Python pipeline ingests postings from six public job APIs every six hours
(Remotive, Arbeitnow, Greenhouse boards, RemoteOK, We Work Remotely, and the
Hacker News "Who is hiring" thread), dedupes them across sources, and tags every
role by region, remote policy, seniority, and tech stack. A Next.js dashboard
surfaces market trends: 1,150+ live tech roles, sliceable, with every search a
shareable URL.

## The AI layer

An LLM (Groq, provider-swappable) reads every posting's full description and:

1. Compresses recruiter prose into one-line summaries.
2. Parses salaries out of prose ("80-95k EUR depending on experience" becomes
   filterable structured data). Never invented: no stated salary means an empty
   field.
3. Corrects wrong remote/region tags: postings flagged "remote" whose text says
   "Available Locations: Munich" get fixed automatically.

The LLM is never a hard dependency: if the key is missing or rate-limited, the
pipeline completes on a deterministic rules layer and catches up later, visibly,
on the public /pipeline observability page.

## Engineering highlights

- Two-layer enrichment: deterministic rules always run; the LLM is an
  opportunistic upgrade.
- Provider-agnostic LLM abstraction (swapping providers is a config change).
- Designed for free tiers: bounded batches, resumable backfills, per-source
  failure isolation. Total infrastructure cost: $0/month.
- 60 pytest tests (API adapters mocked with respx) running in CI.
- Stack: Python 3.12 (httpx, pydantic, supabase-py) on a GitHub Actions cron;
  Next.js 16, TypeScript, Tailwind 4 on Vercel; Supabase Postgres with row level
  security.

## What it proves

Python data pipelines, LLM structured extraction, CI/CD, honest engineering
around free-tier constraints, and data visualization.
