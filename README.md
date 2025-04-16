# MyMCP Prompt

## Description

MyMCP Prompt is a tool for generating Model Context Protocol (MCP) servers from natural language descriptions. This MVP uses the Google Gemini API to convert user descriptions into functional Python MCP servers with corresponding JSON configurations.

## Project Structure

The application consists of:

-   **Flask Backend (Root Directory):**
    -   `app.py`: Main Flask application setup (CORS, blueprint registration).
    -   `api.py`: Contains the `/api/generate-mcp` endpoint which interacts with the Google Gemini API to generate server code and configuration.
    -   `requirements.txt`: Lists Python dependencies.
-   **React Frontend (`/frontend-vite` Directory):**
    -   Provides a web interface (`frontend-vite/src/App.js`) for users to input server descriptions.
    -   Displays the generated Python code and JSON configuration.
    -   Shows the paths where the generated files are saved.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/AlexJ-StL/mymcp
    cd mymcp
    ```

2.  **Backend Setup (Root Directory):**

    Create and activate a virtual environment (using uv is recommended):

    ```bash
    # In the project root directory (mymcp)
    uv venv
    source .venv/Scripts/activate  # On Windows
    # source .venv/bin/activate    # On macOS/Linux
    ```

    Install Python dependencies:

    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Frontend Setup:**

    Navigate to the `frontend-vite` directory:

    ```bash
    cd frontend-vite
    ```

    Install Node.js dependencies:

    ```bash
    npm install
    ```

    Navigate back to the root directory:
    ```bash
    cd ..
    ```


4.  **Set the Gemini API Key:**

    **Important:** Obtain a Google Gemini API key and set it as an environment variable named `GEMINI_API_KEY`. **Do not commit your API key to the repository.**

    **Windows (Command Prompt):**

    ```bash
    set GEMINI_API_KEY=your_api_key
    ```
    **Windows (PowerShell):**
    ```powershell
    $env:GEMINI_API_KEY="your_api_key"
    ```
    *(Note: This sets the variable only for the current session. For persistent setting, use `setx` or system environment variables settings.)*

    **macOS / Linux:**

    Add the following line to your `.bashrc`, `.zshrc`, or other shell configuration file:

    ```bash
    export GEMINI_API_KEY="your_api_key"
    ```

    Then, source the file (or open a new terminal):

    ```bash
    source ~/.bashrc  # Or ~/.zshrc, etc.
    ```

## Usage

1.  **Start the Backend Server:**
    -   Ensure your virtual environment is activated in the root directory.
    -   Make sure the `GEMINI_API_KEY` environment variable is set.
    -   Run the Flask app:
        ```bash
        # In the project root directory (mymcp)
        flask run
        ```
    -   The backend will be available at `http://127.0.0.1:5000`.

2.  **Start the Frontend Development Server:**
    -   Open a *new* terminal.
    -   Navigate to the `frontend-vite` directory:
        ```bash
        cd frontend-vite
        ```
    -   Run the React app:
        ```bash
        npm run dev
        ```
    -   The frontend will open automatically in your browser, usually at `http://localhost:5173`.

3.  **Use the Application:**
    -   Open `http://localhost:5173` in your browser.
    -   Enter a description for the MCP server you want to generate.
    -   Click "Place Your Order".
    -   The generated Python code and JSON configuration will be displayed, and the files will be saved to the `generated_server` directory (or a directory chosen by the LLM).

## Change Log

-   **v0.1.0 (MVP):** Initial release with basic MCP server generation using Google Gemini. Backend in root, frontend in `/frontend`.
-   **v0.2.0 (Vite Frontend & UI Redesign):** Migrated frontend from Create React App to Vite for improved performance, reduced vulnerabilities, and better developer experience. Implemented a new French café-themed UI. Removed the output directory input from the frontend, allowing the backend to choose the output directory. Updated the backend API to handle requests without an output directory.

## Future Features

-   Integration with additional LLMs (OpenRouter, LiteLLM, OpenAI, Anthropic, SombaNova, Cerebras, LM Studio, Ollama, Groq).
-   Support for generating tools/function calls within the MCP server.
-   Support for generating agent prompts.
-   Improved error handling and user feedback.
-   More sophisticated MCP server code generation (e.g., using templates, better structure).
-   UI enhancements.
-   Unit tests for backend and frontend.