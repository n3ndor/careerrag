---
id: project-swaprika
title: Swaprika - what to use instead of a missing ingredient
type: project
source_url: https://swaprika.nagysolution.com
updated: 2026-09-25
---

Swaprika is a fun public project: an ingredient substitution finder, live at
https://swaprika.nagysolution.com and open source at
https://github.com/n3ndor/swaprika (MIT licence, code and data).

The idea came from a familiar moment: Sunday evening, the oven is warm, and one
ingredient is missing. A search engine gives fourteen tabs and a generic "just use
oil". Swaprika asks two things, what you are making and what ran out, and shows
only the swaps that work for that dish: how much to use, what the swap keeps and
loses, what turns out different, what to adjust, and which dishes it fails in.
Butter becomes oil in a cake, but not in a croissant.

It holds 49 ingredients in six families and 133 swaps across 44 dishes and
techniques. The dataset is common kitchen knowledge written by hand. There is no
account, no backend and no ads.

## Stack

Astro with a single React island for the finder. All animation, including the
flying pepper on the cover, is plain CSS. The site is served as static files from
Cloudflare, so it costs nothing to run and has no request limits. An earlier
version served the data from a GraphQL API on Cloudflare Workers and D1 with plan
based access; it was dropped in favour of a static site and is kept at a git tag.

## What it shows

Product and interface craft on a small, well scoped idea: a clear two step flow,
honest limits on every card, and polish in the details rather than in features.
