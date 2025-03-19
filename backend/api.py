import os
from flask import Blueprint, jsonify, request, Response
from google.genai import GenerativeModel
from typing import Any, Dict, Union, Tuple  # For type hints


api_bp = Blueprint('api', __name__)

GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "No Gemini API key found. "
        "Set the GEMINI_API_KEY environment variable."
    )

model = GenerativeModel(
    model_name='gemini-2.0-pro-exp-0205',
    api_key=GOOGLE_API_KEY
)


@api_bp.route('/generate_mcp_server', methods=['POST'])
def generate_mcp_server() -> Union[
    Dict[str, Union[str, Any]],
    Tuple[Response, int]
]:
    prompt = request.get_json().get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        if not isinstance(prompt, str):
            return jsonify({"error": "Prompt must be a string"}), 400
        response = model.generate_content(prompt)
        mcp_server_code = response.text
        return jsonify({"mcp_server_code": mcp_server_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
