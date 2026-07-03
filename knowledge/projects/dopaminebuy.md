---
id: project-dopaminebuy
title: dopaminebuy - a fake shopping game PWA
type: project
source_url: https://dopaminebuy.nagysolution.com
updated: 2026-07-03
---

dopaminebuy is a public portfolio project, live at
https://dopaminebuy.nagysolution.com, launched July 2026.

## What it is

A shopping game inspired by Korea's viral "fake shopping" sites: stores that
exist purely for the feeling of buying. Players get $2,000 of play money, buy
things they could never afford, wait for a real-time delivery, unbox items, and
keep everything in a vault. Daily missions, collection sets, a mystery box every
6 hours, and items that sell out until tomorrow drive retention.

## Engineering highlights

- React 19 + TypeScript + Tailwind, installable as a PWA on phones.
- Runs 100% serverless on Cloudflare (Workers + D1). No backend server. Running
  cost: $0/month.
- Real Stripe payment integration with verified webhooks, in test mode; going
  live with real money is one config change.
- Built in collaboration with agentic AI (Claude Code): the AI wrote and audited
  code, Nandor directed the product, tested on devices, and made the decisions.
  Empty folder to finished app in about 45 iterations.

## What it proves

Product sense, consumer PWA engineering, Cloudflare Workers/D1, Stripe
integration, and an effective AI-assisted development workflow.
