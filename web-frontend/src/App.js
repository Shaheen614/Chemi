import React, { useState } from "react";
import UploadCSV from "./components/UploadCSV";
import SummaryTable from "./components/SummaryTable";
import Charts from "./components/Charts";
import DownloadReport from "./components/DownloadReport";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Chemical Equipment Visualizer</h1>
      <UploadCSV setSummary={setSummary} />
      <SummaryTable summary={summary} />
      <Charts summary={summary} />
      <DownloadReport />
    </div>
  );
}

export default App;
