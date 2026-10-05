def outer_func():
    num = 56

    def inner_func():
        print(num, "in inner func")

    inner_func()
    print(num, "in outer func")


outer_func()
inner_func()

# ETL: Trade Ingestion with Local Helpers (Encapsulation)
# Use nested functions to keep ETL helpers scoped to the pipeline step.
# This keeps the global namespace clean and makes the code easier to reason about.
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List, Dict, Any

@dataclass
class Trade:
    trade_id: str
    symbol: str
    qty: int
    price: float
    currency: str
    timestamp: datetime

def ingest_trades(raw_rows: Iterable[Dict[str, Any]]) -> List[Trade]:
    """Extract + Transform with nested helpers to validate & normalize."""

    def _parse_row(row: Dict[str, Any]) -> Trade:
        # --- nested function only used inside ingest_trades ---
        return Trade(
            trade_id=str(row["trade_id"]).strip(),
            symbol=str(row["symbol"]).upper().strip(),
            qty=int(row["qty"]),
            price=float(row["price"]),
            currency=str(row.get("currency", "USD")).upper(),
            timestamp=_parse_ts(row.get("timestamp")),
        )

    def _parse_ts(value) -> datetime:
        # --- only needed for this ingestion path ---
        if isinstance(value, datetime):
            return value
        return datetime.fromisoformat(value)

    def _validate(trade: Trade) -> None:
        # --- localized validation logic ---
        if trade.qty <= 0:
            raise ValueError(f"Qty must be positive: {trade}")
        if trade.price <= 0:
            raise ValueError(f"Price must be positive: {trade}")
        if trade.currency not in {"USD", "GBP", "EUR"}:
            raise ValueError(f"Unsupported currency: {trade.currency}")

    trades: List[Trade] = []
    for r in raw_rows:
        t = _parse_row(r)
        _validate(t)
        trades.append(t)
    return trades

# --- Usage ---
raw = [
    {"trade_id": "T1", "symbol": "Aapl", "qty": 100, "price": 175.5, "currency": "usd", "timestamp": "2024-01-15T10:00:00"},
    {"trade_id": "T2", "symbol": "MSFT", "qty": 50, "price": 311.2, "currency": "USD", "timestamp": "2024-01-15T10:01:00"},
]
clean = ingest_trades(raw)
print(clean)