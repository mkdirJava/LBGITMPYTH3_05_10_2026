import bankmodule
import sys

# Simulated bank account object
account = {"name": "Alice", "balance": 1000}

print("Initial refcount:", sys.getrefcount(account))

# Pass to C extension
result = bankmodule.process_account(account)

print("After function call refcount for account:", sys.getrefcount(account))
print("After function call refcount for result:", sys.getrefcount(result))
# Check returned object identity
print("Same object returned:", result is account)
print(result["name"])
print(result["balance"])

del account
print(result["name"])

