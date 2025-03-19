# MyMCP Prompt

## Description

MyMCP Prompt is a tool for generating MCP servers, tools, and agent prompts from natural language. This MVP focuses on generating MCP servers using the Google Gemini API.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd mymcp
    ```

2.  **Backend Setup:**

    Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

    Create and activate a virtual environment (using uv):

    ```bash
    uv venv
    source .venv/Scripts/activate
    ```

    Install dependencies:

    ```bash
    uv pip install -r requirements.txt
    ```
    (Note: We haven't created `requirements.txt` yet, but we will.)

3.  **Frontend Setup:**

     Navigate to the `frontend` directory:
    ```
     cd ../frontend
    ```
    (We will set up the frontend later)

4.  **Set the Gemini API Key:**

    Obtain a Google Gemini API key and set it as an environment variable named `GEMINI_API_KEY`.

    **Windows:**

    ```bash
    setx GEMINI_API_KEY "your_api_key"
    ```

    **macOS / Linux:**

    Add the following line to your `.bashrc`, `.zshrc`, or other shell configuration file:

    ```bash
    export GEMINI_API_KEY="your_api_key"
    ```

    Then, source the file:

    ```bash
    source ~/.bashrc  # Or ~/.zshrc, etc.
    ```

## Usage
1.  Navigate to the `backend` directory.
2.  Activate the venv:
    ```bash
    source .venv/Scripts/activate
    ```
3.  Run the Flask app:
    ```
    flask run
    ```
4. The app will be available at `http://127.0.0.1:5000`.

## Change Log

-   **v0.1.0 (MVP):** Initial release with basic MCP server generation using Google Gemini.

## Future Features

-   Integration with additional LLMs (OpenRouter, LiteLLM, OpenAI, Anthropic, SombaNova, Cerebras, LM Studio, Ollama, Groq).
-   Support for generating tools/function calls.
-   Support for generating agent prompts.
-   Improved error handling and user feedback.
-   More sophisticated MCP server code generation.
-   UI enhancements.