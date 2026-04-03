# SQLReviewer/db/models.py

from sqlalchemy import Column, Integer, Text, Boolean, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector
from datetime import datetime

Base = declarative_base()


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True)
    query_text = Column(Text, nullable=False)
    normalized_query = Column(Text, nullable=False)
    fingerprint = Column(Text, nullable=True)  # for deduplication
    embedding = Column(Vector(384), nullable=True)  # pgvector embedding
    has_retail_filter = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index('idx_fingerprint', 'fingerprint'),
    )

    def __repr__(self):
        return f"<Query id={self.id} retail={self.has_retail_filter}>"


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    query_id = Column(Integer, nullable=False)
    review_text = Column(Text, nullable=False)
    tag = Column(Text, nullable=True)
    is_correct = Column(Boolean, default=None)  # nullable for undecided
    feedback_type = Column(Text, nullable=True)
    reviewer = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Review id={self.id} query_id={self.query_id} reviewer={self.reviewer}>"