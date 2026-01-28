import React from "react";
import { Bar } from "react-chartjs-2";

export default function Charts({ summary }) {
  if (!summary) return null;
  const data = {
    labels: Object.keys(summary.type_distribution),
    datasets: [{
      label: "Equipment Types",
      data: Object.values(summary.type_distribution),
      backgroundColor: "rgba(75,192,192,0.6)"
    }]
  };
  return <Bar data={data} />;
}
