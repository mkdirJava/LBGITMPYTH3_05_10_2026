from pydantic import BaseModel

class AccountResponse(BaseModel):
    account_id: str
    balance: float
    currency: str