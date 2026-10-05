from fastapi import FastAPI
from app.api.routes import accounts, payments

app = FastAPI(title="Banking API Demo")

app.include_router(accounts.router)
app.include_router(payments.router)


