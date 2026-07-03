"""CareerRAG indexer: chunk -> embed -> upsert to Supabase pgvector.

Idempotent and change-aware: chunks whose content hash already exists in the
database are skipped, so a run after a small edit embeds only what changed.
Chunks that disappeared from the knowledge base are deleted.

Usage:
    python -m indexer.main --dry-run     # parse + chunk only, no network
    python -m indexer.main               # full run (needs env vars)

Env vars (full run):
    SUPABASE_URL          https://<ref>.supabase.co
    SUPABASE_SECRET_KEY   service key (writes bypass RLS; CI secret)
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

import httpx

from .documents import Chunk, load_chunks

# Per-invocation CPU on Supabase edge functions is tight; batches above ~4
# texts hit the worker limit (HTTP 546) with the gte-small model.
EMBED_BATCH = 4
TABLE = "careerrag_chunks"


def knowledge_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "knowledge"


class SupabaseIndex:
    def __init__(self, url: str, secret_key: str) -> None:
        self.url = url.rstrip("/")
        self.client = httpx.Client(
            headers={
                "apikey": secret_key,
                "Authorization": f"Bearer {secret_key}",
            },
            timeout=60,
        )

    def existing_hashes(self) -> dict[tuple[str, int], str]:
        resp = self.client.get(
            f"{self.url}/rest/v1/{TABLE}",
            params={"select": "doc_id,chunk_index,content_hash", "limit": "10000"},
        )
        resp.raise_for_status()
        return {
            (row["doc_id"], row["chunk_index"]): row["content_hash"]
            for row in resp.json()
        }

    def embed(self, texts: list[str]) -> list[list[float]]:
        embeddings: list[list[float]] = []
        for start in range(0, len(texts), EMBED_BATCH):
            batch = texts[start : start + EMBED_BATCH]
            for attempt in range(3):
                resp = self.client.post(
                    f"{self.url}/functions/v1/embed", json={"input": batch}
                )
                if resp.status_code == 200:
                    embeddings.extend(resp.json()["embeddings"])
                    break
                if attempt == 2:
                    resp.raise_for_status()
                time.sleep(2 ** (attempt + 1))
        return embeddings

    def upsert(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        rows = [
            {
                "doc_id": c.doc_id,
                "chunk_index": c.chunk_index,
                "title": c.title,
                "doc_type": c.doc_type,
                "source_url": c.source_url,
                "updated": c.updated,
                "content": c.content,
                "content_hash": c.content_hash,
                "embedding": e,
            }
            for c, e in zip(chunks, embeddings, strict=True)
        ]
        resp = self.client.post(
            f"{self.url}/rest/v1/{TABLE}",
            params={"on_conflict": "doc_id,chunk_index"},
            headers={"Prefer": "resolution=merge-duplicates"},
            json=rows,
        )
        resp.raise_for_status()

    def delete(self, keys: list[tuple[str, int]]) -> None:
        for doc_id, chunk_index in keys:
            resp = self.client.delete(
                f"{self.url}/rest/v1/{TABLE}",
                params={"doc_id": f"eq.{doc_id}", "chunk_index": f"eq.{chunk_index}"},
            )
            resp.raise_for_status()


def run(dry_run: bool) -> int:
    chunks = load_chunks(knowledge_dir())
    docs = {c.doc_id for c in chunks}
    print(f"knowledge base: {len(docs)} documents, {len(chunks)} chunks")

    if dry_run:
        for c in chunks:
            print(f"  {c.doc_id}[{c.chunk_index}]  {len(c.content):>5} chars  ({c.doc_type})")
        print("dry run: no embedding or database writes")
        return 0

    url = os.environ.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_SECRET_KEY", "")
    if not url or not key:
        print("error: SUPABASE_URL and SUPABASE_SECRET_KEY must be set", file=sys.stderr)
        return 1

    index = SupabaseIndex(url, key)
    existing = index.existing_hashes()

    current_keys = {(c.doc_id, c.chunk_index) for c in chunks}
    changed = [
        c for c in chunks
        if existing.get((c.doc_id, c.chunk_index)) != c.content_hash
    ]
    stale = sorted(k for k in existing if k not in current_keys)

    print(f"unchanged: {len(chunks) - len(changed)}, to embed: {len(changed)}, stale: {len(stale)}")

    if changed:
        embeddings = index.embed([c.content for c in changed])
        index.upsert(changed, embeddings)
        print(f"upserted {len(changed)} chunks")
    if stale:
        index.delete(stale)
        print(f"deleted {len(stale)} stale chunks")

    print("index up to date")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="CareerRAG knowledge indexer")
    parser.add_argument("--dry-run", action="store_true", help="parse and chunk only")
    args = parser.parse_args()
    return run(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
