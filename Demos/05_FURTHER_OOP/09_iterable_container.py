class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_transaction(self, amount):
        self.transactions.append(amount)

    # Make the account iterable
    def __iter__(self):
        return TransactionIterator(self.transactions)

class TransactionIterator:
    def __init__(self, transactions):
        self._transactions = transactions
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._transactions):
            raise StopIteration
        value = self._transactions[self._index]
        self._index += 1
        return value


# --- Usage ---
account = BankAccount("Alice")
account.add_transaction(100)
account.add_transaction(-20)
account.add_transaction(50)

for t in account:
    print(t)

account = BankAccount("Bob")
account.add_transaction(70)
account.add_transaction(80)
account.add_transaction(90)
account_iter = iter(account)
print(next(account_iter))
print(next(account_iter))
print(next(account_iter))
print(next(account_iter)) #this will raise an exception; object is exhausted
