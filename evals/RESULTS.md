# CareerRAG eval results

Run: 2026-09-07 13:11 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 23 | 24 |
| out_of_scope | 5 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 35/37**

## Failures (kept honest, not hidden)

- `stripe` (grounded): cited ['post-careerrag-launch', 'faq-how-i-work', 'work-3bx'], expected one of ['work-sojourn', 'project-dopaminebuy', 'post-dopaminebuy-launch', 'profile-current-work']
  - Q: Has Nandor built anything with Stripe?
  - A: Yes. Nandor built “dopaminebuy,” a fake‑shopping game PWA that includes Stripe checkout integration. SOURCES: profile-current-work
- `google` (out_of_scope): expected a refusal / no-info answer
  - Q: Has he ever worked at Google?
  - A: I don’t have any record of Nandor working at Google. If you need confirmation, you can reach out to him directly at nandor@nagysolution.com.
