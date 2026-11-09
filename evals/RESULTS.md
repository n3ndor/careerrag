# CareerRAG eval results

Run: 2026-11-09 17:02 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 23 | 28 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 36/41**

## Failures (kept honest, not hidden)

- `stripe` (grounded): missing all of: ['stripe']
  - Q: Has Nandor built anything with Stripe?
  - A: I don't have that in Nandor's public knowledge base. You can email nandor@nagysolution.com for more information.
- `rag-experience` (grounded): cited [], expected one of ['faq-ai-tools', 'work-creator-linkup', 'profile-pitch', 'project-careerrag', 'post-careerrag-launch']
  - Q: What experience does he have with RAG systems?
  - A: Nandor built production‑grade Retrieval‑Augmented Generation (RAG) systems as part of his work at Creator Linkup, where he created n8n workflows that integrated AI, including “RAG knowledge systems.” 
- `manager-quotes` (grounded): cited ['testimonial-torres', 'faq-personal', 'testimonial-vice'], expected one of ['testimonial-peacock', 'testimonial-cordova', 'faq-how-i-work']
  - Q: What do former managers say about him?
  - A: Former managers highlight Nandor’s technical skill, relentless curiosity, and exceptional character. Brendan Cordova, Lead Full‑Stack Developer at 3BX and Sojourn, wrote: “What truly distinguishes Nan
- `current-work` (grounded): missing all of: ['jobfeeds', 'belegradar', 'careerrag']
  - Q: What is Nandor working on right now?
  - A: Nandor is currently dividing his time between freelance client work and his own Shopify‑app products, while also being open to a new full‑time role, contract or engagement.  

**Freelance client work*
- `degree` (grounded): cited ['profile-background-story', 'faq-personal', 'testimonial-soteropulos'], expected one of ['profile-education']
  - Q: Does he have a university degree?
  - A: Yes, Nandor holds a Bachelor of Science in Mathematics and Computer Science from Aurel Vlaicu University in Arad, Romania (2008‑2011). SOURCES: profile-education
