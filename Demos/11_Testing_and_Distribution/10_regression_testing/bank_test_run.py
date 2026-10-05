import sys
from bank import run_scenario

with open("bank.out", "w") as f:
    original_stdout = sys.stdout
    sys.stdout = f

    run_scenario()

    sys.stdout = original_stdout

print("Test output created.")