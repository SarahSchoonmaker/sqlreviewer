CREATE EXTENSION IF NOT EXISTS vector;

-- =====================
-- QUERIES TABLE
-- =====================
CREATE TABLE IF NOT EXISTS queries (
    id SERIAL PRIMARY KEY,
    query_text TEXT,
    normalized_query TEXT,
    fingerprint TEXT,
    embedding VECTOR(384),
    has_retail_filter BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_fingerprint ON queries(fingerprint);

-- =====================
-- REVIEWS TABLE
-- =====================
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    query_id INT,
    review_text TEXT,
    tag TEXT,
    is_correct BOOLEAN,
    feedback_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    role TEXT, -- "analyst" or "admin"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);