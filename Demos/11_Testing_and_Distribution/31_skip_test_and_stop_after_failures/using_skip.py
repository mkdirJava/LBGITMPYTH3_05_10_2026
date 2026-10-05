import pytest
# Skip a test unconditionally (e.g., feature not ready or temporarily disabled)
class LoanService:
    def calculate_interest(self, amount, rate):
        # Feature still under development
        raise NotImplementedError

@pytest.mark.skip(reason="Loan interest calculation not implemented yet")
def test_calculate_interest():
    service = LoanService()
    assert service.calculate_interest(1000, 5) == 50

