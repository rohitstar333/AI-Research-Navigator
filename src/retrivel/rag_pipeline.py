from src.retrivel.query_understanding import (
    understand_query,
)

from src.retrivel.hybrid_retriever import (
    HybridRetriever,
)

from src.retrivel.citation_builder import (
    CitationBuilder,
)

from src.generate.answer_generator import (
    AnswerGenerator,
)

from src.retrivel.refusal_checker import (
    RefusalChecker,
)

from src.agent.tools import (
    lookup_paper,
)

from src.logger import (
    logger,
)


class RAGPipeline:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

        self.citation_builder = (
            CitationBuilder()
        )

        self.answer_generator = (
            AnswerGenerator()
        )

        self.refusal_checker = (
            RefusalChecker()
        )

    def run(
        self,
        question,
    ):

        logger.info(
            "rag_pipeline_started",
            question=question,
        )

        query_info = (
            understand_query(
                question
            )
        )

        paper_name = (
            lookup_paper(
                question
            )
        )

        if paper_name:

            question = (
                paper_name
            )

        filters = None

        results = (
            self.retriever.search(
                query=question,
                limit=5,
                filters=filters,
            )
        )

        logger.info(
            "retrieval_completed",
            retrieved_chunks=len(results),
        )

        if (
            self.refusal_checker
            .should_refuse(
                question,
                results,
            )
        ):

            logger.info(
                "query_refused",
                question=question,
            )

            return (
                self.refusal_checker
                .refusal_message()
            )

        citations = (
            self.citation_builder
            .build(results)
        )

        logger.info(
            "answer_generation_started",
        )

        answer = (
            self.answer_generator
            .generate(
                question,
                results,
                citations,
            )
        )

        logger.info(
            "answer_generation_completed",
        )

        return answer