import uvicorn
from __future__ import annotations

from pathlib import Path
from typing import Any

import polars as pl
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "bank_transactions_synthetic.csv"
VALID_TRANSACTION_TYPES = {"deposit", "withdrawal"}
MISSING_ACCOUNT_VALUES = {"", "nan", "none", "null"}

app = FastAPI(title="Transaction Query Service", version="1.0.0")


def build_json_response(
    status_code: int,
    payload: dict[str, Any],
) -> JSONResponse:
    """Return a JSON response with a mirrored status code in the body."""
    body = {"status_code": status_code, **payload}
    return JSONResponse(status_code=status_code, content=body)


def clean_account_number(value: Any) -> str | None:
    """Normalise a raw account number value to an 8-digit string.

    Blank-like values such as empty strings, ``NaN``, ``null``, and ``None``
    are treated as missing.
    """
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
    """Normalise and validate the transaction type."""
    if value is None:
        return None

    cleaned = str(value).strip().lower()
    if cleaned in VALID_TRANSACTION_TYPES:
        return cleaned

    return None


def load_transactions(data_file: Path = DATA_FILE) -> pl.DataFrame:
    """Load the CSV and clean it before any filtering takes place."""
    dataframe = pl.read_csv(data_file)

    return dataframe.with_columns(
        [
            pl.col("account_number")
            .map_elements(clean_account_number, return_dtype=pl.String)
            .alias("account_number"),
            pl.col("transaction_type")
            .map_elements(clean_transaction_type, return_dtype=pl.String)
            .alias("transaction_type"),
            pl.col("amount_gbp").cast(pl.Float64).round(2).alias("amount_gbp"),
        ]
    )


TRANSACTIONS_DF = load_transactions()


def query_transactions(
    account_number: str,
    transaction_type: str | None = None,
) -> list[dict[str, Any]]:
    """Query cleaned transactions using Polars expressions."""
    filter_expression = pl.col("account_number") == account_number

    if transaction_type is not None:
        filter_expression = filter_expression & (
            pl.col("transaction_type") == transaction_type
        )

    return (
        TRANSACTIONS_DF.filter(
            pl.col("account_number").is_not_null()
            & pl.col("transaction_type").is_not_null()
            & filter_expression
        )
        .sort(["transaction_date", "transaction_time", "transaction_id"])
        .to_dicts()
    )


@app.get("/health")
def health() -> JSONResponse:
    """Return the health status for the service."""
    return build_json_response(200, {"status": "ok"})


@app.get("/transactions")
def get_transactions(
    account_number: str = Query(
        ...,
        description="8-digit bank account number",
    ),
) -> JSONResponse:
    """Return all transactions for a cleaned account number."""
    cleaned_account_number = clean_account_number(account_number)
    if cleaned_account_number is None:
        return build_json_response(
            400,
            {"error": "account_number must be an 8-digit numeric string"},
        )

    transactions = query_transactions(account_number=cleaned_account_number)
    if not transactions:
        return build_json_response(
            404,
            {
                "error": "No transactions found for the supplied account_number",
                "account_number": cleaned_account_number,
            },
        )

    return build_json_response(
        200,
        {
            "account_number": cleaned_account_number,
            "count": len(transactions),
            "transactions": transactions,
        },
    )


@app.get("/transactions/filter")
def get_transactions_by_type(
    account_number: str = Query(
        ...,
        description="8-digit bank account number",
    ),
    transaction_type: str = Query(
        ...,
        description="Transaction type: deposit or withdrawal",
    ),
) -> JSONResponse:
    """Return transactions for an account number filtered by type."""
    cleaned_account_number = clean_account_number(account_number)
    if cleaned_account_number is None:
        return build_json_response(
            400,
            {"error": "account_number must be an 8-digit numeric string"},
        )

    cleaned_transaction_type = clean_transaction_type(transaction_type)
    if cleaned_transaction_type is None:
        return build_json_response(
            400,
            {"error": "transaction_type must be 'deposit' or 'withdrawal'"},
        )

    transactions = query_transactions(
        account_number=cleaned_account_number,
        transaction_type=cleaned_transaction_type,
    )
    if not transactions:
        return build_json_response(
            404,
            {
                "error": (
                    "No transactions found for the supplied account_number "
                    "and transaction_type"
                ),
                "account_number": cleaned_account_number,
                "transaction_type": cleaned_transaction_type,
            },
        )

    return build_json_response(
        200,
        {
            "account_number": cleaned_account_number,
            "transaction_type": cleaned_transaction_type,
            "count": len(transactions),
            "transactions": transactions,
        },
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)