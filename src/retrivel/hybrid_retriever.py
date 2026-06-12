from src.retrivel.retriever import Retriever
from src.retrivel.bm25_retriever import BM25Retriever


class HybridRetriever:

    def __init__(self):

        self.dense = Retriever()

        self.bm25 = BM25Retriever()

    def search(
        self,
        query,
        limit=5,
        filters=None,
    ):

        dense_results = self.dense.search(
            query=query,
            limit=10,
            filters=filters,
        )

        bm25_results = self.bm25.search(
            query=query,
            limit=50,
        )

        fused = {}

        k = 60

        # Dense results
        for rank, point in enumerate(
            dense_results,
            start=1,
        ):

            chunk_id = (
                point.payload["chunk_id"]
            )

            fused[chunk_id] = {
                "point": point,
                "score": (
                    1 / (k + rank)
                ),
            }

        # BM25 results
        for rank, (
            point,
            _
        ) in enumerate(
            bm25_results,
            start=1,
        ):

            chunk_id = (
                point.payload["chunk_id"]
            )

            if chunk_id in fused:

                fused[chunk_id][
                    "score"
                ] += (
                    1 / (k + rank)
                )

            else:

                fused[chunk_id] = {
                    "point": point,
                    "score": (
                        1 / (k + rank)
                    ),
                }

        ranked = sorted(
            fused.values(),
            key=lambda x: x["score"],
            reverse=True,
        )

        return [
            item["point"]
            for item in ranked[:limit]
        ]