from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/admin", tags=["Admin"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/admin/customers")
async def customer_dashboard(request: Request):
    customers = [
        {"id": "C1234", "name": "Sadia Liaqat", "risk": "Low"},
        {"id": "C5678", "name": "Kamran Saleem", "risk": "High"},
    ]

    return templates.TemplateResponse(
        request=request,
        name="admin/customers.html",
        context={"customers": customers}
    )