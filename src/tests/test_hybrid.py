from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)


def test_hybrid_retrieval():

    retriever = (
        HybridRetriever()
    )

    results = retriever.search(
        query="What is attention?",
        limit=5,
    )

    assert len(results) > 0

    assert (
        results[0].payload
        is not None
    )