import struct

# Define the Account class (same as before)
class Account:
    def __init__(self, account_id, name, balance, overdraft_limit):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"{self.account_id} | {self.name} | £{self.balance} | £{self.overdraft_limit}"


FORMAT = "i50sff"

accounts_loaded = []

# Open the binary file for reading
with open("accounts.dat", "rb") as f:
    record_size = struct.calcsize(FORMAT) # records are fixed in size

    while True:
        chunk = f.read(record_size)
        if not chunk:
            break

        # Unpack the binary data converting bytes to Python values
        account_id, name_bytes, balance, overdraft = struct.unpack(FORMAT, chunk)

        # Decode and clean up the name
        name = name_bytes.decode("utf-8").rstrip("\x00")

        # Create Account object and add to list
        account = Account(account_id, name, balance, overdraft)
        accounts_loaded.append(account)

# Display loaded accounts
for acc in accounts_loaded:
    print(acc)