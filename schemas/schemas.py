from pydantic import BaseModel
from typing import List, Dict, Any

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query_id: int
    retail_filter: bool
    matched_columns: List[str]
    similar_queries: List[Dict[str, Any]]
    matching_reviews: List[Dict[str, Any]]
    explanation: str