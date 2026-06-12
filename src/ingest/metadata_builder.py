from src.ingest.id_generator import generate_chunk_id
import hashlib


def generate_content_hash(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def build_chunk_payload(
    document_metadata,
    chunk,
):
    payload = document_metadata.copy()

    payload["section_title"] = chunk["section_title"]
    payload["section_index"] = chunk["section_index"]
    payload["chunk_index"] = chunk["chunk_index"]

    # IMPORTANT
    payload["text"] = chunk["text"]

    content_hash = generate_content_hash(
        chunk["text"]
    )

    payload["content_hash"] = content_hash

    payload["chunk_id"] = generate_chunk_id(
        document_metadata["doc_id"],
        chunk["chunk_index"],
        content_hash
    )

    return payload