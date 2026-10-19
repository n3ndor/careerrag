# CareerRAG eval results

Run: 2026-10-19 14:06 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 26 | 28 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 39/41**

## Failures (kept honest, not hidden)

- `stripe` (grounded): missing all of: ['stripe']
  - Q: Has Nandor built anything with Stripe?
  - A: I don't have that in Nandor's public knowledge base. You can reach out to nandor@nagysolution.com for more information.
- `current-work` (grounded): missing all of: ['jobfeeds', 'belegradar', 'careerrag']
  - Q: What is Nandor working on right now?
  - A: Nandor is currently dividing his time between freelance client work and his own Shopify‑app products, while also being open to a new full‑time role, contract or engagement.  

**Freelance client work*
