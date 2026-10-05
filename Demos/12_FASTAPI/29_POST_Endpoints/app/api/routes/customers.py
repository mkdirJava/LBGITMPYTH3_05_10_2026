from fastapi import APIRouter
from app.services.customer_service import get_customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/{customer_id}")
def read_customer(customer_id: int):
    return get_customer(customer_id)
