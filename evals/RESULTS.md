# CareerRAG eval results

Run: 2026-08-31 14:35 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 22 | 24 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 35/37**

## Failures (kept honest, not hidden)

- `stripe` (grounded): cited ['post-careerrag-launch', 'faq-how-i-work', 'work-3bx'], expected one of ['work-sojourn', 'project-dopaminebuy', 'post-dopaminebuy-launch', 'profile-current-work']
  - Q: Has Nandor built anything with Stripe?
  - A: Yes. Nandor built “dopaminebuy,” a fake‑shopping game PWA that includes Stripe checkout, launched on July 1 2026. SOURCES: profile-current-work
- `manager-quotes` (grounded): cited ['testimonial-torres', 'faq-personal', 'testimonial-vice'], expected one of ['testimonial-peacock', 'testimonial-cordova', 'faq-how-i-work']
  - Q: What do former managers say about him?
  - A: Former managers highlight Nandor’s technical skill, relentless curiosity, and exceptional character. Brendan Cordova, Lead Full‑Stack Developer at 3BX and Sojourn, wrote: “What truly distinguishes Nan
