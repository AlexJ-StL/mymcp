import React from 'react';
import './ResultsDisplay.css';
import { saveAs } from 'file-saver'; // Assuming FileSaver.js is installed

// Receives generated content and file paths from App.jsx
function ResultsDisplay({ generatedCode, generatedConfig }) {

  // Don't render if there's no code or config yet
  if (!generatedCode && !generatedConfig) {
    return null;
  }

  // Handle cases where generation might have failed partially or fully
  const codeContent = generatedCode || "No Python code was generated.";
  const configContent = generatedConfig || "No JSON configuration was generated.";

  const saveCodeToFile = () => {
    const blob = new Blob([codeContent], { type: "text/x-python;charset=utf-8" });
    saveAs(blob, "server.py"); // Default filename
  };

  const saveConfigToFile = () => {
    const blob = new Blob([configContent], { type: "application/json;charset=utf-8" });
    saveAs(blob, "config.json"); // Default filename
  };

  return (
    <section className="results-display-section">
      <h2 className="section-title">Chef's Creations</h2>
      <div className="results-container">
        <div className="result-block">
          <h3>Generated Code (Python)</h3>
          <pre className="code-block">{codeContent}</pre>
          <button className="save-button" onClick={saveCodeToFile}>Save Python Code</button>
        </div>
        <div className="result-block">
          <h3>Generated Configuration (JSON)</h3>
          <pre className="code-block">{configContent}</pre>
          <button className="save-button" onClick={saveConfigToFile}>Save JSON Config</button>
        </div>
      </div>
    </section>
  );
}

export default ResultsDisplay;