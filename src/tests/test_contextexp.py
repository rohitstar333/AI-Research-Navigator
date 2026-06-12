from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)

retriever = HybridRetriever()

results = retriever.search(
    query="attention",
    limit=1,
)

print(
    results[0].payload
)