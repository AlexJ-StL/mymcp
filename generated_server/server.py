import re
from collections import Counter
from typing import Dict

# Assume MCP library and FastMCP class are installed and available
# pip install mcp-library  (Replace with actual package name if known)
try:
    from MCP import FastMCP
except ImportError:
    print("Error: The 'MCP' library is not installed or FastMCP is not found.")
    print("Please install the required library.")
    # Provide a dummy class for the script to be syntactically valid
    # In a real scenario, you would exit or handle this properly.
    class FastMCP:
        def __init__(self, *args, **kwargs):
            print("Warning: Using dummy FastMCP class.")
        def tool(self):
            def decorator(func):
                print(f"Warning: Dummy registration for tool '{func.__name__}'")
                return func
            return decorator
        def run(self, *args, **kwargs):
            print("Warning: Dummy server run method called.")
            print("Server is not actually running.")

# --- Tool Implementation ---

def count_words(text: str) -> Dict[str, int]:
    """
    Helper function to perform the word counting logic.
    """
    if not text:
        return {}
    # Use regex to find words (sequences of word characters)
    # Convert to lowercase for case-insensitive counting
    words = re.findall(r'\b\w+\b', text.lower())
    # Count frequencies using collections.Counter
    word_counts = Counter(words)
    # Return as a standard dictionary
    return dict(word_counts)

# --- Server Setup ---

# Initialize the MCP server, loading configuration from the JSON file
mcp_server = FastMCP(config_path="config.json")

# Define and register the tool function using the decorator
# The decorator links this function to the tool named "count_word_frequency" in config.json
@mcp_server.tool()
def count_word_frequency(text: str) -> Dict[str, int]:
    """
    MCP Tool: Counts word frequency in the input text.
    Corresponds to the 'count_word_frequency' tool in config.json.
    Args:
        text: The input string to analyze.
    Returns:
        A dictionary mapping each word to its frequency count.
    """
    print(f"Received text for word count: '{text[:50]}...'") # Log received text (truncated)
    result = count_words(text)
    print(f"Word count result: {result}") # Log result
    return result

# --- Run the Server ---

if __name__ == "__main__":
    print("Starting MCP Server...")
    # Run the server (adjust host and port as needed)
    # This will typically start a web server (like Uvicorn/Hypercorn if FastMCP uses FastAPI/Quart)
    # and listen for incoming MCP requests.
    mcp_server.run(host="0.0.0.0", port=8000)
    # The actual run command might differ based on the specific MCP library implementation