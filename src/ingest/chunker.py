import re


def split_into_sections(text: str):
    """
    Split text into sections using common academic paper headings.
    """

    section_pattern = r"\n(\d+)\n([A-Z][A-Za-z\s\-]+)\n"

    matches = list(
        re.finditer(
            section_pattern,
            text,
        )
    )

    sections = []

    if not matches:

        return [
            {
                "section_title": "Document",
                "content": text,
            }
        ]

    for i, match in enumerate(
        matches
    ):

        section_title = (
            match.group(2)
            .strip()
        )

        start = match.end()

        if i + 1 < len(matches):

            end = matches[
                i + 1
            ].start()

        else:

            end = len(text)

        section_content = (
            text[start:end]
            .strip()
        )

        sections.append(
            {
                "section_title": section_title,
                "content": section_content,
            }
        )

    return sections


def chunk_text(
    text: str,
    chunk_size: int = 1200,
):
    """
    Create chunks using paragraphs instead
    of fixed character boundaries.
    """

    paragraphs = text.split(
        "\n\n"
    )

    chunks = []

    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = (
            paragraph.strip()
        )

        if not paragraph:
            continue

        if (
            len(current_chunk)
            + len(paragraph)
            < chunk_size
        ):

            current_chunk += (
                paragraph
                + "\n\n"
            )

        else:

            chunks.append(
                current_chunk.strip()
            )

            current_chunk = (
                paragraph
                + "\n\n"
            )

    if current_chunk.strip():
     chunks.append(
        current_chunk.strip()
    )

    return chunks


def create_document_chunks(
    text: str,
    chunk_size: int = 1200,
):
    """
    Split document into sections,
    then split each section into chunks.
    """

    sections = split_into_sections(
        text
    )

    all_chunks = []

    chunk_index = 0

    for (
        section_index,
        section,
    ) in enumerate(
        sections
    ):

        section_chunks = (
            chunk_text(
                section["content"],
                chunk_size=chunk_size,
            )
        )

        for chunk in section_chunks:

            all_chunks.append(
                {
                    "section_title": section[
                        "section_title"
                    ],
                    "section_index": section_index,
                    "chunk_index": chunk_index,
                    "text": chunk,
                }
            )

            chunk_index += 1

    return all_chunks