from src.retrivel.retriever import (
    Retriever,
)


def test_dense_retrieval():

    retriever = Retriever()

    results = retriever.search(
        query="What is attention?",
        limit=5,
    )

    assert len(results) > 0

    assert (
        results[0].payload
        is not None
    )