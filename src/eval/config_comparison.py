from src.eval.golden_questions import (
    QUESTIONS,
)

from src.retrivel.retriever import (
    Retriever,
)

from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)


dense = Retriever()

hybrid = HybridRetriever()


def evaluate():

    dense_precision = 0
    dense_recall = 0

    hybrid_precision = 0
    hybrid_recall = 0

    evaluated = 0

    for item in QUESTIONS:

        if item["route"] == "out_of_scope":
            continue

        expected_docs = set(
            item["expected_docs"]
        )

        query = item["question"]

        # -----------------
        # Dense
        # -----------------

        dense_results = dense.search(
            query=query,
            limit=5,
        )

        dense_docs = set()

        for point in dense_results:

            dense_docs.add(
                point.payload.get(
                    "title",
                    "",
                )
            )

        dense_relevant = 0

        for expected in expected_docs:

            for retrieved in dense_docs:

                if (
                    expected.lower()
                    in retrieved.lower()
                    or
                    retrieved.lower()
                    in expected.lower()
                ):

                    dense_relevant += 1

        dense_precision += (
            dense_relevant
            /
            max(
                len(dense_docs),
                1,
            )
        )

        dense_recall += (
            dense_relevant
            /
            max(
                len(expected_docs),
                1,
            )
        )

        # -----------------
        # Hybrid
        # -----------------

        hybrid_results = hybrid.search(
            query=query,
            limit=5,
        )

        hybrid_docs = set()

        for point in hybrid_results:

            hybrid_docs.add(
                point.payload.get(
                    "title",
                    "",
                )
            )

        hybrid_relevant = 0

        for expected in expected_docs:

            for retrieved in hybrid_docs:

                if (
                    expected.lower()
                    in retrieved.lower()
                    or
                    retrieved.lower()
                    in expected.lower()
                ):

                    hybrid_relevant += 1

        hybrid_precision += (
            hybrid_relevant
            /
            max(
                len(hybrid_docs),
                1,
            )
        )

        hybrid_recall += (
            hybrid_relevant
            /
            max(
                len(expected_docs),
                1,
            )
        )

        evaluated += 1

    return {

        "dense_precision":
            round(
                dense_precision
                / evaluated,
                3,
            ),

        "dense_recall":
            round(
                dense_recall
                / evaluated,
                3,
            ),

        "hybrid_precision":
            round(
                hybrid_precision
                / evaluated,
                3,
            ),

        "hybrid_recall":
            round(
                hybrid_recall
                / evaluated,
                3,
            ),
    }


if __name__ == "__main__":

    print(
        evaluate()
    )