import json
from datetime import datetime
from decimal import Decimal

class BankingJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return {"__type__": "Decimal", "value": str(obj)}
        if isinstance(obj, datetime):
            return {"__type__": "datetime", "value": obj.isoformat()}
        raise TypeError(f"Type {type(obj)} not serializable")
