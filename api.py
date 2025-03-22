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


# Type definitions for your MCP structures
class MCPConfig(Dict[str, Any]):
    pass


class ToolConfig(Dict[str, Any]):
    pass


def generate_mcp_server(prompt: str) -> MCPConfig:
    try:
        response: GenerateContentResponse = model.generate_content(prompt)
        return MCPConfig({'response': response.text})
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

        print(f"Received prompt: {data['prompt']}")  # Debug log

        result = generate_mcp_server(data['prompt'])
        return jsonify(result)
    except Exception as e:
        print(f"Error in generate_mcp_endpoint: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
