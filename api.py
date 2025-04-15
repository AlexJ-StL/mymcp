import os
import json
import re
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
model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

PROMPT_TEMPLATE = """Create a minimal Python MCP server and its JSON configuration based on the following user description:

User Description: {user_description}

The Python code should be a functional server implementing the tools listed in the JSON configuration. If no tools are specified, provide a simple "Hello, world!" example. The server should use the `FastMCP` class from the `MCP` library (assuming it's installed). Include necessary import statements.

The JSON configuration should include:
* "name": A descriptive name for the server (derived from the user description)
* "description": A brief description of the server's purpose (derived from the user description)
* "tools": An array of objects, each with a "name" and "description" describing the tools the server provides. If the user description doesn't specify tools, leave this array empty. Each tool should be a simple function."""

def write_files(response_text: str, output_directory: str) -> Dict[str, str]:
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Extract Python code and JSON configuration using Python regex
        python_match = re.search(r'```python([\s\S]*?)```', response_text)
        json_match = re.search(r'```json([\s\S]*?)```', response_text)

        # Use group(1) to get the captured content
        python_code = python_match.group(1).strip() if python_match else ""
        json_config = json_match.group(1).strip() if json_match else ""

        # Write Python file
        python_path = os.path.join(output_directory, "server.py")
        with open(python_path, "w") as f:
            f.write(python_code)

        # Write JSON file
        json_path = os.path.join(output_directory, "config.json")
        with open(json_path, "w") as f:
            # Pretty print the JSON
            if json_config:
                json_obj = json.loads(json_config)
                json.dump(json_obj, f, indent=4)

        return {
            "python_path": python_path,
            "json_path": json_path
        }
    except Exception as e:
        print(f"Error writing files: {str(e)}")
        print(traceback.format_exc())
        # Return an error dictionary instead of raising
        return {
            "error": str(e),
            "python_path": "",
            "json_path": ""
        }

def generate_mcp_server(user_description: str, output_directory: str = "./generated_server") -> Dict[str, Any]:
    try:
        prompt = PROMPT_TEMPLATE.format(
            user_description=user_description
        )
        response: GenerateContentResponse = model.generate_content(prompt)

        # Write files and get their paths
        file_paths = write_files(response.text, output_directory)

        return {
            'response': response.text,
            'status': 'success',
            'files': file_paths
        }
    except Exception as e:
        print(f"Error in generate_mcp_server: {str(e)}")
        print(traceback.format_exc())
        raise

@api_bp.route('/generate-mcp', methods=['POST'])
def generate_mcp_endpoint():
    try:
        data = request.json
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Missing prompt'}), 400

        output_directory = data.get('outputDir', './generated_server') # Default output directory

        print(f"Received prompt: {data['prompt']}")  # Debug log
        print(f"Output directory: {output_directory}")  # Debug log

        result = generate_mcp_server(data['prompt'], output_directory)
        return jsonify(result)
    except Exception as e:
        print(f"Error in generate_mcp_endpoint: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
