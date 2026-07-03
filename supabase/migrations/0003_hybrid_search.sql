-- Hybrid retrieval: full-text search alongside vector similarity.
-- Small embedding models under-rank rare exact terms ("Cloudflare", "IBAN"):
-- the question's generic words dominate the embedding. Postgres full-text
-- catches exactly those; the chat API merges both result sets.

create index careerrag_chunks_fts_idx on careerrag_chunks
    using gin (to_tsvector('english', content));

create or replace function search_careerrag_chunks(
    query       text,
    match_count int default 4
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
        ts_rank(
            to_tsvector('english', c.content),
            websearch_to_tsquery('english', query)
        )::float as similarity
    from careerrag_chunks c
    where to_tsvector('english', c.content)
          @@ websearch_to_tsquery('english', query)
    order by similarity desc
    limit match_count;
$$;
