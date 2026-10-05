import json
from datetime import datetime
from decimal import Decimal
from custom_handler_banking_json_encoderV2 import BankingJSONEncoder

transaction = {
    "account_id": "ACC123",
    "amount": Decimal("1025.75"),
    "currency": "GBP",
    "timestamp": datetime.now()
}

json_data = json.dumps(transaction, cls=BankingJSONEncoder)
print(json_data)
