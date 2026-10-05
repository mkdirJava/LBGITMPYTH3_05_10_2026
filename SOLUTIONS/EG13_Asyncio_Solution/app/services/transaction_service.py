from pathlib import Path
from typing import Any
import polars as pl

from app.core.config import DATA_FILE
from app.utils.cleaners import clean_account_number, clean_transaction_type

def load_transactions(data_file: Path = DATA_FILE) -> pl.DataFrame:
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
    import polars as pl

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