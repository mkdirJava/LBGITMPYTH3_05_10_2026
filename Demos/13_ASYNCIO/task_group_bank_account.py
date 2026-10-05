import asyncio


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self._lock = asyncio.Lock()  # prevent race conditions

    async def deposit(self, amount):
        async with self._lock:
            await asyncio.sleep(0.1)  # simulate I/O
            self.balance += amount
            print(f"{self.name}: Deposited {amount}, new balance = {self.balance}")

    async def withdraw(self, amount):
        async with self._lock:
            await asyncio.sleep(0.1)
            if amount > self.balance:
                raise ValueError(f"{self.name}: Insufficient funds")
            self.balance -= amount
            print(f"{self.name}: Withdrew {amount}, new balance = {self.balance}")


async def transfer(from_account, to_account, amount):
    await from_account.withdraw(amount)
    await to_account.deposit(amount)
    print(f"Transfer {amount} from {from_account.name} → {to_account.name}")