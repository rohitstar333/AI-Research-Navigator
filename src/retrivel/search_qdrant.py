from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = QdrantClient(
    host="localhost",
    port=6333
)

query = "What is multi-head attention?"

query_vector = model.encode(
    query
).tolist()

results = client.query_points(
    collection_name="research_navigator",
    query=query_vector,
    limit=3
).points

for i, result in enumerate(results, start=1):

    payload = result.payload or {}

    print("\n========================")
    print(f"Rank: {i}")
    print(f"Score: {result.score}")
    print("Title:", payload.get("title"))
    print("Section:", payload.get("section_title"))

    print("\nChunk Text:\n")

    print(
        payload.get("text", "No text found")[:1000]
    )