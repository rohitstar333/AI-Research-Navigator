# src/tests/test_config.py

from src.config import settings


def test_config():

    assert settings.qdrant_port == 6333