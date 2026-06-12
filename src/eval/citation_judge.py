from ollama import chat

from src.eval.citation_rubric import (
    RUBRIC,
)


def judge_answer(
    answer,
):

    prompt = f"""
{RUBRIC}

Answer:

{answer}
"""

    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return (
        response.message.content
        .strip()
    )