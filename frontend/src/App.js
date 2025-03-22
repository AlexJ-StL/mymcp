import React from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = React.useState("");
  const [outputDir, setOutputDir] = React.useState("");
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
      const response = await fetch("http://localhost:5000/api/generate_mcp_server", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setGeneratedConfig(JSON.stringify(data.mcp_server_config, null, 2)); // Assuming backend returns mcp_server_config
      setGeneratedCode(data.mcp_server_code); // Assuming backend returns mcp_server_code
    } catch (error) {
      console.error("Error generating MCP server:", error);
      // Handle error (e.g., display error message to user)
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
            placeholder="Enter your MCP server prompt here..."
            value={prompt}
            onChange={handlePromptChange}
          />
        </section>
        <section>
          <h2>Options</h2>
          <label>
            MCP Server:
            <input type="checkbox" />
          </label>
          {/* Future: Add toggles for Tools and Agent */}
        </section>
        <section>
          <h2>Output Directory</h2>
          <input
            type="text"
            placeholder="Enter output directory..."
            value={outputDir}
            onChange={handleOutputDirChange}
          />
        </section>
        <section>
          <h2>Generated Configuration</h2>
          <pre>{generatedConfig}</pre>
        </section>
        <section>
          <h2>Generated Code</h2>
          <pre>{generatedCode}</pre>
        </section>
        <button onClick={handleSubmit}>Generate MCP Server</button>
      </main>
    </div>
  );
}

export default App;
