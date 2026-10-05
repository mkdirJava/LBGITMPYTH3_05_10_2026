def open_account(name, initial_deposit, **options):
    print(f"Opening account for {name}")
    print(f"Initial deposit: £{initial_deposit}")

    # kwargs let you handle optional settings
    for key, value in options.items():
        print(f"{key}: {value}")

# Example usage
open_account(
    "Alice",
    500,
    account_type="Savings",
    overdraft_limit=1000,
    notifications=True
)

args_as_dict = { "account_type":"Mortgage", "type":"2 year Fixed_Rate", "notifications":True }
open_account("Kamran",50000, **args_as_dict)