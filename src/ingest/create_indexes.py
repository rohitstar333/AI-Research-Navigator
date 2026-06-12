from qdrant_client import QdrantClient
from qdrant_client.models import PayloadSchemaType
from src.config import settings

client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port
)

collection_name = "research_navigator"

client.create_payload_index(
    collection_name,
    "content_type",
    PayloadSchemaType.KEYWORD
)

client.create_payload_index(
    collection_name,
    "year",
    PayloadSchemaType.INTEGER
)

client.create_payload_index(
    collection_name,
    "tags",
    PayloadSchemaType.KEYWORD
)

client.create_payload_index(
    collection_name,
    "primary_category",
    PayloadSchemaType.KEYWORD
)

client.create_payload_index(
    collection_name,
    "is_foundational",
    PayloadSchemaType.BOOL
)

print("Indexes created successfully")