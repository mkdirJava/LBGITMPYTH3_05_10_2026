import pickle

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

# Create the pickle!
pickle_filename = "accounts.pkl"
pickle_file = open(pickle_filename, "wb")
pickle.dump(accounts_dict, pickle_file)
pickle_file.close()

import bz2
# Compress the pickle
small_pickle_file = bz2.BZ2File('smallpickle.bzip', 'w')
pickle.dump(accounts_dict, small_pickle_file )

