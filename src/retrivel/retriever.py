from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from src.config import settings

class Retriever:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.embedding_model
)

        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port
        )

    def search(
        self,
        query,
        limit=5,
        filters=None,
    ):

        query_vector = (
            self.model.encode(query)
            .tolist()
        )

        results = self.client.query_points(
            collection_name="research_navigator",
            query=query_vector,
            query_filter=filters,
            limit=limit,
        ).points

        return results