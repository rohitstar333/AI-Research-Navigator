from qdrant_client import QdrantClient
from src.config import settings

client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port
)

print(
    client.count(
        collection_name="research_navigator"
    )
)