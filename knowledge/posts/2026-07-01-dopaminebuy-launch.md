---
id: post-dopaminebuy-launch
title: LinkedIn post - dopaminebuy launch (July 1, 2026)
type: post
updated: 2026-07-03
---

Published on LinkedIn on July 1, 2026:

I built a shop where everything is fake and nothing ships. On purpose.

In Korea, "fake shopping" sites went viral: stores that exist purely for the
feeling of buying, made for people who love to shop more than they can afford to.
I turned that idea into a complete product.

dopaminebuy is a shopping game (PWA). You get $2,000 of play money, you buy
things you could never afford, you wait for a real-time delivery, you rip the box
open, and you keep everything in your vault. Daily missions, collection sets, a
mystery box every 6 hours, and items that sell out until tomorrow keep you coming
back.

The engineering part is what I'm most proud of:

- React 19 + TypeScript + Tailwind, installable as an app on your phone
- Runs 100% serverless on Cloudflare (Workers + D1). No backend server. Running
  cost: $0/month
- Real Stripe payments with verified webhooks, in test mode. Going live with real
  money is one config change
- Built in collaboration with agentic AI (Claude Code): the AI wrote the code and
  audited its own work, I directed the product, tested on devices, and made the
  calls. Empty folder to finished app in ~45 iterations

Play it: https://dopaminebuy.nagysolution.com
