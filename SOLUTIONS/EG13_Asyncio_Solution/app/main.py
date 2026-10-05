from fastapi import FastAPI
from routes import transactions

app = FastAPI(title="Transaction Query Service", version="1.0.0")

app.include_router(transactions.router)
