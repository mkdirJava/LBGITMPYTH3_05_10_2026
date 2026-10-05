from abc import ABC, abstractmethod

class Account(ABC):
    def deposit(self, amount: int) -> None:
        self.balance += amount
        self.owner = "Anon"
        print(f"Deposited £{amount}. New balance = £{self.balance}")

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        pass

    def get_owner(self) -> str:
        return self.owner

    def change_owner(self, value: str) -> None:
        self.owner = value
        print(f"New owner {value}")