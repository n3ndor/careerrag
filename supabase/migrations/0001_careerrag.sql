-- CareerRAG schema
-- Run in the Supabase SQL editor (same project as JobRadar; tables are prefixed).
-- Writes happen only through the indexer's secret key (bypasses RLS);
-- the chat API reads via the publishable key under a read-only policy.

create extension if not exists vector;

create table careerrag_chunks (
    id           bigint generated always as identity primary key,
    doc_id       text not null,
    chunk_index  int not null,
    title        text not null,
    doc_type     text not null,
    source_url   text,
    updated      date,
    content      text not null,
    content_hash text not null,
    embedding    vector(384),
    indexed_at   timestamptz not null default now(),
    unique (doc_id, chunk_index)
);

create index careerrag_chunks_doc_idx on careerrag_chunks (doc_id);
create index careerrag_chunks_embedding_idx on careerrag_chunks
    using hnsw (embedding vector_cosine_ops);

alter table careerrag_chunks enable row level security;
create policy "public read careerrag_chunks" on careerrag_chunks
    for select using (true);

-- Cosine-similarity retrieval used by the chat API route.
create or replace function match_careerrag_chunks(
    query_embedding vector(384),
    match_count     int default 6,
    min_similarity  float default 0.35
)
returns table (
    doc_id      text,
    chunk_index int,
    title       text,
    doc_type    text,
    source_url  text,
    content     text,
    similarity  float
)
language sql stable
as $$
    select
        c.doc_id,
        c.chunk_index,
        c.title,
        c.doc_type,
        c.source_url,
        c.content,
        1 - (c.embedding <=> query_embedding) as similarity
    from careerrag_chunks c
    where c.embedding is not null
      and 1 - (c.embedding <=> query_embedding) >= min_similarity
    order by c.embedding <=> query_embedding
    limit match_count;
$$;
