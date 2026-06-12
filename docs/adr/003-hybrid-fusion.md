# ADR 003 - Hybrid Retrieval

Status: Accepted

Decision:
A hybrid retrieval approach combining dense retrieval and BM25 was selected.

Reason:
Dense retrieval captures semantic similarity while BM25 captures exact keyword matches.

Consequences:
- Higher recall than dense-only retrieval
- Better handling of technical terminology
- Improved robustness across different query styles