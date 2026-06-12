# src/tests/test_id_generator.py

from src.ingest.id_generator import (
    generate_chunk_id,
)


def test_generate_chunk_id():

    chunk_id = generate_chunk_id(
        "paper1",
        0,
        "abc123",
    )

    assert isinstance(
        chunk_id,
        str,
    )

    assert len(chunk_id) > 0