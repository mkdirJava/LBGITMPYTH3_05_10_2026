from fastapi import APIRouter
from fastapi import HTTPException
from app.services.account_service import get_account
from app.schemas.account_schema import AccountCreate, AccountOut

router = APIRouter(prefix="/accounts", tags=["Accounts"])

# Pretend this is data from a database
accounts = {
    1001: {"account_name": "Current Account", "balance": 1250.50},
    1002: {"account_name": "Savings Account", "balance": 5000.00},
}

@router.get("/getAccountData")
def getAccountData():
    return "data"

@router.get("/accounts")
def list_accounts():
    return [{"account_id": 1, "balance": 500.0}]

from fastapi.responses import StreamingResponse
import io
import csv

def generate_csv():
    buffer = io.StringIO()
    buffer.write("account_id,balance\n1,500.0\n2,234.67\n")
    buffer.seek(0)
    return buffer

# Generates and downloads a file called accounts.csv
@router.get("/export")
def export_accounts():
    return StreamingResponse(
        generate_csv(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=accounts.csv"}
    )

# Generates and downloads file called export.csv
@router.get("/export.csv")
async def export_csv():

    def generate():
        output = io.StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow(["id", "name", "email"])
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)

        # Data rows
        rows = [
            [1, "Peter", "peter@example.com"],
            [2, "Alice", "alice@example.com"],
        ]

        for row in rows:
            writer.writerow(row)
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)

    headers = {
        "Content-Disposition": 'attachment; filename="export.csv"'
    }

    return StreamingResponse(
        generate(),
        media_type="text/csv",
        headers=headers
    )

from fastapi.responses import Response
@router.get("/{id}/xml")
def get_account_xml(id: int):
    xml_data = f"""
        <account>
            <account_id>{id}</account_id>
            <balance>500.0</balance>
        </account>
    """
    return Response(content=xml_data, media_type="application/xml")



@router.get("/{id}")
def get_account(id: int):
    db = "DB connection"  # repeated in every route
    return {"id": id, "db": db}


from fastapi import Depends
from app.api.deps import get_db
@router.get("/{id}")
def get_account(id: int, db=Depends(get_db)):
    return {"id": id, "db": db}


@router.post("/{customer_id}/{balance}", response_model=AccountOut, status_code=201)
def create_account(account: AccountCreate):
    return {**account.model_dump(), "account_id": 1}


# MULTIPLE PATH PARAMETERS
@router.get("/customers/{customer_id}/accounts/{account_id}")
def get_customer_account_details(customer_id: int, account_id: int):
    return get_account(customer_id, account_id)

@router.get("/{account_id}")
def get_account(account_id: int):
    account = accounts.get(account_id)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Account {account_id} not found"
        )

    return account
"""
 Running Background Tasks
"""
from fastapi import BackgroundTasks
from datetime import datetime
import time

def record_audit_event(account_id: str):
    time.sleep(5) # sleep for 5 seconds
    print(f"Audit record created for {account_id}, "
          f"time: {(datetime.now())}")

@router.post("/accounts_with_background_tasks")
async def create_account(
    background_tasks: BackgroundTasks
):
    account_id = "ACC12345"

    background_tasks.add_task(
        record_audit_event,
        account_id
    )

    return {
        "message": "Account created",
        "account_id": account_id,
        "time": datetime.now()
    }

"""
 X-API-KEY
"""
from fastapi import Depends, Header, HTTPException
from app.api.deps import get_api_key
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)

def validate_api_key(
    x_api_key: str = Header(alias="X-API-Key"),
    api_key: str = Depends(get_api_key)
):
    if x_api_key != api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

@router.get(
    "/accounts_with_api_key/{account_id}",
    dependencies=[Depends(validate_api_key)]
)
async def get_account(account_id: str):
    return {"account_id": account_id}




# # Query parameter
# @router.get("/")
# def get_account_details(account_id: str | None = None):
#     if account_id:
#         return {
#             "account_id": account_id,
#             "customer_id": 2,
#             "balance": 500.0
#         }
#     else:
#         return {}

# # Query with multiple parameters
# @router.get("/")
# def get_account_details(account_id: str | None = None, customer_id: str | None = None):
#     if account_id:
#         return {
#             "account_id": account_id,
#             "customer_id": customer_id,
#             "balance": 500.0
#         }
#     else:
#         return {}

# # Simple path parameter
# @router.get("/{account_id}")
# def get_account_details(account_id: int):
#     # Look up
#     return {
#         "account_id": account_id,
#         "balance": 500.0
#     }
