# CareerRAG eval results

Run: 2026-11-23 18:55 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 25 | 28 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 38/41**

## Failures (kept honest, not hidden)

- `stripe` (grounded): missing all of: ['stripe']
  - Q: Has Nandor built anything with Stripe?
  - A: I don't have that in Nandor's public knowledge base. You can reach out to nandor@nagysolution.com for more details.
- `current-work` (grounded): missing all of: ['jobfeeds', 'belegradar', 'careerrag']
  - Q: What is Nandor working on right now?
  - A: Nandor is currently dividing his time between freelance client work and his own Shopify‑app products, while also being open to a new full‑time role, contract or engagement.  

**Freelance client work*
- `degree` (grounded): cited ['profile-background-story', 'faq-personal', 'testimonial-soteropulos'], expected one of ['profile-education']
  - Q: Does he have a university degree?
  - A: Yes, Nandor holds a Bachelor of Science in Mathematics and Computer Science from Aurel Vlaicu University in Arad, Romania (2008‑2011). SOURCES: profile-education
