# decorators can help you add cross‑cutting concerns—like audit logging,
# retries, access control, caching, metrics, and validation
# without cluttering core business logic (pricing, orders, risk).
#
# Audit Logging Decorator (OMS / Trade Processing)
# Goal: Every order/trade action should emit a consistent audit record for compliance.
# Why this helps: You get consistent, tamper‑resistant audit trails without repeating logging code.
import functools
import json
from datetime import datetime,UTC

def audit_log(action_name: str):
    """Decorator that logs inputs/outputs with a consistent schema."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            ts = datetime.now(UTC).isoformat() + "Z"
            result = fn(*args, **kwargs)
            record = {
                "ts": ts,
                "action": action_name,
                "args": args,
                "kwargs": kwargs,
                "result": result,
            }
            # In production: send to Kafka / SIEM / file / db
            print("[AUDIT]", json.dumps(record, default=str))
            return result
        return wrapper
    return decorator

# --- Usage: decorate core business functions ---
@audit_log("NEW_ORDER")
def create_order(symbol: str, qty: int, price: float, trader_id: str):
    # business logic goes here (persist, route, etc.)
    return {"order_id": "O123", "status": "accepted"}

@audit_log("CANCEL_ORDER")
def cancel_order(order_id: str, trader_id: str):
    # business logic...
    return {"order_id": order_id, "status": "cancelled"}

create_order("AAPL", 1000, 175.5, trader_id="alice")
cancel_order("O123", trader_id="alice")


# Retry with Exponential Backoff (Market Data / Pricing APIs)
# Goal: Market data calls can fail transiently. Add robust retries around I/O functions.
# This is useful because Decorators make the resilience policy (retries/backoff) reusable
# and consistent across all external calls (pricing, FIX gateways, brokers).
import time
import functools
from random import random

def retry(exceptions, tries=3, base_delay=0.2, factor=2.0):
    """Retry on given exceptions with exponential backoff."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            attempt, delay = 0, base_delay
            while True:
                try:
                    return fn(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= tries:
                        raise
                    time.sleep(delay)
                    delay *= factor
        return wrapper
    return decorator

@retry((ConnectionError, TimeoutError), tries=5, base_delay=0.1, factor=1.8)
def get_quote(symbol: str) -> float:
    # Simulated flaky quote source
    print("attempt")
    if random() < 0.1:
        print("error")
        raise ConnectionError("Transient feed error")
    return 100.0 + random()

price = get_quote("MSFT")
print(price)



# Pie Syntax Decorator:
def limit_withdrawals(func):
    """Decorator enforcing a max withdrawal amount per transaction."""
    def wrapper(balance, amount):
        if amount > 300:
            pass
            #raise ValueError("Withdrawal exceeds daily limit of £300.")
        print(f"[SECURITY] Withdrawal validated: £{amount}")
        return func(balance, amount)
    return wrapper

@limit_withdrawals   # ← pie syntax decorating the function
def withdraw(balance, amount):
    return balance - amount

# Use it
balance = 500
balance = withdraw(balance, 100)
print("New balance:", balance)

balance = withdraw(balance, 400)
print("New balance:", balance)




def transaction_logger(label):  # 1. Outer: Catch the parameter
    def decorator(func):       # 2. Middle: Catch the function
        def wrapper(self, amount):
            print(f"[LOG] Starting {label} for {self.owner}...")
            result = func(self, amount)
            print(f"[LOG] {label} finished. Balance: ${self.balance}")
            return result
        return wrapper
    return decorator

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @transaction_logger("DEPOSIT") # Parameter "DEPOSIT" passed here
    def deposit(self, amount):
        self.balance += amount

    @transaction_logger("WITHDRAW") # Parameter "DEPOSIT" passed here
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("Ted", 1000)
account.deposit(100)
account.withdraw(100)

from functools import wraps

def security_audit(func):
    @wraps(func)  # Copies name and docstring
    def wrapper(self, *args, **kwargs):
        """Internal audit wrapper logic."""
        print(f"Securing {func.__name__}...")
        return func(self, *args, **kwargs)
    return wrapper

class BankAccount:
    @security_audit
    def deposit(self, amount):
        """increases funds after identity verification."""
        self.balance += amount

# Without @wraps: account.deposit.__name__ would be "wrapper"
# With @wraps:    account.deposit.__name__ is "deposit"
print(f"Function Name: {BankAccount.deposit.__name__}")
print(f"Docstring: {BankAccount.deposit.__doc__}")