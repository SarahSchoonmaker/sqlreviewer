# SQLReviewer/db/crud.py

from db.database import SessionLocal
from db.models import Query, Review


def save_query(query_text, normalized_query, fingerprint, embedding, has_retail_filter):
    """
    Save a SQL query into the database with fingerprint, normalized form, embedding, and retail filter flag.
    """
    db = SessionLocal()

    q = Query(
        query_text=query_text,
        normalized_query=normalized_query,
        fingerprint=fingerprint,
        embedding=embedding,
        has_retail_filter=has_retail_filter
    )

    db.add(q)
    db.commit()
    db.refresh(q)

    return q.id


def save_review(query_id, review_text, tag, is_correct, feedback_type=None, reviewer=None):
    """
    Save an investigator review for a query.
    """
    db = SessionLocal()

    r = Review(
        query_id=query_id,
        review_text=review_text,
        tag=tag,
        is_correct=is_correct,
        feedback_type=feedback_type,
        reviewer=reviewer
    )

    db.add(r)
    db.commit()
    db.refresh(r)

    return r.id


def get_reviews_for_similar(similar_queries):
    """
    Retrieve reviews for a list of similar queries.
    """
    db = SessionLocal()

    # Extract IDs of similar queries
    ids = [q["id"] for q in similar_queries]

    if not ids:
        return []

    reviews = db.query(Review).filter(Review.query_id.in_(ids)).all()

    # Format reviews for API consumption
    return [
        {
            "query_id": r.query_id,
            "review": r.review_text,
            "tag": r.tag,
            "is_correct": r.is_correct,
            "feedback_type": r.feedback_type,
            "reviewer": getattr(r, "reviewer", None)
        }
        for r in reviews
    ]