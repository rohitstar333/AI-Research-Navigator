from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    embedding_model: str = (
        "all-MiniLM-L6-v2"
    )

    llm_model: str = (
        "qwen2.5:3b"
    )

    qdrant_host: str = (
        "localhost"
    )

    qdrant_port: int = (
        6333
    )

    refusal_threshold: int = (
        2
    )


settings = Settings()