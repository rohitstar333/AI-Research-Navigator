class CitationBuilder:

    def build(
        self,
        retrieved_points,
    ):

        citations = []

        seen_docs = set()

        citation_id = 1

        for point in retrieved_points:

            payload = point.payload

            doc_id = payload["doc_id"]

            if doc_id in seen_docs:
                continue

            seen_docs.add(doc_id)

            authors = payload.get(
                "authors",
                []
            )

            if len(authors) >= 3:

                author_text = (
                    f"{authors[0]} et al."
                )

            elif len(authors) == 2:

                author_text = (
                    f"{authors[0]}, {authors[1]}"
                )

            elif len(authors) == 1:

                author_text = authors[0]

            else:

                author_text = (
                    "Unknown Author"
                )

            citations.append(
                {
                    "citation_id": citation_id,
                    "doc_id": doc_id,
                    "title": payload.get(
                        "title",
                        ""
                    ),
                    "authors": author_text,
                    "year": payload.get(
                        "year",
                        ""
                    ),
                    "section": payload.get(
                        "section_title",
                        ""
                    ),
                    "source_url": payload.get(
                        "source_url",
                        ""
                    ),
                }
            )

            citation_id += 1

        return citations