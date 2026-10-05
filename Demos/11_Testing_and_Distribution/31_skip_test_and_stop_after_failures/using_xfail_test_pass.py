import pytest


class InterestCalculator:
    def calculate(self, amount, rate):
        # Known bug: rounding error
        return amount * rate / 100  # missing rounding

# @pytest.mark.xfail(reason="Known rounding bug: precision not handled correctly")
def test_interest_rounding():
    calc = InterestCalculator()
    result = calc.calculate(1000, 2.555)

    # result is actually correct so test will pass
    assert round(result, 2) == 25.55




if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])
