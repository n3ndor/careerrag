---
id: post-careerrag-launch
title: LinkedIn post - CareerRAG launch (drafted July 2026)
type: post
updated: 2026-08-10
---

Drafted for LinkedIn in July 2026, planned to publish about a week after the
JobRadar post. Not yet published as of this writing.

Recruiters read 200 CVs a day. Mine answers questions.

I built an AI you can interview about my career. It lives on my portfolio, it
only knows my public professional data, and every answer comes with sources:
the project, testimonial, or post that backs it up.

Ask it "Has Nandor built anything with Stripe?" and it cites the exact
projects. Ask it "Has he worked at Google?" and it says it doesn't know.
That refusal is the feature I'm most proud of. Anyone can make an LLM talk;
making it admit what it doesn't know is the engineering part.

How it works:

A public knowledge base of curated markdown files (work history, projects,
testimonials, FAQ) lives in a git repo. Anyone can read exactly what the bot
knows.

A Python indexer chunks and embeds it into Supabase pgvector on every push.
One embedding model at index time and query time, enforced by design, because
mixing models is the classic silent RAG failure.

The chat retrieves the best chunks and Groq answers under a strict grounding
prompt: context only, cite sources, refuse when unsure, never state salary
figures.

An automated eval suite interrogates the production endpoint every week:
grounded questions, out-of-scope questions, prompt injection attacks. Results
are published in the repo, failures included.

The eval suite already caught a real bug before launch: a prompt injection
that leaked my system prompt. Fixed, and now there's a regression test for it.

Runs on 0 EUR/month: Supabase free tier, Groq free tier, Vercel Hobby.

Try to break it: https://nagysolution.com
Code + knowledge base + eval results: https://github.com/n3ndor/careerrag

Tags: #buildinpublic #ai #rag #llm #python #nextjs #supabase #agenticai
#recruiting
