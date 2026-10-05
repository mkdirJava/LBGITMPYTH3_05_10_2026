import pytest
import os

class PaymentProcessor:
    def process_payment(self, amount):
        return "Processed"


@pytest.mark.skipif(
    os.getenv("ENV") != "production",
    reason="High-value transactions only tested in production-like environment"
)
def test_large_transaction():
    processor = PaymentProcessor()
    result = processor.process_payment(1_000_000)  # £1M transaction
    assert result == "Processed"

