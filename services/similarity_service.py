from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Query
from app.config import SIMILARITY_THRESHOLD

def find_similar_queries(embedding):
    db: Session = SessionLocal()

    results = db.execute(
        """
        SELECT id, query_text, 1 - (embedding <=> :embedding) AS similarity
        FROM queries
        ORDER BY embedding <=> :embedding
        LIMIT 5
        """,
        {"embedding": embedding}
    ).fetchall()

    return [
        {"id": r[0], "query": r[1], "similarity": float(r[2])}
        for r in results if r[2] > SIMILARITY_THRESHOLD
    ]