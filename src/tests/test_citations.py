from src.retrivel.citation_builder import (
    CitationBuilder,
)


class MockPoint:

    def __init__(self):

        self.payload = {

            "doc_id":
                "paper_001",

            "title":
                "Attention Is All You Need",

            "authors":
                ["Ashish Vaswani"],

            "year":
                2017,

            "section_title":
                "Attention",

            "source_url":
                "https://arxiv.org/abs/1706.03762",
        }


def test_citation_generation():

    builder = (
        CitationBuilder()
    )

    citations = (
        builder.build(
            [MockPoint()]
        )
    )

    assert (
        len(citations)
        == 1
    )

    assert (
        citations[0]["doc_id"]
        ==
        "paper_001"
    )

    assert (
        citations[0]["title"]
        ==
        "Attention Is All You Need"
    )

    assert (
        citations[0]["year"]
        ==
        2017
    )

    assert (
        citations[0]["authors"]
        ==
        "Ashish Vaswani"
    )