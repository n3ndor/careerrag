---
id: work-creator-linkup
title: Creator Linkup - Full Stack Automation Engineer (May 2025 - September 2026)
type: profile
updated: 2026-10-02
---

Nandor worked at Creator Linkup, an influencer marketing company in Germany
(remote), as a Full Stack Automation Engineer from May 2025 to September 2026.

What he built there:

- 65+ production n8n workflows with AI integrations, including customer-facing
  chatbots and RAG knowledge systems.
- These automations reduced manual operational work from around 16 hours per week
  to 2-3 hours per employee.
- A one-click outreach pipeline. Coworkers picked an audience in a schema-driven
  trigger table (region, age, gender, and per-brand eligibility rules, for example
  a period-care brand only reaching women aged 18 to 40). The workflow then
  scraped profiles, checked duplicates, drafted a personal message and loaded the
  lead into Smartlead.
- A PostgreSQL database with 19 relational tables holding 120k+ rows. When older
  contacts were imported, their different shape (agency names instead of persons,
  several handles per person) broke deduplication and 1,000+ leads had to be
  checked by hand. He rebuilt the model around the person: many social handles and
  emails per identity, collaboration history scoped per brand, and a rebooking
  message instead of cold outreach for anyone who had already worked with them.
- An internal Next.js dashboard that brought Google Sheets, Asana, Monday, Front
  and the outreach trigger table under one roof.
- Onboarded 4 new clients and 5 co-workers, handling IT infrastructure and
  workflow setup.

He shipped new features to production every 1 to 2 weeks throughout the
build-out. A deliberate design goal was self-sufficiency: the automation
ecosystem he built is documented and easy to maintain, so it runs the company's
operations with minimal day-to-day engineering. He considers working himself out
of the daily loop a feature of good automation, not a risk.
