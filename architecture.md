# Architecture

## Overview

AI Research Navigator is a Retrieval-Augmented Generation (RAG) system designed for exploring AI research papers and technical documents.

The system ingests research documents, chunks them into searchable units, stores embeddings in Qdrant, retrieves relevant information using hybrid retrieval, and generates cited answers using a local language model.

---

## System Architecture

Documents

↓

Parsers (PDF / Markdown)

↓

Chunker

↓

Metadata Builder

↓

Embeddings (all-MiniLM-L6-v2)

↓

Qdrant Vector Database

↓

Retrieval Layer

├── Dense Retrieval

├── BM25 Retrieval

└── Hybrid Retrieval

↓

Citation Builder

↓

Refusal Checker

↓

Answer Generator (Qwen 2.5 3B)

↓

Final Response

---

## Components

### Ingestion Layer

Responsible for:

* Parsing documents
* Chunking content
* Building metadata
* Creating embeddings
* Uploading vectors to Qdrant

Files:

* src/ingest/

### Retrieval Layer

Responsible for:

* Dense retrieval
* BM25 retrieval
* Hybrid retrieval
* Metadata filtering

Files:

* src/retrivel/

### Generation Layer

Responsible for:

* Context assembly
* Citation generation
* Answer generation

Files:

* src/generate/

### Agent Layer

Responsible for:

* Query routing
* LangGraph workflow execution
* Paper lookup tools

Files:

* src/agent/

### Evaluation Layer

Responsible for:

* Precision@K
* Recall@K
* Citation faithfulness
* Refusal accuracy
* Latency measurement

Files:

* src/eval/

---

## Retrieval Flow

1. User submits a query.
2. Router determines the query type.
3. Hybrid retrieval fetches relevant chunks.
4. Refusal checker determines whether enough evidence exists.
5. Citations are generated.
6. Answer generator creates a cited response.
7. Final answer is returned.

---

## Technology Stack

* Python
* LangGraph
* Qdrant
* Sentence Transformers
* Ollama
* Qwen 2.5 3B
* Pytest
* Mypy
* Structlog
* Docker
