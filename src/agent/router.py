from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)

from src.retrivel.refusal_checker import (
    RefusalChecker,
)

from .state import ResearchState

from .tools import (
    lookup_paper,
)

retriever = HybridRetriever()

refusal_checker = RefusalChecker()


def router(
    state: ResearchState,
):

    query = state["query"]

    retrieved_points = retriever.search(
        query=query,
        limit=3,
    )

    if refusal_checker.should_refuse(
        query,
        retrieved_points,
    ):

        return {
            "route": "out_of_scope"
        }

    q = query.lower()

    if (
        "compare" in q
        or " vs " in q
        or "difference between" in q
    ):

        route = (
            "compare_approaches"
        )

    elif any(
        word in q
        for word in [
            "recent",
            "latest",
            "new developments",
            "last 12 months",
            "past year",
        ]
    ):

        route = (
            "recent_developments"
        )

    elif any(
        word in q
        for word in [
            "recommend",
            "reading list",
            "foundational papers",
            "papers on",
        ]
    ):

        route = (
            "find_papers"
        )

    elif lookup_paper(
        query
    ):

        route = (
            "paper_deep_dive"
        )

    elif "paper" in q:

        route = (
            "paper_deep_dive"
        )

    else:

        route = (
            "concept_explanation"
        )

    return {
        "route": route
    }