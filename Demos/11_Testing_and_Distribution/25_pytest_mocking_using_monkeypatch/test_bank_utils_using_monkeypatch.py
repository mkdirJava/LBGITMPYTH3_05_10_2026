import bank_utils
from bank_utils import process_payment

def test_process_payment_success(monkeypatch):
    #  Mock implementation
    def mock_send_payment(account_id, amount):
        return {"status": "SUCCESS"}

    # Replace the real function
    monkeypatch.setattr(
        bank_utils,
        "send_payment_to_bank_api",
        mock_send_payment
    )

    result = process_payment("ACC1001", 100)

    assert result == "Payment processed"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])