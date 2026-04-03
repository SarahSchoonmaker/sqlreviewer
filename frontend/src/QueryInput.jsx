import { useState } from "react";

export default function QueryInput({ onAnalyze }) {
  const [query, setQuery] = useState("");

  return (
    <div>
      <textarea
        rows={6}
        style={{ width: "100%" }}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={() => onAnalyze(query)}>Analyze</button>
    </div>
  );
}