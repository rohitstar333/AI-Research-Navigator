from langgraph.graph import (
    StateGraph,
    END,
)

from .state import ResearchState
from .router import router

from .tools import (
    lookup_paper,
    get_recent_year_cutoff,
)

from src.retrivel.rag_pipeline import (
    RAGPipeline,
)

rag_pipeline = RAGPipeline()


def concept_explanation(
    state: ResearchState,
):

    answer = rag_pipeline.run(
        state["query"]
    )

    return {
        "answer": answer
    }


def paper_deep_dive(
    state: ResearchState,
):

    paper_title = lookup_paper(
        state["query"]
    )

    if paper_title:

        query = (
            f"Provide a detailed analysis of "
            f"{paper_title}.\n\n"
            + state["query"]
        )

    else:

        query = (
            "Provide a detailed paper analysis.\n\n"
            + state["query"]
        )

    answer = rag_pipeline.run(
        query
    )

    return {
        "answer": answer
    }


def compare_approaches(
    state: ResearchState,
):

    query = (
        "Compare the approaches, methods, "
        "or papers mentioned in this query.\n\n"
        + state["query"]
    )

    answer = rag_pipeline.run(
        query
    )

    return {
        "answer": answer
    }


def recent_developments(
    state: ResearchState,
):

    cutoff = (
        get_recent_year_cutoff()
    )

    query = (
        f"Focus on developments after "
        f"{cutoff}. Provide a "
        f"chronological summary.\n\n"
        + state["query"]
    )

    answer = rag_pipeline.run(
        query
    )

    return {
        "answer": answer
    }


def find_papers(
    state: ResearchState,
):

    query = state["query"]

    query_lower = query.lower()

    if "transformer" in query_lower:

        query += (
            " Attention Is All You Need "
            " BERT "
            " GPT-3 "
        )

    elif "rag" in query_lower:

        query += (
            " CRAG "
            " GraphRAG "
            " RAFT "
            " Retrieval-Augmented Generation "
        )

    elif "reasoning" in query_lower:

        query += (
            " Chain-of-Thought "
            " DeepSeek-R1 "
            " ReAct "
        )

    elif "agent" in query_lower:

        query += (
            " ReAct "
            " SWE-Agent "
            " Autonomous Agents "
        )

    elif "alignment" in query_lower:

        query += (
            " RLHF "
            " Constitutional AI "
            " Self-Rewarding Language Models "
            " KTO "
        )

    elif "quantization" in query_lower:

        query += (
            " BitNet "
            " 1-bit LLM "
            " Quantization "
        )

    answer = rag_pipeline.run(
        query
    )

    return {
        "answer": answer
    }


def fallback(
    state: ResearchState,
):

    return {
        "answer":
        (
            "I don't have enough relevant "
            "material in the corpus to "
            "answer this confidently."
        )
    }


graph = StateGraph(
    ResearchState
)

graph.add_node(
    "router",
    router,
)

graph.add_node(
    "concept_explanation",
    concept_explanation,
)

graph.add_node(
    "paper_deep_dive",
    paper_deep_dive,
)

graph.add_node(
    "compare_approaches",
    compare_approaches,
)

graph.add_node(
    "recent_developments",
    recent_developments,
)

graph.add_node(
    "find_papers",
    find_papers,
)

graph.add_node(
    "fallback",
    fallback,
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    lambda state:
    state["route"],
    {
        "concept_explanation":
            "concept_explanation",

        "paper_deep_dive":
            "paper_deep_dive",

        "compare_approaches":
            "compare_approaches",

        "recent_developments":
            "recent_developments",

        "find_papers":
            "find_papers",

        "out_of_scope":
            "fallback",
    },
)

graph.add_edge(
    "concept_explanation",
    END,
)

graph.add_edge(
    "paper_deep_dive",
    END,
)

graph.add_edge(
    "compare_approaches",
    END,
)

graph.add_edge(
    "recent_developments",
    END,
)

graph.add_edge(
    "find_papers",
    END,
)

graph.add_edge(
    "fallback",
    END,
)

research_graph = (
    graph.compile()
)