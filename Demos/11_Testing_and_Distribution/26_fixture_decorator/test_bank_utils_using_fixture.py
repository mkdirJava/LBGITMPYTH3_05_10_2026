import pytest
import bank_utils
from bank_utils import process_payment

@pytest.fixture()
def mock_successful_payment(monkeypatch):
    def mock_send_payment(account_id, amount):
        return {"status": "SUCCESS"}

    monkeypatch.setattr(
        bank_utils,
        "send_payment_to_bank_api",
        mock_send_payment
    )
    return mock_send_payment

def test_process_payment_success(mock_successful_payment):
    result = process_payment("ACC1001", 100)
    assert result == "Payment processed"

@pytest.fixture()
def mock_failed_payment(monkeypatch):
    def mock_send_payment(account_id, amount):
        return {"status": "FAILED"}

    monkeypatch.setattr(
        bank_utils,
        "send_payment_to_bank_api",
        mock_send_payment
    )
    return mock_send_payment

def test_process_payment_failure(mock_failed_payment):
    import pytest

    with pytest.raises(RuntimeError):
        process_payment("ACC1001", 100)



if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])