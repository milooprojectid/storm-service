from typing import Dict, Any
from flask import jsonify, make_response

def api_response(payload: Dict[str, Any]) -> Any:
    return make_response(
        jsonify(payload)
    )