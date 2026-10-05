import pytest
from unittest.mock import AsyncMock
from bank_service__asyncio_pytest_fixtures import BankService


# ✅ async fixture
@pytest.fixture
async def fraud_checker():
    mock = AsyncMock()
    mock.check.return_value = True
    return mock


# ✅ test using the fixture
# @pytest.mark.asyncio
async def test_successful_transfer(fraud_checker):
    service = BankService(fraud_checker)

    result = await service.transfer("Alice", "Bob", 100)

    assert result["status"] == "success"
    fraud_checker.check.assert_awaited_once_with("Alice", "Bob", 100)


# ✅ failure case
# @pytest.mark.asyncio
async def test_fraud_detected(fraud_checker):
    fraud_checker.check.return_value = False

    service = BankService(fraud_checker)

    with pytest.raises(ValueError):
        await service.transfer("Alice", "Bob", 100)