import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/sqlintel")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
SIMILARITY_THRESHOLD = 0.85