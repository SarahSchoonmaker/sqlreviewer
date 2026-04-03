from fastapi import APIRouter, Depends
from api.deps import get_user   # 👈 updated import

from schemas.schemas import QueryRequest, QueryResponse
from services.sql_analyzer import analyze_query_pipeline
from db.crud import save_review

router = APIRouter()


@router.post("/analyze", response_model=QueryResponse)
def analyze(request: QueryRequest):
    return analyze_query_pipeline(request.query)


@router.post("/review")
def submit_review(payload: dict, user: str = Depends(get_user)):
    return save_review(
        query_id=payload["query_id"],
        review_text=payload["review"],
        tag=payload["tag"],
        is_correct=payload["is_correct"],
        feedback_type=payload.get("feedback_type"),
        reviewer=user   # 👈 important
    )