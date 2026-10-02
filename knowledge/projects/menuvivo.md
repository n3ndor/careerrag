---
id: project-menuvivo
title: MenuVivo - multi-tenant business pages for small businesses in Paraguay
type: project
source_url: https://menuvivo.nagysolution.com
updated: 2026-10-02
---

MenuVivo is Nandor's own product: a multi-tenant platform that sells simple
business pages to home kitchens, bakeries and small service businesses in
Paraguay. A public demo with three fictional businesses is live at
https://menuvivo.nagysolution.com.

Each client gets a public page with the week's menu or offers, orders confirmed
on WhatsApp, and an own admin panel on their own subdomain or domain. Nandor has
a superadmin panel with a client overview, user management, leads from the
landing form and downloadable reports. The interface is in Spanish and English.

The key design decision: one deployment serves every client, so a new client is
a database row, not a new site, and clients host nothing. Stack: Node.js, Hono,
SQLite.
