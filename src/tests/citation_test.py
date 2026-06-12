from src.retrivel.rag_pipeline import RAGPipeline

rag = RAGPipeline()

print(
    rag.run(
        "What is attention?"
    )
)