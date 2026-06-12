# src/tests/test_md_parser.py

from src.ingest.md_parser import (
    parse_markdown,
)


def test_parse_markdown(tmp_path):

    test_file = (
        tmp_path / "test.md"
    )

    test_file.write_text(
        "# Hello World"
    )

    content = parse_markdown(
        test_file
    )

    assert content == (
        "# Hello World"
    )