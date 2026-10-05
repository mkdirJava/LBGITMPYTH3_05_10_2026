from app.core.config import DATA_FILE
from app.services.transaction_service import query_transactions

# ✅ Config dependency
def get_data_file():
    return DATA_FILE

# ✅ Service dependency
def get_transaction_service():
    return query_transactions
