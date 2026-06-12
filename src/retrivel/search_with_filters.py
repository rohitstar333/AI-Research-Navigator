from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
    Range
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = QdrantClient(
    host="localhost",
    port=6333
)

query = "recent work on attention"

query_vector = model.encode(
    query
).tolist()

search_filter = Filter(
    must=[
        FieldCondition(
            key="year",
            match=MatchValue(
                value=2017
            )
        )
    ]
)

results = client.query_points(
    collection_name="research_navigator",
    query=query_vector,
    query_filter=search_filter,
    limit=5
).points

for i, result in enumerate(results, start=1):

    payload = result.payload or {}

    print("\n====================")
    print(f"Rank: {i}")
    print(f"Score: {result.score}")
    print("Title:", payload.get("title"))
    print("Year:", payload.get("year"))
    print("Section:", payload.get("section_title"))