# CareerRAG eval results

Run: 2026-08-17 07:48 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 21 | 24 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 34/37**

## Failures (kept honest, not hidden)

- `stripe` (grounded): cited ['post-careerrag-launch', 'faq-how-i-work', 'work-3bx'], expected one of ['work-sojourn', 'project-dopaminebuy', 'post-dopaminebuy-launch', 'profile-current-work']
  - Q: Has Nandor built anything with Stripe?
  - A: Yes. Nandor built **dopaminebuy**, a fake‑shopping game PWA that includes Stripe checkout integration. SOURCES: profile-current-work
- `degree` (grounded): cited ['profile-background-story', 'faq-personal', 'testimonial-soteropulos'], expected one of ['profile-education']
  - Q: Does he have a university degree?
  - A: Yes, Nandor holds a Bachelor of Science degree in Mathematics and Computer Science from Aurel Vlaicu University in Arad, Romania (2008‑2011). SOURCES: profile-education
- `python-work` (grounded): cited ['testimonial-vice', 'github-repos', 'profile-current-work'], expected one of ['project-jobradar', 'profile-skills', 'work-freelance', 'profile-education']
  - Q: What Python work has he done?
  - A: Nandor has used Python for several automation and data‑pipeline projects. He built the back‑end of JobRadar with a Python 3.12 pipeline (httpx, pydantic, supabase‑py) that scrapes job listings, runs d
