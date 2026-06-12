from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from src.config import settings

client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port
)

collections = client.get_collections()

existing = [
    c.name
    for c in collections.collections
]

if "research_navigator" not in existing:

    client.create_collection(
        collection_name="research_navigator",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection created!")

else:
    print("Collection already exists.")