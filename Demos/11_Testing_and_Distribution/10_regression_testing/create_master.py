import sys
from bank import run_scenario

with open("bank.master", "w") as f:
    original_stdout = sys.stdout
    sys.stdout = f

    run_scenario()

    sys.stdout = original_stdout

print("Master file created.")