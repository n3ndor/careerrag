# CareerRAG eval results

Run: 2026-09-28 17:09 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 27 | 28 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 40/41**

## Failures (kept honest, not hidden)

- `stripe` (grounded): missing all of: ['stripe']
  - Q: Has Nandor built anything with Stripe?
  - A: I don't have that in Nandor's public knowledge base. You can reach out to nandor@nagysolution.com for more information.
