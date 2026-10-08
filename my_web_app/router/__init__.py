from fastapi import APIRouter, BackgroundTasks,Request
from fastapi.templating import Jinja2Templates
from my_web_app.model import Example,ExampleResponse

router = APIRouter()
templates = Jinja2Templates(directory="my_web_app/templates")

@router.get("/")
def root(request: Request, username:str = "anon"):
    context = {
        "request": request,
        "username":username,
        "items": ["Python", "FastAPI", "Jinja2"]
    }
    
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context=context
    )

def background_task(message:str):
    print(f"I am from the background {message}")

@router.get("/background")
async def background(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task, "Hello World")
    return {"status": "Task running in background"}


@router.get("/here/{message}")
def here(message:str, example: Example) -> ExampleResponse:
    print(message)
    print(example)
    return ExampleResponse(response=f"hi there {example.name}")


from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)
account_router = APIRouter(prefix="/account")
VALID_API_KEY = "my_super_secret_api_token_123"

async def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key"
        )
    return api_key

@account_router.get("/{id}")
def get_account(id:str,api_key: str = Depends(validate_api_key)):
    return f"I have your account {id}"




