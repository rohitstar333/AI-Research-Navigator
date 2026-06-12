from src.retrivel.query_understanding import (
    understand_query,
)


def test_recent_query():

    result = understand_query(
        "recent work on speculative decoding"
    )

    assert (
        result["filters"][
            "year_min"
        ]
        == 2023
    )

    assert (
        "speculative_decoding"
        in
        result["filters"][
            "tags"
        ]
    )


def test_foundational_query():

    result = understand_query(
        "foundational transformer papers"
    )

    assert (
        result["filters"][
            "is_foundational"
        ]
        is True
    )

    assert (
        "transformers"
        in
        result["filters"][
            "tags"
        ]
    )


def test_year_query():

    result = understand_query(
        "attention papers from 2024"
    )

    assert (
        result["filters"][
            "year"
        ]
        == 2024
    )

    assert (
        "attention"
        in
        result["filters"][
            "tags"
        ]
    )