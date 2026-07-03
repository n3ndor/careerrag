-- Question log: powers per-IP rate limiting and a feedback loop for eval
-- questions. No document content is stored beyond what visitors type.
-- Written only via the secret key (RLS enabled, no public policies).

create table careerrag_questions (
    id         bigint generated always as identity primary key,
    ip_hash    text not null,
    question   text not null,
    answered   boolean not null default true,
    created_at timestamptz not null default now()
);

create index careerrag_questions_rate_idx
    on careerrag_questions (ip_hash, created_at desc);

alter table careerrag_questions enable row level security;
-- Intentionally no public policies: reads and writes go through the
-- service key in the chat API route only.
