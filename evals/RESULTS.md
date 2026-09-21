# CareerRAG eval results

Run: 2026-09-21 13:29 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 22 | 24 |
| out_of_scope | 5 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 34/37**

## Failures (kept honest, not hidden)

- `stripe` (grounded): cited ['post-careerrag-launch', 'faq-how-i-work', 'work-3bx'], expected one of ['work-sojourn', 'project-dopaminebuy', 'post-dopaminebuy-launch', 'profile-current-work']
  - Q: Has Nandor built anything with Stripe?
  - A: Yes. Nandor created the “dopaminebuy” fake‑shopping game PWA, which includes Stripe checkout integration. SOURCES: profile-current-work
- `manager-quotes` (grounded): cited ['testimonial-torres', 'faq-personal', 'testimonial-vice'], expected one of ['testimonial-peacock', 'testimonial-cordova', 'faq-how-i-work']
  - Q: What do former managers say about him?
  - A: Former managers highlight Nandor’s technical skill, relentless curiosity, and exceptional character. Brendan Cordova, Lead Full‑Stack Developer at 3BX and Sojourn, wrote: “What truly distinguishes Nan
- `google` (out_of_scope): expected a refusal / no-info answer
  - Q: Has he ever worked at Google?
  - A: I don’t have any record of Nandor working at Google. If you need confirmation, you can reach out to him directly at nandor@nagysolution.com.
