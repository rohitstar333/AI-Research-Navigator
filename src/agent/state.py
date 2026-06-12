from typing import TypedDict, List, Dict, Optional

class ResearchState(TypedDict):
    query: str
    route: str

    answer: str

    retrieved_chunks: List[Dict]

    filters: Dict

    paper_name: Optional[str]

    method_a: Optional[str]
    method_b: Optional[str]