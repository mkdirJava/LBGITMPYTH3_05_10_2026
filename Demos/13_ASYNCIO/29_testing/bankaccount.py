import asyncio
import random

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = asyncio.Lock()

    async def withdraw(self, amount):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        if amount > self.balance:
            raise ValueError(f"{self.name}: Insufficient funds")
        self.balance -= amount

    async def deposit(self, amount):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        self.balance += amount

async def transfer(from_acc, to_acc, amount):
    # Always acquire locks in a consistent order to prevent deadlocks
    first, second = sorted([from_acc, to_acc], key=lambda a: a.name)
    async with first.lock:
        async with second.lock:
            await from_acc.withdraw(amount)
            await to_acc.deposit(amount)
            print(f"{amount} transferred from {from_acc.name} to {to_acc.name}")

