# src/tests/test_metadata_builder.py

from src.ingest.metadata_builder import (
    generate_content_hash,
    build_chunk_payload,
)


def test_generate_content_hash():

    result = generate_content_hash(
        "hello world"
    )

    assert isinstance(
        result,
        str,
    )

    assert len(result) == 64


def test_build_chunk_payload():

    document_metadata = {
        "doc_id": "paper1",
        "title": "Test Paper",
    }

    chunk = {
        "section_title": "Intro",
        "section_index": 0,
        "chunk_index": 0,
        "text": "This is a test chunk",
    }

    payload = build_chunk_payload(
        document_metadata,
        chunk,
    )

    assert (
        payload["doc_id"]
        == "paper1"
    )

    assert (
        payload["section_title"]
        == "Intro"
    )

    assert (
        payload["text"]
        == "This is a test chunk"
    )

    assert (
        "content_hash"
        in payload
    )

    assert (
        "chunk_id"
        in payload
    )