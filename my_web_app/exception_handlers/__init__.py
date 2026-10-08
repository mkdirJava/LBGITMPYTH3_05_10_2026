
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def universal_catch_all_handler(request: Request, exc: Exception):
    # Log tracebacks or send alerts here
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal Server Error", "message": "I am not telling you "}
    )

def apply_exception(app: FastAPI):
    app.add_exception_handler(RequestValidationError, universal_catch_all_handler)