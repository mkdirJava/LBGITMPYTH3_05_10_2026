from datetime import datetime
from decimal import Decimal

def banking_json_handler(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # or str(obj) for exact precision
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
