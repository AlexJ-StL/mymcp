import os
import traceback
from flask import Blueprint, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
from typing import Dict, Any, Optional, List, Union
from google.generativeai.types import GenerateContentResponse

api_bp = Blueprint('api', __name__)
CORS(api_bp, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "No Gemini API key found. "
        "Set the GEMINI_API_KEY environment variable."
    )

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')

PROMPT_TEMPLATE = """Create a minimal Python MCP server and its JSON configuration based on the following user description:

User Description: {user_description}

Save the Python code to: {output_directory}/server.py
Save the JSON configuration to: {output_directory}/config.json

The Python code should be a functional server implementing the tools listed in the JSON configuration. If no tools are specified, provide a simple "Hello, world!" example. The server should use the `FastMCP` class from the `MCP` library (assuming it's installed). Include necessary import statements.

The JSON configuration should include:
* "name": A descriptive name for the server (derived from the user description)
* "description": A brief description of the server's purpose (derived from the user description)
* "tools": An array of objects, each with a "name" and "description" describing the tools the server provides. If the user description doesn't specify tools, leave this array empty. Each tool should be a simple function."""

def generate_mcp_server(user_description: str, output_directory: str) -> Dict[str, Any]:
    try:
        prompt = PROMPT_TEMPLATE.format(
            user_description=user_description,
            output_directory=output_directory
        )
        response: GenerateContentResponse = model.generate_content(prompt)
        return {
            'response': response.text,
            'status': 'success'
        }
    except Exception as e:
        print(f"Error in generate_mcp_server: {str(e)}")
        print(traceback.format_exc())
        raise

@api_bp.route('/generate-mcp', methods=['POST'])
def generate_mcp_endpoint():
    try:
        data = request.json
        if not data or 'prompt' not in data or 'outputDir' not in data:
            return jsonify({'error': 'Missing prompt or output directory'}), 400

        print(f"Received prompt: {data['prompt']}")  # Debug log
        print(f"Output directory: {data['outputDir']}")  # Debug log

        result = generate_mcp_server(data['prompt'], data['outputDir'])
        return jsonify(result)
    except Exception as e:
        print(f"Error in generate_mcp_endpoint: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
