from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "bank_transactions_synthetic.csv"

VALID_TRANSACTION_TYPES = {"deposit", "withdrawal"}
MISSING_ACCOUNT_VALUES = {"", "nan", "none", "null"}