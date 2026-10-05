from typing import Any
from fastapi.responses import JSONResponse

def build_json_response(status_code: int, payload: dict[str, Any]) -> JSONResponse:
    body = {"status_code": status_code, **payload}
    return JSONResponse(status_code=status_code, content=body)