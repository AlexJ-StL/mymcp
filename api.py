import os
from flask import Blueprint, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
from typing import Dict, Any, Optional, List, Union
from google.generativeai.types import GenerateContentResponse

api_bp = Blueprint('api', __name__)
CORS(api_bp, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000",]
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
model = genai.GenerativeModel('gemini-pro')


# Type definitions for your MCP structures
class MCPConfig(Dict[str, Any]):
    pass


class ToolConfig(Dict[str, Any]):
    pass


def generate_mcp_server(prompt: str) -> MCPConfig:
    # Remove async/await since generate_content is synchronous
    response: GenerateContentResponse = model.generate_content(prompt)
    # Add any parsing logic here
    return MCPConfig({'response': response.text})


def generate_tool_framework(prompt: str) -> ToolConfig:
    # Remove async/await since generate_content is synchronous
    response: GenerateContentResponse = model.generate_content(prompt)
    # Add any parsing logic here
    return ToolConfig({'response': response.text})


@api_bp.route('/generate-mcp', methods=['POST'])
def generate_mcp_endpoint():
    data = request.json
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing prompt'}), 400

    result = generate_mcp_server(data['prompt'])
    return jsonify(result)


@api_bp.route('/generate-tool', methods=['POST'])
def generate_tool_endpoint():
    data = request.json
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing prompt'}), 400

    result = generate_tool_framework(data['prompt'])
    return jsonify(result)
