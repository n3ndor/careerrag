---
id: faq-ai-tools
title: FAQ - How Nandor works with AI tools
type: faq
updated: 2026-07-03
---

## Does he use AI coding tools?

Yes, deliberately and transparently. Nandor builds production systems with
agentic AI (Claude Code) as a pair programmer: the AI writes and audits code
while he directs the product, reviews the output, tests on real devices, and
makes the engineering decisions. dopaminebuy went from empty folder to finished
PWA in about 45 iterations this way; JobRadar went from empty folder to
production in 48 hours.

He treats AI as a force multiplier, not a replacement for engineering judgment:
his projects ship with test suites in CI, published evaluation results, and
honest documentation of limitations.

## What AI engineering has he done beyond coding tools?

- 100+ production n8n workflows with AI integrations, including customer-facing
  chatbots and RAG knowledge systems at Creator Linkup.
- LLM structured extraction in JobRadar (summaries, salary parsing, tag
  verification against full job descriptions).
- CareerRAG, the grounded retrieval-augmented chat assistant answering these
  questions right now.
- Works with the Claude API, OpenAI API, and Groq; builds provider-swappable
  abstractions so no single LLM vendor is a hard dependency.
