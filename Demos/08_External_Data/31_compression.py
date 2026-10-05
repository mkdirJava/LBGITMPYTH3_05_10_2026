import gzip
import json
import os

class Account:
    def __init__(self, account_id, name, balance, overdraft_limit):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"{self.account_id} | {self.name} | £{self.balance} | £{self.overdraft_limit}"

accounts = [
    Account(45678, "Kamran Liaqat", 2540.75, 500.00),
    Account(45679, "Sadia Saleem", 342.76, 600.00)
]

# Create a dictionary of accounts
accounts_dict = {
    account.account_id: {
        "name": account.name,
        "balance": account.balance,
        "overdraft_limit": account.overdraft_limit
    }
    for account in accounts
}

# Set the compressed archive filename
arc_filename = 'accounts_dictionary.gz'
arc_file = gzip.open(arc_filename, 'wb')
try:

    # Convert dict to bytes
    dict_bytes = json.dumps(accounts_dict).encode("utf-8")
    # Zip this content...
    arc_file.write(dict_bytes)
finally:
    arc_file.close()
    print(f"{arc_filename} contains ", end="")
    print(f"{os.stat(arc_filename).st_size} compressed bytes")


# And in reverse...

# Read and decompress the archive
arc_filename = "accounts_dictionary.gz"

with gzip.open(arc_filename, "rb") as arc_file:
    compressed_data = arc_file.read()

# Convert bytes back to a dictionary
accounts_dict = json.loads(compressed_data.decode("utf-8"))

print("Dictionary loaded from archive:")
print(accounts_dict)

# Recreate Account objects
accounts2 = [
    Account(
        int(account_id),
        details["name"],
        details["balance"],
        details["overdraft_limit"]
    )
    for account_id, details in accounts_dict.items()
]

print("\nReconstructed Account objects:")
for account in accounts2:
    print(account)
