"""Load knowledge-base markdown files and split them into embeddable chunks.

Files are small and hand-curated, so chunking is simple: a file under the
size limit is one chunk; larger files split on ## headings, and any oversized
section falls back to paragraph packing. No token counting is needed because
gte-small truncates at 512 tokens and the limits below stay safely under it.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

MAX_CHUNK_CHARS = 1400

REQUIRED_KEYS = ("id", "title", "type")


@dataclass
class Document:
    doc_id: str
    title: str
    doc_type: str
    source_url: str | None
    updated: str | None
    body: str
    path: Path


@dataclass
class Chunk:
    doc_id: str
    chunk_index: int
    title: str
    doc_type: str
    source_url: str | None
    updated: str | None
    content: str
    content_hash: str = field(init=False)

    def __post_init__(self) -> None:
        self.content_hash = hashlib.sha256(self.content.encode("utf-8")).hexdigest()


class KnowledgeError(ValueError):
    """Raised when a knowledge file is malformed."""


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.DOTALL)
    if not match:
        raise KnowledgeError(f"{path}: missing frontmatter block")
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise KnowledgeError(f"{path}: bad frontmatter line: {line!r}")
        meta[key.strip()] = value.strip()
    missing = [k for k in REQUIRED_KEYS if not meta.get(k)]
    if missing:
        raise KnowledgeError(f"{path}: frontmatter missing {missing}")
    return meta, match.group(2).strip()


def load_documents(knowledge_dir: Path) -> list[Document]:
    docs: list[Document] = []
    seen_ids: set[str] = set()
    for path in sorted(knowledge_dir.rglob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"), path)
        if meta["id"] in seen_ids:
            raise KnowledgeError(f"{path}: duplicate doc id {meta['id']!r}")
        seen_ids.add(meta["id"])
        if not body:
            raise KnowledgeError(f"{path}: empty body")
        docs.append(
            Document(
                doc_id=meta["id"],
                title=meta["title"],
                doc_type=meta["type"],
                source_url=meta.get("source_url") or None,
                updated=meta.get("updated") or None,
                body=body,
                path=path,
            )
        )
    return docs


def _pack_paragraphs(paragraphs: list[str]) -> list[str]:
    parts: list[str] = []
    current = ""
    for para in paragraphs:
        candidate = f"{current}\n\n{para}".strip()
        if current and len(candidate) > MAX_CHUNK_CHARS:
            parts.append(current)
            current = para
        else:
            current = candidate
    if current:
        parts.append(current)
    return parts


def split_body(body: str) -> list[str]:
    if len(body) <= MAX_CHUNK_CHARS:
        return [body]
    # Split on ## headings (keeping the heading with its section), break any
    # oversized section into paragraphs, then greedily re-pack the pieces so
    # small adjacent sections share a chunk instead of becoming fragments.
    sections = re.split(r"(?m)^(?=## )", body)
    pieces: list[str] = []
    for section in (s.strip() for s in sections if s.strip()):
        if len(section) <= MAX_CHUNK_CHARS:
            pieces.append(section)
        else:
            pieces.extend(_pack_paragraphs(re.split(r"\n\s*\n", section)))
    return _pack_paragraphs(pieces)


def chunk_document(doc: Document) -> list[Chunk]:
    chunks = []
    for i, content in enumerate(split_body(doc.body)):
        # Prefix every chunk with the document title so retrieval and the
        # LLM always see which document a fragment belongs to.
        text = f"# {doc.title}\n\n{content}"
        chunks.append(
            Chunk(
                doc_id=doc.doc_id,
                chunk_index=i,
                title=doc.title,
                doc_type=doc.doc_type,
                source_url=doc.source_url,
                updated=doc.updated,
                content=text,
            )
        )
    return chunks


def load_chunks(knowledge_dir: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    for doc in load_documents(knowledge_dir):
        chunks.extend(chunk_document(doc))
    return chunks
