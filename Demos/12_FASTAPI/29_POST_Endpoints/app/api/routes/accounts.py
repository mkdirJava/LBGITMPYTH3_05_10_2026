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


@router.post("/", response_model=AccountOut, status_code=201)
def create_account(account: AccountCreate):
    # model_dump() converts a Pydantic model into a standard Python dictionary by:
    # - Taking all fields from account
    # - Adding a  new field: "account_id": 1
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
