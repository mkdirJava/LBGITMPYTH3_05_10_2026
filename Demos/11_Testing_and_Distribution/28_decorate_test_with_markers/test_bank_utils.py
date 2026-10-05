import pytest
from bank_utils import transfer_funds

@pytest.mark.fast
def test_small_transfer():
    assert transfer_funds(1000, 100) == 900

@pytest.mark.slow
def test_large_transfer():
    # Simulate something "heavier" conceptually
    assert transfer_funds(1000000, 500000) == 500000

@pytest.mark.error
def test_transfer_insufficient_funds():
    with pytest.raises(ValueError):
        transfer_funds(100, 200)

@pytest.mark.error
def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer_funds(100, -10)