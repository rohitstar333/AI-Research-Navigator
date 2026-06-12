import json

from src.eval.retrieval_metrics import (
    precision_recall_at_k,
)

from src.eval.latency_metrics import (
    latency_metrics,
)

from src.eval.refusal_metrics import (
    refusal_accuracy,
)

from src.eval.token_cost import (
    token_cost,
)


retrieval = (
    precision_recall_at_k()
)

latency = (
    latency_metrics()
)

refusal = (
    refusal_accuracy()
)

tokens = (
    token_cost()
)


report = {

    "precision_at_5":
        retrieval[
            "precision_at_k"
        ],

    "recall_at_5":
        retrieval[
            "recall_at_k"
        ],

    "citation_faithfulness": {

        "rubric": [

            "Every factual claim should have a citation",

            "Claims without citations fail",

            "Citations should correspond to retrieved sources",
        ]
    },

    "refusal_accuracy":
        refusal[
            "refusal_accuracy"
        ],

    "latency": {

        "avg":
            latency[
                "avg_latency"
            ],

        "p50":
            latency[
                "p50_latency"
            ],

        "p95":
            latency[
                "p95_latency"
            ],
    },

    "token_cost":
        tokens,
}


with open(
    "evaluation_report.json",
    "w",
) as f:

    json.dump(
        report,
        f,
        indent=4,
    )


print(
    json.dumps(
        report,
        indent=4,
    )
)

print(
    "\nevaluation_report.json created"
)