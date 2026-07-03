from pathlib import Path

import pytest

from indexer.documents import (
    MAX_CHUNK_CHARS,
    KnowledgeError,
    chunk_document,
    load_chunks,
    load_documents,
    parse_frontmatter,
    split_body,
)

KNOWLEDGE_DIR = Path(__file__).resolve().parents[2] / "knowledge"


def make_doc(tmp_path: Path, name: str, text: str) -> Path:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


VALID = """---
id: test-doc
title: Test document
type: profile
updated: 2026-07-03
---

Some body text.
"""


def test_parse_frontmatter_valid(tmp_path):
    meta, body = parse_frontmatter(VALID, tmp_path / "x.md")
    assert meta["id"] == "test-doc"
    assert meta["type"] == "profile"
    assert body == "Some body text."


@pytest.mark.parametrize(
    "text",
    [
        "no frontmatter at all",
        "---\ntitle: only title\n---\nbody",  # missing id and type
    ],
)
def test_parse_frontmatter_invalid(tmp_path, text):
    with pytest.raises(KnowledgeError):
        parse_frontmatter(text, tmp_path / "x.md")


def test_load_documents_rejects_duplicate_ids(tmp_path):
    make_doc(tmp_path, "a.md", VALID)
    make_doc(tmp_path, "b.md", VALID)
    with pytest.raises(KnowledgeError, match="duplicate"):
        load_documents(tmp_path)


def test_load_documents_skips_readme(tmp_path):
    make_doc(tmp_path, "a.md", VALID)
    make_doc(tmp_path, "README.md", "just a note, no frontmatter")
    assert len(load_documents(tmp_path)) == 1


def test_small_body_is_single_chunk():
    assert split_body("short text") == ["short text"]


def test_long_body_splits_on_headings():
    body = "\n\n".join(f"## Section {i}\n\n" + ("x" * 600) for i in range(5))
    parts = split_body(body)
    assert len(parts) > 1
    assert all(len(p) <= MAX_CHUNK_CHARS for p in parts)
    assert parts[0].startswith("## Section 0")


def test_small_sections_are_packed_together():
    body = "intro " * 300 + "\n\n" + "\n\n".join(
        f"## S{i}\n\ntiny section" for i in range(6)
    )
    parts = split_body(body)
    # The six tiny sections must not become six separate chunks.
    section_chunks = [p for p in parts if "## S" in p]
    assert len(section_chunks) == 1


def test_oversized_section_packs_paragraphs():
    body = "## One big section\n\n" + "\n\n".join("y" * 500 for _ in range(6))
    parts = split_body(body)
    assert len(parts) > 1
    assert all(len(p) <= MAX_CHUNK_CHARS for p in parts)


def test_chunk_prefixes_title(tmp_path):
    make_doc(tmp_path, "a.md", VALID)
    (doc,) = load_documents(tmp_path)
    (chunk,) = chunk_document(doc)
    assert chunk.content.startswith("# Test document")
    assert chunk.content_hash


def test_real_knowledge_base_parses_and_chunks():
    """The committed knowledge base must always be indexable."""
    chunks = load_chunks(KNOWLEDGE_DIR)
    assert len(chunks) >= 15
    assert all(len(c.content) <= MAX_CHUNK_CHARS + 200 for c in chunks)
    types = {c.doc_type for c in chunks}
    assert {"profile", "project", "testimonial", "post", "faq"} <= types
