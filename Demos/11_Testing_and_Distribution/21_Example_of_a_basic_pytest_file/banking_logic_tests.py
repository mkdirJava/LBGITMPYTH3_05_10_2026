import pytest
from banking_logic import deposit, withdraw

def setup_function():
    """Executed before each test."""
    pass

def test_simple_scalar():
    y = 'world';
    fred = str.upper(f"fred's {y}")
    assert fred == "FRED'S WORLD"

def test_attribute():
    fred = "fred"
    assert hasattr(fred, 'upper')

@pytest.mark.deposit
def test_deposit_increases_balance():
    result = deposit(100, 50)
    assert result == 150

@pytest.mark.deposit
def test_deposit_negative_amount_raises_error():
    with pytest.raises(ValueError):
        deposit(100, -10)

def test_withdraw_reduces_balance():
    result = withdraw(100, 40)
    assert result == 60

def test_withdraw_too_much_raises_error():
    with pytest.raises(ValueError):
        withdraw(100, 200)

def test_withdraw_negative_amount_raises_error():
    with pytest.raises(ValueError):
        withdraw(100, -5)

def teardown_function():
    """Executed after each test."""
    pass
