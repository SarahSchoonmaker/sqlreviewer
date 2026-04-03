import { useState } from "react";
import { analyzeQuery } from "./api";

import QueryInput from "./components/QueryInput";
import ResultsPanel from "./components/ResultsPanel";
import SimilarQueries from "./components/SimilarQueries";
import ReviewPanel from "./components/ReviewPanel";

export default function App() {
  const [result, setResult] = useState(null);

  const handleAnalyze = async (query) => {
    const res = await analyzeQuery(query);
    setResult(res);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>SQL Intelligence Platform</h1>

      <QueryInput onAnalyze={handleAnalyze} />

      {result && (
        <>
          <ResultsPanel result={result} />
          <SimilarQueries queries={result.similar_queries} />
          <ReviewPanel queryId={result.query_id} />
        </>
      )}
    </div>
  );
}