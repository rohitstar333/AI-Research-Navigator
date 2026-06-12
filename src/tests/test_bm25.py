from src.retrivel.bm25_retriever import (
    BM25Retriever,
)


def test_bm25_retrieval():

    retriever = (
        BM25Retriever()
    )

    results = retriever.search(
        query="What is attention?",
        limit=5,
    )

    assert len(results) > 0

    point, score = results[0]

    assert point.payload is not None

    assert score >= 0 