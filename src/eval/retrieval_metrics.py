from src.eval.golden_questions import (
    QUESTIONS,
)

from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)


retriever = HybridRetriever()


def precision_recall_at_k(
    k=5,
):

    total_precision = 0
    total_recall = 0

    evaluated = 0

    for item in QUESTIONS:

        if (
            item["route"]
            == "out_of_scope"
        ):
            continue

        question = (
            item["question"]
        )

        expected_docs = set(
            item["expected_docs"]
        )

        results = (
            retriever.search(
                query=question,
                limit=k,
            )
        )

        retrieved_docs = set()

        for point in results:

            retrieved_docs.add(
                point.payload.get(
                    "title",
                    ""
                )
            )

        print(
            "\n"
            + "=" * 60
        )

        print(
            "QUESTION:"
        )

        print(
            question
        )

        print(
            "\nEXPECTED DOCS:"
        )

        for doc in expected_docs:

            print(
                "-",
                doc,
            )

        print(
            "\nRETRIEVED DOCS:"
        )

        for doc in retrieved_docs:

            print(
                "-",
                doc,
            )

        print(
            "=" * 60
        )

        relevant = set()

        for expected in expected_docs:

            expected_lower = (
                expected.lower()
            )

            for retrieved in retrieved_docs:

                retrieved_lower = (
                    retrieved.lower()
                )

                if (
                    expected_lower
                    in
                    retrieved_lower
                    or
                    retrieved_lower
                    in
                    expected_lower
                ):

                    relevant.add(
                        retrieved
                    )

        precision = (
            len(relevant)
            /
            max(
                len(retrieved_docs),
                1,
            )
        )

        recall = (
            len(relevant)
            /
            max(
                len(expected_docs),
                1,
            )
        )

        total_precision += (
            precision
        )

        total_recall += (
            recall
        )

        evaluated += 1

    return {

        "precision_at_k":
        round(
            total_precision
            / evaluated,
            3,
        ),

        "recall_at_k":
        round(
            total_recall
            / evaluated,
            3,
        ),
    }


if __name__ == "__main__":

    print(
        precision_recall_at_k()
    )