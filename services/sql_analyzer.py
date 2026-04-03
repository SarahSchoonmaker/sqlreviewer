import sqlglot

from app.services.retail_detector import detect_retail_filter
from app.services.embedding_service import get_embedding
from app.services.similarity_service import find_similar_queries
from app.services.ml_classifier import predict_retail
from app.services.fingerprinting import generate_fingerprint

from app.db.crud import save_query, get_reviews_for_similar


def analyze_query_pipeline(sql: str):
    tree = sqlglot.parse_one(sql)

    # Fingerprinting + normalization
    fingerprint, normalized = generate_fingerprint(sql)

    # Rule-based detection
    rule_pred, matched = detect_retail_filter(tree)

    # ML prediction
    ml_pred, confidence = predict_retail(normalized)

    # Final decision
    final_pred = rule_pred or ml_pred

    # Embedding
    embedding = get_embedding(normalized)

    # Similar queries
    similar = find_similar_queries(embedding)

    # Matching reviews
    reviews = get_reviews_for_similar(similar)

    # Save
    query_id = save_query(
        query_text=sql,
        normalized_query=normalized,
        fingerprint=fingerprint,
        embedding=embedding,
        has_retail_filter=final_pred
    )

    return {
        "query_id": query_id,
        "retail_filter": final_pred,
        "confidence": confidence,
        "rule_based": rule_pred,
        "ml_based": ml_pred,
        "matched_columns": matched,
        "similar_queries": similar,
        "matching_reviews": reviews,
        "explanation": (
            f"Rule matched: {matched}" if rule_pred else "ML predicted retail pattern"
        )
    }