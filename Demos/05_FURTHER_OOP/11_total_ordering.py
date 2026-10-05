from functools import total_ordering

# @total_ordering
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance == other.balance

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __le__(self, other): # needed
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance <= other.balance   
    

    def __str__(self):
        return f"{self.owner}: £{self.balance}"

# --- Usage ---
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)
acc3 = BankAccount("Charlie", 1000)

print(acc1 > acc2)    # True
print(acc1 == acc3)   # True
print(acc2 <= acc1)   # True

# Sorting accounts
accounts = [acc1, acc2, acc3]
for acc in sorted(accounts):
    print(acc)