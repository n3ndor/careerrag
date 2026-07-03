<div align="center">

# 🎙 CareerRAG

**An AI you can interview about my career.**

A recruiter-facing RAG assistant that answers questions about Nandor Nagy,
grounded in a curated public knowledge base, with citations and honest
"I don't know" handling.

[**▶ Ask it live on nagysolution.com**](https://nagysolution.com)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-pgvector-3FCF8E?logo=supabase&logoColor=white)
![Groq](https://img.shields.io/badge/LLM-Groq-f55036)
![Cost](https://img.shields.io/badge/infra%20cost-%240%2Fmonth-3ddc97)

</div>

---

## What it does

Recruiters read CVs; nobody has interviewed one. CareerRAG lets you ask
"Has Nandor built anything with Stripe?" or "Can he work US hours?" and get a
short grounded answer citing the project, testimonial, or post that backs it.
Ask something outside the knowledge base and it tells you it does not know,
which demonstrates hallucination control better than any claim could.

## Architecture

```
knowledge/ (curated public-safe markdown, this repo)
      │  push triggers GitHub Action
      ▼
Python indexer  (chunk -> embed -> upsert, change-aware)
      │                         embeddings: Supabase Edge Function
      ▼                         running built-in gte-small (384d)
Supabase Postgres + pgvector  (match_careerrag_chunks RPC, cosine)
      ▲
      │  retrieval (top-k + similarity threshold)
Chat on nagysolution.com  ->  Groq (strict grounding prompt + citations)
```

- **One embedding model, one place.** Both the indexer (index time) and the
  chat API (query time) call the same Supabase Edge Function wrapping the
  built-in gte-small model. Mixing embedding models is the classic silent RAG
  failure; this design makes it impossible.
- **Change-aware indexing.** Chunks are content-hashed; a run after editing one
  file embeds only that file's chunks and deletes stale ones.
- **Grounding over fluency.** The generation prompt requires answers only from
  retrieved context, with source citations, and a visible refusal when the
  context is insufficient.
- **Evals against production.** A weekly CI job interrogates the real deployed
  endpoint (not a mock) with 33 cases across four categories and publishes the
  results, failures included, in [`evals/RESULTS.md`](evals/RESULTS.md). Safety
  categories (out-of-scope, compensation, adversarial) gate at 100%; grounded
  questions gate at 80%. The suite caught a prompt-injection leak before
  launch; that attack is now a permanent regression test.
- **Self-refreshing knowledge.** A weekly cron regenerates the GitHub section
  of the knowledge base from the public API and commits it, which triggers
  re-indexing. The bot stays current about public repos with zero manual work.

## Repository layout

```
knowledge/           the knowledge base (markdown + frontmatter)
  profile/           pitch, work history, skills, education, current work
  projects/          one deep-dive per portfolio project
  testimonials/      what CIOs, leads, and mentors wrote
  posts/             published LinkedIn posts
  faq/               recruiter questions, answered
  github/            auto-generated from the GitHub API (weekly cron)
indexer/             Python: frontmatter parsing, chunking, embedding, upsert
evals/               33 cases + runner hitting the production endpoint
supabase/            schema (pgvector + match RPC) and the embed edge function
.github/workflows/   index on push · weekly github-refresh · weekly evals
```

## Running locally

```bash
cd indexer
python -m venv .venv && .venv/Scripts/pip install -e .[dev]
.venv/Scripts/python -m pytest -q          # tests, no network
.venv/Scripts/python -m indexer.main --dry-run   # parse + chunk, no network
```

A full indexing run needs `SUPABASE_URL` and `SUPABASE_SECRET_KEY` set.

## Status

- [x] Knowledge base v1 (25 curated documents)
- [x] Indexer: chunking, hashing, change-aware embedding, stale cleanup
- [x] Supabase schema: pgvector, HNSW index, similarity RPC, read-only RLS
- [x] Chat API + UI live on nagysolution.com: grounded Groq generation with
      citations, per-IP rate limiting, model fallback on free-tier 429s
- [x] Eval suite: 33 cases (grounded / out-of-scope / compensation /
      adversarial) against the production endpoint, weekly, results in
      [`evals/RESULTS.md`](evals/RESULTS.md)
- [x] Weekly GitHub auto-refresh of `knowledge/github/`

---

<div align="center">

Built by [**Nandor Nagy**](https://github.com/n3ndor) · part of a public portfolio.<br>
The knowledge base is deliberately public: the bot can only say what you can read here.

</div>
