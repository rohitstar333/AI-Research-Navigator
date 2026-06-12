import json

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer

from src.ingest.pdf_parser import parse_pdf
from src.ingest.md_parser import parse_markdown
from src.ingest.chunker import create_document_chunks
from src.ingest.metadata_builder import build_chunk_payload
from src.config import settings


# Connect to Qdrant
client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port
)

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Load manifest
with open("manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

points = []

# Process all documents
for document_metadata in manifest["documents"]:

    path = document_metadata["local_path"]

    print(f"\nProcessing: {path}")

    try:

        if path.endswith(".pdf"):
            text = parse_pdf(path)

        elif path.endswith(".md"):
            text = parse_markdown(path)

        else:
            print(f"Skipping unsupported file: {path}")
            continue

        chunks = create_document_chunks(text)

        print(f"Chunks created: {len(chunks)}")

        for chunk in chunks:

            payload = build_chunk_payload(
                document_metadata,
                chunk
            )

            vector = model.encode(
                chunk["text"]
            ).tolist()

            points.append(
                PointStruct(
                    id=payload["chunk_id"],
                    vector=vector,
                    payload=payload
                )
            )

    except Exception as e:
        print(f"Error processing {path}")
        print(e)

print(f"\nTotal points to upload: {len(points)}")

# Upload in batches
batch_size = 100

for i in range(0, len(points), batch_size):

    batch = points[i:i + batch_size]

    client.upsert(
        collection_name="research_navigator",
        points=batch
    )

    print(
        f"Uploaded {min(i + batch_size, len(points))}/{len(points)}"
    )

print(
    f"\nSuccessfully stored {len(points)} chunks in Qdrant"
)