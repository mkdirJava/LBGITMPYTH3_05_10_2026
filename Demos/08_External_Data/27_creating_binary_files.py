import struct

# Define the Account class
class Account:
    def __init__(self, account_id, name, balance, overdraft_limit):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.overdraft_limit = overdraft_limit

# Create account instances
accounts = [
    Account(45678, "Kamran Liaqat", 2540.75, 500.00),
    Account(45679, "Sadia Saleem", 342.76, 600.00)
]

# Define binary format:
# i = int (account_id)
# 50s = fixed-length string (name, 50 bytes)
# f = float (balance)
# f = float (overdraft_limit)
FORMAT = "i50sff"

# Write to binary file
with open("accounts.dat", "wb") as f:
    for acc in accounts:
        # Encode name to bytes and pad/truncate to 50 bytes
        name_bytes = acc.name.encode("utf-8")
        name_bytes = name_bytes[:50].ljust(50, b"\x00")

        packed_data = struct.pack(
            FORMAT,
            acc.account_id,
            name_bytes,
            acc.balance,
            acc.overdraft_limit
        )
        f.write(packed_data)

print("Account objects written to binary file.")