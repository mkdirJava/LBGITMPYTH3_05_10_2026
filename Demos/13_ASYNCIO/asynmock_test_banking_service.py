import pytest
from unittest.mock import AsyncMock
from asyncmock_banking_service import BankService


#@pytest.mark.asyncio
async def test_successful_transfer():
    # Create async mock
    mock_gateway = AsyncMock()

    # Configure return value of async method
    mock_gateway.process_payment.return_value = {
        "status": "success",
        "transaction_id": "tx123"
    }

    service = BankService(mock_gateway)

    result = await service.transfer("Alice", "Bob", 100)

    # Assertions
    assert result["status"] == "success"
    assert result["transaction_id"] == "tx123"

    # Verify async call was made correctly
    mock_gateway.process_payment.assert_awaited_once_with(
        "Alice", "Bob", 100
    )

#@pytest.mark.asyncio
async def test_failed_transfer():
    mock_gateway = AsyncMock()

    mock_gateway.process_payment.return_value = {
        "status": "failed"
    }

    service = BankService(mock_gateway)

    with pytest.raises(RuntimeError):
        await service.transfer("Alice", "Bob", 100)


#@pytest.mark.asyncio
async def test_invalid_amount():
    mock_gateway = AsyncMock()
    service = BankService(mock_gateway)

    with pytest.raises(ValueError):
        await service.transfer("Alice", "Bob", -50)

    # Ensure external service was NOT called
    mock_gateway.process_payment.assert_not_awaited()