from inspect import Signature, Parameter


class BankAccount:
    # Define allowed fields as a "schema"
    __signature__ = Signature([
        Parameter("owner", Parameter.POSITIONAL_OR_KEYWORD),
        Parameter("balance", Parameter.POSITIONAL_OR_KEYWORD),
        Parameter("overdraft_limit", Parameter.POSITIONAL_OR_KEYWORD, default=None),
       ])

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


def apply_updates(obj, updates: dict, signature: Signature):
    allowed_fields = signature.parameters

    for key, value in updates.items():
        if key in allowed_fields:
            current_value = getattr(obj, key, None)
            print(f"Updating '{key}': {current_value} -> {value}")
            setattr(obj, key, value)
        else:
            print(f"Ignoring unknown field: {key}")


# --- Usage ---
account = BankAccount("Alice", 1000)

updates = {
    "balance": 1500,
    "overdraft_limit": 200,
    "unknown_field": "ignored"
}

apply_updates(account, updates, BankAccount.__signature__)

# Inspect known attributes via signature
for name in BankAccount.__signature__.parameters:
    value = getattr(account, name, None)
    print(f"{name}: {value}")