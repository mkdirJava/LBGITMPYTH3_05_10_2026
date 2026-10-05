from fastapi import APIRouter
from fastapi import HTTPException
router = APIRouter(prefix="/accounts", tags=["Accounts"])

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

# MULTIPLE PATH PARAMETERS
from app.services.account_service import get_account as ga
@router.get("/customers/{customer_id}/accounts/{account_id}")
def get_customer_account_details(customer_id: int, account_id: int):
    return ga(customer_id, account_id)



from fastapi import HTTPException
# Pretend this is data from a database
accounts = {
    1001: {"account_name": "Current Account", "balance": 1250.50},
    1002: {"account_name": "Savings Account", "balance": 5000.00},
}

@router.get("/{account_id}")
def get_account(account_id: int):
    account = accounts.get(account_id)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail=f"Account {account_id} not found"
        )

    return account