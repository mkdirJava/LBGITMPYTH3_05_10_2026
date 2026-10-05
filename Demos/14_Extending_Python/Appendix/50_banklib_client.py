from ctypes import *

# Load the DLL (Windows example)
banklib = cdll.LoadLibrary(r".\banklib.dll")

# Define argument and return types (IMPORTANT for correctness)
banklib.calculate_interest.argtypes = [c_double, c_double, c_int]
banklib.calculate_interest.restype = c_double

banklib.print_account_summary.argtypes = [c_double]
banklib.print_account_summary.restype = None

# Simulated bank account data
balance = 1000.0     # £1000
rate = 0.05          # 5% interest
years = 3

# Call the C function
interest = banklib.calculate_interest(balance, rate, years)

# Print result in Python
print(f"Interest earned: £{interest:.2f}")

# Call C function that prints directly
banklib.print_account_summary(balance + interest)