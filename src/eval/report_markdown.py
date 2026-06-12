import json

with open(
    "evaluation_report.json",
    "r",
) as f:

    report = json.load(f)

markdown = f"""
# Evaluation Report

## Retrieval Metrics

- Precision@5: {report["precision_at_5"]}
- Recall@5: {report["recall_at_5"]}

## Citation Faithfulness

Rubric:

1. Every factual claim should have a citation.
2. Claims without citations fail.
3. Citations should correspond to retrieved sources.

## Refusal Correctness

- Accuracy: {report["refusal_accuracy"]}

## Latency

- Average: {report["latency"]["avg"]} sec
- P50: {report["latency"]["p50"]} sec
- P95: {report["latency"]["p95"]} sec

## Token Cost

- Average Tokens Per Query: {report["token_cost"]["avg_tokens_per_query"]}

## Configuration Comparison

Configuration A:
- Dense Retrieval

Configuration B:
- Hybrid Retrieval

Comparison pending.
"""

with open(
    "evaluation_report.md",
    "w",
    encoding="utf-8",
) as f:

    f.write(markdown)

print(
    "evaluation_report.md created"
)