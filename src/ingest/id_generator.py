import uuid


def generate_chunk_id(
    doc_id,
    chunk_index,
    content_hash,
):
    raw = (
        f"{doc_id}:"
        f"{chunk_index}:"
        f"{content_hash}"
    )

    return str(
        uuid.uuid5(
            uuid.NAMESPACE_DNS,
            raw
        )
    )