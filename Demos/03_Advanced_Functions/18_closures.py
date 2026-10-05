def make_interest_calculator(rate):
    """Creates a function that applies a fixed interest rate."""
    def apply_interest(balance):
        """Apply the captured interest rate to a balance."""
        return balance + (balance * rate)

    return apply_interest  # This inner function closes over 'rate'


# Create two different calculators with different interest rates
savings_interest = make_interest_calculator(0.03)  # 3%
loan_interest = make_interest_calculator(0.07)  # 7%

# Use them
print(savings_interest(1000))  # 1030.0
print(loan_interest(1000))  # 1070.0

