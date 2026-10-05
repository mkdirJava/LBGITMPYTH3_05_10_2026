from pydantic import BaseModel, Field

class Account(BaseModel):
    account_id: int
    customer_id: int
    balance: float = Field(gt=0)
