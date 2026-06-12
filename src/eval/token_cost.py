from src.eval.golden_questions import QUESTIONS
from src.retrivel.rag_pipeline import RAGPipeline

rag = RAGPipeline()


def token_cost():

    total_tokens = 0
    total_questions = 0

    for item in QUESTIONS[:5]:

        if item["route"] == "out_of_scope":
            continue

        answer = rag.run(
            item["question"]
        )

        tokens = len(
            answer.split()
        )

        total_tokens += tokens
        total_questions += 1

    avg_tokens = (
        total_tokens
        / total_questions
    )

    return {
        "avg_tokens_per_query":
            round(
                avg_tokens,
                2
            ),
        "questions":
            total_questions,
    }


if __name__ == "__main__":

    print(
        token_cost()
    )