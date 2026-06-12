# src/tests/test_parser.py

from pathlib import Path
from src.ingest.pdf_parser import parse_pdf

pdf = list(
    Path("documents/arxiv").glob("*.pdf")
)[0]

text = parse_pdf(str(pdf))

print(text[:5000])