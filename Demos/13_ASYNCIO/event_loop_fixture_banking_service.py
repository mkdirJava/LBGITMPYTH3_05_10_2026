import asyncio

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    async def deposit(self, amount):
        await asyncio.sleep(0.1)  # simulate I/O delay
        self.balance += amount
        return self.balance

    async def withdraw(self, amount):
        await asyncio.sleep(0.1) # simulate I/O delay
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

async def transfer(from_account, to_account, amount):
    await from_account.withdraw(amount)
    await to_account.deposit(amount)