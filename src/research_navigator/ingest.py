import argparse
from qdrant_client import QdrantClient


def ingest():
    print("Running ingestion...")


def validate():
    print("Validating corpus...")


def reindex():
    print("Reindexing...")


def stats():
    client = QdrantClient(
        host="localhost",
        port=6333
    )

    result = client.count(
        collection_name="research_navigator"
    )

    print("\n===== DATABASE STATS =====")
    print(f"Total Chunks: {result.count}")


def main():
    parser = argparse.ArgumentParser(
        description="AI Research Navigator"
    )

    parser.add_argument(
        "command",
        choices=[
            "ingest",
            "validate",
            "reindex",
            "stats"
        ]
    )

    args = parser.parse_args()

    if args.command == "ingest":
        ingest()

    elif args.command == "validate":
        validate()

    elif args.command == "reindex":
        reindex()

    elif args.command == "stats":
        stats()


if __name__ == "__main__":
    main()