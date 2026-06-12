from rank_bm25 import BM25Okapi  # type: ignore
from qdrant_client import QdrantClient
from src.config import settings


class BM25Retriever:

    COLLECTION_NAME = "research_navigator"

    def __init__(self):

        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port
        )

        self.points = []
        self.documents = []

        self.load_chunks()

    def load_chunks(self):

        offset = None

        while True:

            points, offset = self.client.scroll(
                collection_name=self.COLLECTION_NAME,
                limit=1000,
                offset=offset,
                with_payload=True
            )

            self.points.extend(points)

            if offset is None:
                break

        self.documents = []

        for point in self.points:

            payload = point.payload

            title = payload.get(
                "title",
                ""
            )

            section = payload.get(
                "section_title",
                ""
            )

            text = payload.get(
                "text",
                ""
            )

            combined_text = (
                title
                + " "
                + title
                + " "
                + section
                + " "
                + text
            )

            self.documents.append(
                combined_text
            )

        tokenized_docs = [

            doc.lower().split()

            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(
            tokenized_docs
        )

        print(
            f"Loaded {len(self.documents)} chunks"
        )

    def search(
        self,
        query,
        limit=5
    ):

        tokenized_query = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            zip(
                self.points,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:limit]