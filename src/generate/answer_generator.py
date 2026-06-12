from ollama import chat
from src.config import settings


class AnswerGenerator:

    def generate(
        self,
        question,
        retrieved_points,
        citations,
    ):

        context = ""

        for point in retrieved_points[:3]:

            payload = point.payload

            context += (
                f"\n\nDOCUMENT: "
                f"{payload.get('title', '')}\n"
                f"SECTION: "
                f"{payload.get('section_title', '')}\n\n"
                f"{payload.get('text', '')}"
            )

        prompt = f"""
You are a research assistant working only with a retrieved document corpus.

Question:
{question}

Retrieved Context:
{context}

Available Citations:

[1] Retrieved Source 1
[2] Retrieved Source 2
[3] Retrieved Source 3

Instructions:

- Answer ONLY from the retrieved context.
- If the retrieved context contains relevant information, answer the question using that information.
- Do NOT refuse if the context contains partial but useful information.
- Refuse ONLY when the retrieved context is completely unrelated to the question.
- Every factual sentence must end with a citation marker such as [1], [2], or [3].
- Never make a factual claim without a citation.
- Use multiple citations when information comes from multiple sources.
- Do not invent facts.
- Do not invent citations.
- If the retrieved context is completely insufficient or unrelated, respond exactly:

"I don't have enough relevant material in the corpus to answer this confidently."

Example:

Qwen is a family of large language models developed by Alibaba Cloud [1].

Qwen models support text, image, audio, and video understanding [1].

Return only the answer.
"""

        response = chat(
            model=settings.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        answer = (
            response.message.content
        )

        prompt_tokens = len(
            prompt.split()
        )

        answer_tokens = len(
            answer.split()
        )

        total_tokens = (
            prompt_tokens
            + answer_tokens
        )

        print(
            "\nTOKEN USAGE"
        )

        print(
            f"Prompt Tokens: {prompt_tokens}"
        )

        print(
            f"Answer Tokens: {answer_tokens}"
        )

        print(
            f"Total Tokens: {total_tokens}"
        )

        answer += "\n\nREFERENCES\n"

        for citation in citations:

            answer += (
                f"\n[{citation['citation_id']}] "
                f"{citation['title']} | "
                f"{citation['authors']} | "
                f"{citation['year']} | "
                f"{citation['section']} | "
                f"{citation['source_url']}"
            )

        return answer