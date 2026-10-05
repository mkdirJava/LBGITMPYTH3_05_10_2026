import json
from datetime import datetime
from decimal import Decimal
from custom_handler_banking_json_encoderV1 import banking_json_handler

transaction = {
    "account_id": "ACC123",
    "amount": Decimal("1025.75"),
    "currency": "GBP",
    "timestamp": datetime.now()
}

#json_data = json.dumps(transaction) # triggers TypeError: Object of type Decimal is not JSON serializable
json_data = json.dumps(transaction, default=banking_json_handler)
print(json_data)
