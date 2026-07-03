---
id: project-careerrag
title: CareerRAG - this AI assistant
type: project
source_url: https://github.com/n3ndor/careerrag
updated: 2026-07-03
---

CareerRAG is the AI assistant you are talking to right now. It answers questions
about Nandor Nagy's career, grounded in a curated public knowledge base, with
citations. It is itself a portfolio project demonstrating retrieval-augmented
generation (RAG) built the way production systems need it.

## How it works

- A curated knowledge base of public-safe markdown files (profile, projects,
  testimonials, published posts, FAQ) lives in a public git repo.
- A Python indexing pipeline chunks the files, generates embeddings with
  Supabase's built-in gte-small model, and upserts them into Supabase Postgres
  with pgvector. It re-runs automatically on every push via GitHub Actions.
- The chat on nagysolution.com retrieves the most relevant chunks by cosine
  similarity and asks an LLM (Groq) to answer strictly from that context, with
  citations. If the context does not contain the answer, it says so instead of
  guessing.
- An automated evaluation suite tests grounded answers, refusal behavior on
  out-of-scope questions, and resistance to prompt injection.

## What it proves

RAG architecture, embeddings and vector search, hallucination control, eval
discipline, and running an AI product on $0/month infrastructure.
