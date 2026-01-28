import React, { useState } from "react";
import API from "../api";

export default function UploadCSV({ setSummary }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await API.post("/upload/", formData);
    setSummary(res.data.summary);
  };

  return (
    <div>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
