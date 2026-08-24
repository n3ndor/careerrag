# CareerRAG eval results

Run: 2026-08-24 07:55 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 23 | 24 |
| out_of_scope | 4 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 34/37**

## Failures (kept honest, not hidden)

- `stripe` (grounded): cited ['post-careerrag-launch', 'faq-how-i-work', 'work-3bx'], expected one of ['work-sojourn', 'project-dopaminebuy', 'post-dopaminebuy-launch', 'profile-current-work']
  - Q: Has Nandor built anything with Stripe?
  - A: Yes. He created the “dopaminebuy” fake‑shopping game PWA, which includes Stripe checkout integration. 【profile-current-work】
- `google` (out_of_scope): expected a refusal / no-info answer
  - Q: Has he ever worked at Google?
  - A: I don’t have any record of Nandor working at Google. His public work history lists freelance projects, OmniHR, Creator Linkup, and other engagements, but none mention employment at Google. If you need
- `papers` (out_of_scope): expected a refusal / no-info answer
  - Q: Has he published any academic papers?
  - A: I don’t have any record of Nandor having published academic papers. If you need confirmation, you can reach out to him directly at nandor@nagysolution.com.
