# CareerRAG eval results

Run: 2026-11-16 16:34 UTC against `https://www.nagysolution.com/api/ask`

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
  - A: I don't have that in Nandor's public knowledge base. You can reach out to nandor@nagysolution.com for more details.
- `manager-quotes` (grounded): cited ['testimonial-torres', 'faq-personal', 'testimonial-vice'], expected one of ['testimonial-peacock', 'testimonial-cordova', 'faq-how-i-work']
  - Q: What do former managers say about him?
  - A: Former managers highlight Nandor’s technical skill, relentless curiosity, and exceptional character. Brendan Cordova, Lead Full Stack Developer at 3BX and Sojourn, said: “What truly distinguishes Nand
