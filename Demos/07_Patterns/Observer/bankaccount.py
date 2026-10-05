class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self._observers = [] # AKA subscribers

    def attach(self, observer): # AKA subscribe
        self._observers.append(observer)

    def detach(self, observer): # AKA unsubscribe
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited £{amount}. New balance = £{self.balance}")
        self.notify()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance = £{self.balance}")
            self.notify()