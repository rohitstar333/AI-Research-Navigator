from src.eval.golden_questions import (
    QUESTIONS,
)

from src.retrivel.rag_pipeline import (
    RAGPipeline,
)


rag = RAGPipeline()


def refusal_accuracy():

    total = 0
    correct = 0

    for item in QUESTIONS:

        if (
            item["route"]
            != "out_of_scope"
        ):
            continue

        question = (
            item["question"]
        )

        answer = rag.run(
            question
        )

        refused = (
            "I don't have enough relevant material"
            in answer
        )

        total += 1

        if refused:

            correct += 1

    return {
        "refusal_accuracy":
        round(
            correct / total,
            3,
        ),
        "correct":
        correct,
        "total":
        total,
    }


if __name__ == "__main__":

    print(
        refusal_accuracy()
    )