import React from "react";

export default function SummaryTable({ summary }) {
  if (!summary) return null;

  return (
    <table border="1" style={{ marginTop: "20px", width: "100%" }}>
      <thead>
        <tr>
          <th>Total Count</th>
          <th>Avg Flowrate</th>
          <th>Avg Pressure</th>
          <th>Avg Temperature</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{summary.count}</td>
          <td>{summary.avg_flowrate.toFixed(2)}</td>
          <td>{summary.avg_pressure.toFixed(2)}</td>
          <td>{summary.avg_temperature.toFixed(2)}</td>
        </tr>
      </tbody>
    </table>
  );
}
