# CareerRAG eval results

Run: 2026-07-06 11:30 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 22 | 24 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 35/37**

## Failures (kept honest, not hidden)

- `mentoring` (grounded): cited [], expected one of ['work-omnihr', 'work-sojourn', 'work-creator-linkup']
  - Q: Has he mentored anyone or led a team?
  - A: Nandor has been mentored by Christina Torres, who describes him as an outstanding software engineer with a remarkable work ethic and dedication. He has also been a model student and a great team playe
- `degree` (grounded): cited ['profile-background-story', 'faq-personal', 'testimonial-soteropulos'], expected one of ['profile-education']
  - Q: Does he have a university degree?
  - A: Yes, Nandor has a B.S. in Mathematics and Computer Science from Aurel Vlaicu University in Arad, Romania, which he finished in the top 10 of his class. He studied C++, C#, Turbo Pascal, and Java durin
