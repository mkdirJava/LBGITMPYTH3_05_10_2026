from pydantic import BaseModel, Field

class AccountCreate(BaseModel):
    customer_id: int
    balance: float = Field(gt=0)

class AccountOut(AccountCreate):
    account_id: int


