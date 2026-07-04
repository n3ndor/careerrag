-- Log the bot's answers alongside the questions, so bad answers can be
-- found, audited, and fixed by improving the knowledge base. This is the
-- feedback loop: review what real visitors asked, patch the gaps.

alter table careerrag_questions
    add column answer text,
    add column sources text[] not null default '{}';
