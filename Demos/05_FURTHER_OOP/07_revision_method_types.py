class BankAccount:
    bank_name = "Global Bank"
    total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    # Instance method: works with a specific account
    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            return f"{self.owner} new balance: {self.balance}"

    # Class method: works with class-level data
    @classmethod
    def get_total_accounts(cls):
        return f"Total accounts in {cls.bank_name}: {cls.total_accounts}"

    # Static method: utility logic related to accounts
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


# --- Usage ---
acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 50)

# Instance method
print(acc1.deposit(50))  # uses that account's balance

# Class method
print(BankAccount.get_total_accounts())  # uses shared class data

# Static method
print(BankAccount.is_valid_amount(25))  # simple utility check


print(type(acc1.__init__))
#<class 'method'>

print(type(acc1.deposit))
#<class 'method'>

print(type(acc1.get_total_accounts))
#<class 'method'>

print(type(acc1.is_valid_amount))
#<class 'function'>
