import pytest
import bank_utils
from bank_utils import process_payment

@pytest.fixture
def mock_payment(monkeypatch):
    def _mock(status):
        def fake(account_id, amount):
            return {"status": status}
        monkeypatch.setattr(
            bank_utils,
            "send_payment_to_bank_api",
            fake
        )
    return _mock

def test_process_payment_success(mock_payment):
    mock_payment("SUCCESS")
    result = process_payment("ACC1001", 100)
    assert result == "Payment processed"

def test_process_payment_failure(mock_payment):
    mock_payment("FAILED")
    with pytest.raises(RuntimeError):
        process_payment("ACC1001", 100)



if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])