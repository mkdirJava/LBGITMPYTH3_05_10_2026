from fastapi import APIRouter, BackgroundTasks,Request
from fastapi.templating import Jinja2Templates
from my_web_app.model import Example,ExampleResponse
from fastapi import Response, Query
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse  

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

@router.get("/heatlh")
def health () -> Response:
    return Response(content="ok",status_code=200)

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

from typing import List

class Transaction(BaseModel):
    transaction_id :str = Field()
    account_number : str = Field()
    transaction_date : str = Field()
    transaction_time : str = Field()
    transaction_type : str = Field()
    amount_gbp : str = Field()

transaction_router = APIRouter(prefix="/transaction")

transactions :List[Transaction] =[
     Transaction(
        transaction_id="TXN-20261009-001",
        transaction_date="2026-10-09",
        transaction_time="08:14:22",
        transaction_type="DEBIT",
        amount_gbp="14.50",
        account_number="001"
    ),
    Transaction(
        transaction_id="TXN-20261009-002",
        transaction_date="2026-10-09",
        transaction_time="09:30:00",
        transaction_type="CREDIT",
        amount_gbp="1250.00",
        account_number="002"
    ),
    Transaction(
        transaction_id="TXN-20261008-001",
        transaction_date="2026-10-08",
        transaction_time="14:22:05",
        transaction_type="DEBIT",
        amount_gbp="89.99",
        account_number="003"
    ),
    Transaction(
        transaction_id="TXN-20261008-002",
        transaction_date="2026-10-08",
        transaction_time="18:45:12",
        transaction_type="DEBIT",
        amount_gbp="6.40",
        account_number="004"
    ),
    Transaction(
        transaction_id="TXN-20261007-001",
        transaction_date="2026-10-07",
        transaction_time="11:05:34",
        transaction_type="DEBIT",
        amount_gbp="123.21",
        account_number="005"
    ),
    Transaction(
        transaction_id="TXN-20261006-001",
        transaction_date="2026-10-06",
        transaction_time="00:01:00",
        transaction_type="CREDIT",
        amount_gbp="45.10",
        account_number="006"
    ),
    Transaction(
        transaction_id="TXN-20261005-001",
        transaction_date="2026-10-05",
        transaction_time="15:30:45",
        transaction_type="DEBIT",
        amount_gbp="320.00",
        account_number="007"
    )
]

@transaction_router.get("/")
def get_transactions(account_number :str= Query(default=..., min_length=0, max_length=50)) -> JSONResponse :
    if account_number is None or len(account_number) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, # Returns 400
            detail="The name 'ALICE' is reserved and cannot be used."
        )
    found_transactions = [trans.model_dump_json() for trans in transactions if trans.account_number  == account_number]
    return JSONResponse (
        content={"account_number": account_number,
        "count": len(found_transactions),
        "transactions": found_transactions
        }, status_code=200)


@transaction_router.get("/filter")
def get_transactions(
    account_number :str = Query(default=..., min_length=0, max_length=50),
    transaction_type: str = Query(default=..., min_length=0, max_length=50)
    ) -> Response:
    if account_number is None or len(account_number) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, # Returns 400
            detail="The name 'ALICE' is reserved and cannot be used."
        )
    
    found_transactions = [trans for trans in transactions if trans.account_number  == account_number and trans.transaction_type == transaction_type]
    return Response(
        content={"account_number": account_number,
        "count": len(found_transactions),
        "transactions": found_transactions
        }, status_code=200)


