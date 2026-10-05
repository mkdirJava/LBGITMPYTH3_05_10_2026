from fastapi import APIRouter
from fastapi import HTTPException
from app.services.account_service import get_account
from app.services.notification_service import generate_overdraft_email_text, generate_overdraft_email_html

router = APIRouter(prefix="/accounts", tags=["Accounts"])

# Pretend this is data from a database
accounts = {
    1001: {"account_name": "Current Account", "balance": 1250.50},
    1002: {"account_name": "Savings Account", "balance": 5000.00},
}

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
@router.get("/home")
def render_home(request: Request):
    return templates.TemplateResponse(
        request,
        name="index.html",
        context={
            "title": "Home"
        }
    )

@router.get("/{account_id}/overdraft-email-text")
def overdraft_email(account_id: int):
    email_content = generate_overdraft_email_text(
        customer_name="Ernst Blofeld",
        account_id=account_id,
        balance=-51.47
    )

    return {"email_preview": email_content}

@router.get("/{account_id}/overdraft-email-html")
def overdraft_email(account_id: int):
    email_content = generate_overdraft_email_html(
        customer_name="Ernst Blofeld",
        account_id=account_id,
        balance=-51.47
    )

    return {"email_preview": email_content}

@router.get("/getAccounts")
def getAccounts():
    return "data"

@router.get("/accounts")
def list_accounts():
    return [{"account_id": 1, "balance": 500.0}]

from fastapi.responses import StreamingResponse
import io

def generate_csv():
    buffer = io.StringIO()
    buffer.write("account_id,balance\n1,500.0\n2,234.67\n")
    buffer.seek(0)
    return buffer

@router.get("/export")
def export_accounts():
    return StreamingResponse(
        generate_csv(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=accounts.csv"}
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

