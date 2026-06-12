import time
import statistics

from src.eval.golden_questions import (
    QUESTIONS,
)

from src.retrivel.rag_pipeline import (
    RAGPipeline,
)


rag = RAGPipeline()


def latency_metrics():

    times = []

    for item in QUESTIONS:

        start = time.perf_counter()

        rag.run(
            item["question"]
        )

        end = time.perf_counter()

        times.append(
            end - start
        )

    times.sort()

    p50 = statistics.median(
        times
    )

    p95_index = int(
        len(times) * 0.95
    )

    p95 = times[
        min(
            p95_index,
            len(times) - 1,
        )
    ]

    avg = sum(times) / len(times)

    return {
        "avg_latency":
            round(avg, 3),

        "p50_latency":
            round(p50, 3),

        "p95_latency":
            round(p95, 3),
    }


if __name__ == "__main__":

    print(
        latency_metrics()
    )