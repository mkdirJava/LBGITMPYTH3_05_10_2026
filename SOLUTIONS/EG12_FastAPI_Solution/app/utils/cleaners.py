from typing import Any
from app.core.config import VALID_TRANSACTION_TYPES, MISSING_ACCOUNT_VALUES

def clean_account_number(value: Any) -> str | None:
    if value is None:
        return None

    cleaned = str(value).strip()
    if not cleaned:
        return None

    if cleaned.lower() in MISSING_ACCOUNT_VALUES:
        return None

    if cleaned.endswith(".0"):
        cleaned = cleaned[:-2]

    if not cleaned.isdigit():
        return None

    if len(cleaned) != 8:
        return None

    return cleaned


def clean_transaction_type(value: Any) -> str | None:
    if value is None:
        return None

    cleaned = str(value).strip().lower()
    if cleaned in VALID_TRANSACTION_TYPES:
        return cleaned

    return None