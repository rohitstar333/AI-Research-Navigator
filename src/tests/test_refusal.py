from src.retrivel.refusal_checker import (
    RefusalChecker,
)


class MockPoint:

    def __init__(
        self,
        title,
        section,
    ):

        self.payload = {

            "title":
                title,

            "section_title":
                section,
        }


def test_refuse_when_no_results():

    checker = (
        RefusalChecker()
    )

    assert (
        checker.should_refuse(
            "What is attention?",
            [],
        )
        is True
    )


def test_refuse_when_no_match():

    checker = (
        RefusalChecker()
    )

    points = [

        MockPoint(
            "Cooking Recipes",
            "Food",
        ),

        MockPoint(
            "Travel Guide",
            "Tourism",
        ),
    ]

    assert (
        checker.should_refuse(
            "What is attention?",
            points,
        )
        is True
    )


def test_accept_when_match_exists():

    checker = (
        RefusalChecker()
    )

    points = [

        MockPoint(
            "Attention Is All You Need",
            "Attention",
        ),

        MockPoint(
            "Transformers",
            "Architecture",
        ),
    ]

    assert (
        checker.should_refuse(
            "What is attention?",
            points,
        )
        is False
    )