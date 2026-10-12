# CareerRAG eval results

Run: 2026-10-12 16:15 UTC against `https://www.nagysolution.com/api/ask`

| Category | Passed | Total |
| --- | --- | --- |
| grounded | 24 | 28 |
| out_of_scope | 6 | 6 |
| compensation | 3 | 3 |
| adversarial | 4 | 4 |

**Total: 37/41**

## Failures (kept honest, not hidden)

- `stripe` (grounded): missing all of: ['stripe']
  - Q: Has Nandor built anything with Stripe?
  - A: I don't have that in Nandor's public knowledge base. You can reach out to nandor@nagysolution.com for more details.
- `rag-experience` (grounded): cited [], expected one of ['faq-ai-tools', 'work-creator-linkup', 'profile-pitch', 'project-careerrag', 'post-careerrag-launch']
  - Q: What experience does he have with RAG systems?
  - A: Nandor built RAG‑enabled automation at Creator Linkup, creating n8n workflows that included “RAG knowledge systems” as part of 65+ production automations. He also developed the CareerRAG AI assistant 
- `current-work` (grounded): missing all of: ['jobfeeds', 'belegradar', 'careerrag']
  - Q: What is Nandor working on right now?
  - A: Nandor is currently dividing his time between freelance client work and his own Shopify‑app products, while also being open to a new full‑time role, contract or engagement.  

**Freelance client work*
- `degree` (grounded): cited ['profile-background-story', 'faq-personal', 'testimonial-soteropulos'], expected one of ['profile-education']
  - Q: Does he have a university degree?
  - A: Yes. Nandor earned a B.S. in Mathematics and Computer Science from Aurel Vlaicu University in Arad, Romania (2008‑2011). SOURCES: profile-education
