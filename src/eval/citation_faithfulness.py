from src.eval.golden_questions import QUESTIONS
from src.retrivel.rag_pipeline import RAGPipeline

rag = RAGPipeline()


def citation_faithfulness():

    total_answers = 0
    answers_with_citations = 0

    for item in QUESTIONS[:3]:

        if item["route"] == "out_of_scope":
            continue

        answer = rag.run(
            item["question"]
        )

        total_answers += 1

        if "[1]" in answer:
            answers_with_citations += 1

    return {
        "total_answers": total_answers,
        "answers_with_citations": answers_with_citations,
        "citation_coverage":
            round(
                answers_with_citations
                / total_answers,
                3,
            )
    }


if __name__ == "__main__":
    print(
        citation_faithfulness()
    )