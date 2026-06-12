from src.agent.graph import (
    research_graph,
)


def test_concept_route():

    result = research_graph.invoke(
        {
            "query": "What is attention?",
            "route": "",
            "answer": "",
            "retrieved_chunks": [],
            "filters": {},
            "paper_name": None,
            "method_a": None,
            "method_b": None,
        }
    )

    assert result["route"] == (
        "concept_explanation"
    )


def test_paper_route():

    result = research_graph.invoke(
        {
            "query": "Explain BERT",
            "route": "",
            "answer": "",
            "retrieved_chunks": [],
            "filters": {},
            "paper_name": None,
            "method_a": None,
            "method_b": None,
        }
    )

    assert result["route"] == (
        "paper_deep_dive"
    )


def test_out_of_scope_route():

    result = research_graph.invoke(
        {
            "query": "Capital of France",
            "route": "",
            "answer": "",
            "retrieved_chunks": [],
            "filters": {},
            "paper_name": None,
            "method_a": None,
            "method_b": None,
        }
    )

    assert result["route"] == (
        "out_of_scope"
    )