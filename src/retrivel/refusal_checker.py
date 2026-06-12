import re
from src.config import settings


class RefusalChecker:

    def __init__(
        self,
         min_results=settings.refusal_threshold,
    ):

        self.min_results = min_results

    def should_refuse(
        self,
        question,
        retrieved_points,
    ):

        if (
            len(retrieved_points)
            < self.min_results
        ):
            return True

        question_words = set(
            re.findall(
                r"\b[a-zA-Z0-9]+\b",
                question.lower(),
            )
        )

        question_words = {
            word
            for word in question_words
            if len(word) > 3
        }

        matches = 0

        for point in retrieved_points:

            payload = point.payload

            searchable_text = (
                payload.get(
                    "title",
                    ""
                )
                + " "
                + payload.get(
                    "section_title",
                    ""
                )
            ).lower()

            if any(
                word in searchable_text
                for word in question_words
            ):
                matches += 1

        return matches == 0

    def refusal_message(
        self,
    ):

        return (
            "I don't have enough relevant "
            "material in the corpus to answer "
            "this confidently."
        )