class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
def process_batch_transactions(acc, transactions):
    # Perf Optimization: "Bind" method to local name
    # Avoid o/h of looking up 'deposit' on 'acc' many times.
    quick_deposit = acc.deposit
    for amount in transactions:
        quick_deposit(amount)  # Faster execution
        #account.deposit(amount)
# Simulating 1 million automated deposits
bulk_data = [10.50] * 1000000
my_account = BankAccount()
process_batch_transactions(my_account, bulk_data)
print(my_account.balance)
