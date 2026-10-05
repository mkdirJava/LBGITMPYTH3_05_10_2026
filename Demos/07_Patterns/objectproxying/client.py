from bankaccount import BankAccount
from bankaccountproxy import BankAccountProxy
from account import Account

def handle_request(account: Account, amount: int) -> None:
    account.withdraw(amount)

account = BankAccount("Peter", 1500)
proxy = BankAccountProxy(account)

print(proxy.get_owner())    # delegated
proxy.deposit(500)          # delegated
proxy.withdraw(200)         # handled normally
proxy.withdraw(2000)        # intercepted by proxy

proxy.change_owner("Ted")     # would be delegated but 'owner' has already been resolved
proxy.deposit(500)          # would be delegated but 'balance' has already been resolved

handle_request(account, 3000)
handle_request(proxy, 4000)
