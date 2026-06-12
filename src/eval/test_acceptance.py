from src.eval.test_questions import (
    QUESTIONS,
)

from src.retrivel.rag_pipeline import (
    RAGPipeline,
)

rag = RAGPipeline()

for question in QUESTIONS:

    response = rag.run(
        question
    )

    print("\n" + "=" * 50)
    print("Question:")
    print(question)

    print("\nResponse:")
    print(response)