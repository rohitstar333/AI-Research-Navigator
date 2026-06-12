# src/tests/test_tools.py

from src.agent.tools import (
    lookup_paper,
)


def test_lookup_paper():

    result = lookup_paper(
        "Explain BERT"
    )

    assert result is not None