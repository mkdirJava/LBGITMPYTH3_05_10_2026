class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def print_statement(self):
        print(f"Account Holder : {self.name}")
        print(f"Balance        : £{self.balance:.2f}")


def run_scenario():
    acc = Account("Alice", 100.00)

    acc.deposit(50)
    acc.withdraw(26)

    acc.print_statement()

if __name__ == "__main__":
    run_scenario()