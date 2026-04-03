const API_URL = "http://localhost:8000";

export async function analyzeQuery(query) {
  const res = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query })
  });

  return res.json();
}

export async function submitReview(payload) {
  const res = await fetch(`${API_URL}/review`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  });

  return res.json();
}