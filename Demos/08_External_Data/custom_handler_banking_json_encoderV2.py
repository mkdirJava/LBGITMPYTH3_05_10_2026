import json
from datetime import datetime
from decimal import Decimal

class BankingJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # or str(obj) for full precision
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)