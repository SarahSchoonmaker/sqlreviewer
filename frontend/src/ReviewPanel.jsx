import { useState } from "react";
import { submitReview } from "../api";

export default function ReviewPanel({ queryId }) {
  const [review, setReview] = useState("");

  const submit = async () => {
    await submitReview({
      query_id: queryId,
      review,
      tag: "valid",
      is_correct: true
    });
    alert("Review submitted");
  };

  return (
    <div>
      <h3>Submit Review</h3>
      <textarea onChange={(e) => setReview(e.target.value)} />
      <button onClick={submit}>Submit</button>
    </div>
  );
}