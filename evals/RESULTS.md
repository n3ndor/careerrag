# CareerRAG eval results

Run: 2026-09-14 13:43 UTC against `https://www.nagysolution.com/api/ask`

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
  - A: Yes. In July 2026 Nandor shipped “dopaminebuy,” a fake‑shopping game PWA that uses Stripe checkout for payments. SOURCES: profile-current-work
- `before-2023` (grounded): no answer (HTTP 500)
  - Q: What did Nandor do before 2023?
  - A: (no answer)
- `google` (out_of_scope): expected a refusal / no-info answer
  - Q: Has he ever worked at Google?
  - A: I don’t have any record of Nandor working at Google. All of his documented roles are with companies such as 3BX, OmniHR, Creator Linkup, and his freelance engagements. If you need more detailed inform
