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

# --- Demonstrate closure attributes ---
print("Closure function __name__ :", savings_interest.__name__)
print("Closure function __doc__ :", savings_interest.__doc__)

# Show what was captured in the closure
cells = savings_interest.__closure__
print("Has closure? :", cells is not None)
if cells:
    # There may be multiple cells; here we expect one (the 'rate')
    print("Captured value(s) :", [cell.cell_contents for cell in cells])

# Also show the outer factory’s attributes for contrast
print("Factory __name__ :", make_interest_calculator.__name__)
print("Factory __doc__ :", make_interest_calculator.__doc__)
