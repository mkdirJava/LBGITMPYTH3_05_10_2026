# run_bank.py
from banking import process_deposit, get_transaction_type

# MonkeyType sees: str, float -> float
print(process_deposit("ACC-123", 250.50))

# MonkeyType sees: int -> str
print(get_transaction_type(1))

# rename 30_monkeytype_example_workflow_1 to start with an alpha character. say "x"
# From terminal window run:
# monkeytype run x30_monkeytype_example_workflow_1.py

# will produce a set of proposed changes to banking.py:
# monkeytype stub banking

# Will apply the changes to the banking.py file:
# monkeytype apply banking
# see 31_monkeytype_example_workflow_2.py for what file will be changed to