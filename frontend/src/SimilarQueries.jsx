export default function SimilarQueries({ queries }) {
  return (
    <div>
      <h3>Similar Queries</h3>
      {queries.map((q) => (
        <div key={q.id}>
          <pre>{q.query}</pre>
          <p>Similarity: {q.similarity}</p>
        </div>
      ))}
    </div>
  );
}