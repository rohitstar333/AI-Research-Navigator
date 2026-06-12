from src.ingest.id_generator import generate_chunk_id

chunk_id = generate_chunk_id(
    doc_id="arxiv-1706.03762",
    chunk_index=0,
    content_hash="598bcf165e2a2ef84d68fa4449f2146cfb80cadcfa50ce8926363d3417354ac4",
)

print(chunk_id)