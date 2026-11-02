# CareerRAG eval results

Run: 2026-11-02 16:44 UTC against `https://www.nagysolution.com/api/ask`

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
- `manager-quotes` (grounded): cited ['testimonial-torres', 'faq-personal', 'testimonial-vice'], expected one of ['testimonial-peacock', 'testimonial-cordova', 'faq-how-i-work']
  - Q: What do former managers say about him?
  - A: Former managers highlight Nandor’s technical skill, relentless curiosity, and outstanding character. Brendan Cordova, Lead Full‑Stack Developer at 3BX and Sojourn, wrote: “What truly distinguishes Nan
- `current-work` (grounded): missing all of: ['jobfeeds', 'belegradar', 'careerrag']
  - Q: What is Nandor working on right now?
  - A: Nandor is currently dividing his time between freelance client work and his own Shopify‑app products, while also being open to a new full‑time role or contract.  

**Freelance client work**  
- Ongoin
