from src.agent.graph import (
    research_graph,
)

queries = [
    "What is FlashAttention?",
    
    "FlashAttention vs Standard Attention",
    "Recent developments in MoE",
    "Recommend papers on FlashAttention",
   
]

for query in queries:

    result = research_graph.invoke(
        {
            "query": query,
            "route": "",
            "answer": "",
            "retrieved_chunks": [],
            "filters": {},
            "paper_name": None,
            "method_a": None,
            "method_b": None,
        }
    )

    print("\n" + "=" * 50)
    print(query)
    print("=" * 50)
    print(result["answer"])