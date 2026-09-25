---
id: project-shopify-apps
title: Nasolv Shopify apps - two published App Store products
type: project
source_url: https://apps.shopify.com/partners/nagy-solution
updated: 2026-09-25
---

Nandor builds and sells his own Shopify apps under the brand **Nasolv** (from
Nagy Solution). Two are published on the Shopify App Store, both reviewed and
approved by Shopify in September 2026. These are products, not client work: he
owns the code, the hosting, the pricing and the support.

## Nasolv Accessibility Scan

Live at https://apps.shopify.com/accessibility-audit, published 14 September
2026. Product page: https://accessibility.nagysolution.com

It loads a merchant's storefront in a real browser (Playwright) and tests it
against WCAG 2.2 AA, the standard behind the European Accessibility Act, the
German BFSG and the American ADA. Every failure is reported with the element
that caused it. Findings a machine cannot decide are kept in a separate bucket
instead of being counted as passes, and scheduled re-scans email the merchant
when a page that was previously clean starts failing.

The app deliberately does not claim to make a store compliant, and adds nothing
to the storefront: no overlay, no widget, no injected script. That position is a
reaction to a competitor being fined one million dollars by the FTC in January
2025 for overclaiming. The admin interface is available in English, German,
Spanish, French and Italian.

## Nasolv Reorder

Live at https://apps.shopify.com/nasolv-reorder, published 11 September 2026.
Product page: https://reorder.nagysolution.com

It answers one question for small retailers: what to reorder, how much and the
date to order by. The interesting constraint is that Shopify's API returns only
60 days of order history, which is not enough to forecast with, so the app takes
a nightly snapshot and accumulates its own history over time. Where the sales
history is too short to forecast, it says that plainly rather than printing a
number it cannot support. It does not build purchase orders, because Shopify
ships those for free.

## In development: marketplace connectors

Two more apps are being built, both connecting a Shopify store to a European
marketplace so a merchant can sell there without an ERP. Neither is on the App
Store yet.

- **Kaufland connector.** Lists Shopify products on Kaufland by barcode (EAN),
  keeps stock in sync in both directions, imports Kaufland orders into Shopify and
  sends tracking numbers back. Planned for all nine Kaufland storefronts: Germany,
  Austria, Czechia, Slovakia, Poland, France, Italy, Spain and the Netherlands.
- **eMAG connector.** The same kind of sync for eMAG, the largest online
  marketplace in Romania, Hungary and Bulgaria. The app will be in Romanian and
  Hungarian, two of the languages Nandor speaks. As of September 2026 no live
  Shopify app syncs eMAG orders; the one earlier connector was withdrawn from the
  App Store.

## Stack and operations

Remix and TypeScript, Shopify Polaris for the admin UI, Prisma and PostgreSQL,
Playwright and axe-core for the scanning engine, Docker Compose behind Traefik
on a VPS in Frankfurt, with Shopify handling billing and webhooks. Nandor runs
the deployments, the backups, the cron jobs and the support himself.

## What it proves

End-to-end product ownership rather than delivery against someone else's spec:
market research, App Store review, subscription billing, GDPR-relevant hosting
decisions, multi-language product copy, and operating a paid service for
merchants he has never met.

## Honest status

Both apps are new and have no reviews yet, which is normal for a recently listed
app: roughly 57 percent of the 25,000 apps on the Shopify App Store have zero
reviews. Nandor tracks each app against a fixed kill date rather than keeping
something alive out of attachment. Ask him directly for current install or
revenue numbers, they are not published here.
