import React from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = React.useState("");
  const [outputDir, setOutputDir] = React.useState("./output");
  const [generatedConfig, setGeneratedConfig] = React.useState("");
  const [generatedCode, setGeneratedCode] = React.useState("");

  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleOutputDirChange = (event) => {
    setOutputDir(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      console.log("Sending prompt:", prompt); // Debug log
      console.log("Output directory:", outputDir); // Debug log

      const response = await fetch("http://localhost:5000/api/generate-mcp", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
          prompt: prompt,
          outputDir: outputDir 
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error("Server error response:", errorData); // Debug log
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Received data:", data); // Debug log

      // Split the response into Python code and JSON configuration
      const responseText = data.response || "";
      const pythonCodeMatch = responseText.match(/```python([\s\S]*?)```/);
      const jsonConfigMatch = responseText.match(/```json([\s\S]*?)```/);

      setGeneratedCode(pythonCodeMatch ? pythonCodeMatch[1].trim() : "No Python code generated");
      setGeneratedConfig(jsonConfigMatch ? jsonConfigMatch[1].trim() : "No JSON configuration generated");
    } catch (error) {
      console.error("Error generating MCP server:", error);
      setGeneratedConfig("Error: " + error.message);
      setGeneratedCode("");
    }
  };
  return (
    <div className="App">
      <header className="App-header">
        <h1>MyMCP Prompt</h1>
      </header>
      <main>
        <section>
          <h2>Prompt Input</h2>
          <textarea
            placeholder="Describe your MCP server requirements..."
            value={prompt}
            onChange={handlePromptChange}
          />
        </section>
        <section>
          <h2>Output Directory</h2>
          <input
            type="text"
            placeholder="Enter output directory path..."
            value={outputDir}
            onChange={handleOutputDirChange}
          />
        </section>
        <section>
          <h2>Generated Configuration (JSON)</h2>
          <pre>{generatedConfig}</pre>
        </section>
        <section>
          <h2>Generated Code (Python)</h2>
          <pre>{generatedCode}</pre>
        </section>
        <button onClick={handleSubmit}>Generate MCP Server</button>
      </main>
    </div>
  );
}

export default App;

