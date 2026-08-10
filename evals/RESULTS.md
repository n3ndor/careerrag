# CareerRAG eval results

Run: 2026-08-10 23:44 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 23 | 24 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 36/37**

## Failures (kept honest, not hidden)

- `mentoring` (grounded): cited ['testimonial-torres', 'testimonial-soteropulos', 'testimonial-vice'], expected one of ['work-omnihr', 'work-sojourn', 'work-creator-linkup']
  - Q: Has he mentored anyone or led a team?
  - A: Nandor has been mentored by Christina Torres, who describes herself as his "guiding light during challenging times". She also mentions that he is a natural leader who can motivate and inspire others t
