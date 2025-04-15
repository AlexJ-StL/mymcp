import React, { useState } from 'react';
import './App.css'; // Main app styles

// Import Components
import Header from './Header';
import ChefSelector from './ChefSelector';
import Menu from './Menu';
import OrderForm from './OrderForm';
import LiveStatus, { STATUS } from './LiveStatus'; // Import STATUS constants
import ResultsDisplay from './ResultsDisplay';

function App() {
  // State Variables
  const [prompt, setPrompt] = useState("");
  const [status, setStatus] = useState(STATUS.IDLE); // Initial status
  const [generatedConfig, setGeneratedConfig] = useState("");
  const [generatedCode, setGeneratedCode] = useState("");
  const [filePaths, setFilePaths] = useState(null);
  const [errorMessage, setErrorMessage] = useState(""); // For displaying errors

  // Event Handlers
  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleMenuSelect = (selectedPrompt) => {
    setPrompt(selectedPrompt); // Update prompt state with selected example
  };

  const handleSubmit = async () => {
    // Reset previous results and errors
    setGeneratedCode("");
    setGeneratedConfig("");
    setFilePaths(null);
    setErrorMessage("");
    setStatus(STATUS.ORDERED); // 1. Set status to Ordered

    // Simulate "Cooking" starting almost immediately
    // In a real scenario with backend updates, this might be triggered by a backend event
    setTimeout(() => setStatus(STATUS.COOKING), 100); // 2. Set status to Cooking (simulated)

    try {
      console.log("Sending prompt:", prompt); // Debug log

      // Make the API call (without outputDir)
      const response = await fetch("http://localhost:5000/api/generate-mcp", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt }), // Only send the prompt
      });

      if (!response.ok) {
        let errorMsg = `HTTP error! status: ${response.status}`;
        try {
          const errorData = await response.json();
          console.error("Server error response:", errorData); // Debug log
          errorMsg = errorData.error || errorMsg; // Use server error message if available
        } catch {
          // Ignore if response is not JSON
        }
        throw new Error(errorMsg);
      }

      const data = await response.json();
      console.log("Received data:", data); // Debug log

      // Extract code and config
      const responseText = data.response || "";
      const pythonCodeMatch = responseText.match(/```python([\s\S]*?)```/);
      const jsonConfigMatch = responseText.match(/```json([\s\S]*?)```/);

      setGeneratedCode(pythonCodeMatch ? pythonCodeMatch[1].trim() : "");
      setGeneratedConfig(jsonConfigMatch ? jsonConfigMatch[1].trim() : "");
      setFilePaths(data.files || null);
      setStatus(STATUS.DELIVERED); // 3. Set status to Delivered on success

    } catch (error) {
      console.error("Error generating MCP server:", error);
      setErrorMessage("Error: " + error.message);
      setGeneratedConfig(""); // Clear any partial results on error
      setGeneratedCode("");
      setFilePaths(null);
      setStatus(STATUS.ERROR); // 4. Set status to Error
    }
  };

  // Render the application
  return (
    <div className="App">
      <Header />
      <main className="app-content">
        <ChefSelector /> {/* Currently static */}
        <Menu onSelect={handleMenuSelect} /> {/* Pass handler */}
        <OrderForm
          prompt={prompt}
          onPromptChange={handlePromptChange}
          onSubmit={handleSubmit}
        />
        <LiveStatus status={status} /> {/* Pass current status */}
        {/* Display error message if status is ERROR */}
        {status === STATUS.ERROR && errorMessage && (
          <div className="error-message-container">{errorMessage}</div>
        )}
        {/* Display results only when delivered successfully */}
        {status === STATUS.DELIVERED && (
          <ResultsDisplay
            generatedCode={generatedCode}
            generatedConfig={generatedConfig}
            filePaths={filePaths}
          />
        )}
      </main>
    </div>
  );
}

export default App;
