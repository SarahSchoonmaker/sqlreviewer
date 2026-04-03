export default function ResultsPanel({ result }) {
  return (
    <div>
      <h3>Retail Filter: {result.retail_filter ? "YES" : "NO"}</h3>
      <p>Confidence: {result.confidence}</p>
      <p>{result.explanation}</p>
    </div>
  );
}