from pathlib import Path

from src.ingest.pdf_parser import parse_pdf
from src.ingest.chunker import create_document_chunks

pdfs = list(
    Path("documents/arxiv").glob("*.pdf")
)

pdf_path = str(pdfs[0])

print("Using:", pdf_path)

text = parse_pdf(pdf_path)

chunks = create_document_chunks(text)

print("\nTotal Chunks:")
print(len(chunks))

print("\nFirst Chunk:")
print(chunks[0])

print("\nSecond Chunk:")
print(chunks[1])