# Example 1 — Using Counter to Aggregate Trade Volumes by Symbol
# In trading desks and reporting pipelines, you often need to
# aggregate trade counts or volumes across symbols, currencies, or venues.
# Counter makes this trivial and extremely fast
# .
# Scenario:
# You receive a stream of executed trades and want to know total traded
# volume per symbol for intraday risk or TCA (Transaction Cost Analysis).

# Why Counter is useful in FS
# - Perfect for market surveillance (detecting abnormal volume)
# - Used in intraday risk dashboards
# - Helpful in TCA analytics
# - Avoids manual dict boilerplate
from collections import Counter

trades = [
    {"symbol": "AAPL", "qty": 100},
    {"symbol": "MSFT", "qty": 50},
    {"symbol": "AAPL", "qty": 200},
    {"symbol": "GOOG", "qty": 10},
    {"symbol": "MSFT", "qty": 25},
]

volumes = Counter()

for t in trades:
    volumes[t["symbol"]] += t["qty"]

print(volumes) # Counter({'AAPL': 300, 'MSFT': 75, 'GOOG': 10})

# Example 2 — Using defaultdict to Group Trades by Trader, Symbol, or Desk
# Trade‑booking and middle‑office systems often need to create buckets or groups of trades.
# defaultdict(list) is ideal for this.

# Scenario:
# Group trades by trader to compute P&L attribution later.

# Why defaultdict is useful in FS
# - Used for P&L attribution by book, trader, desk
# - Common in limit monitoring (group exposures per owner)
# - Helps build per‑symbol or per‑venue breakdowns
# - Cleaner than checking if key not in dict repeatedly
from collections import defaultdict

trades = [
    {"trader": "Alice", "symbol": "AAPL", "qty": 100},
    {"trader": "Bob", "symbol": "MSFT", "qty": 50},
    {"trader": "Alice", "symbol": "GOOG", "qty": 80},
    {"trader": "Bob", "symbol": "AAPL", "qty": 30},
]

by_trader = defaultdict(list)
for t in trades:
    by_trader[t["trader"]].append(t)

print(by_trader)
# Expected Output
# {
#     'Alice': [
#         {'trader': 'Alice', 'symbol': 'AAPL', 'qty': 100},
#         {'trader': 'Alice', 'symbol': 'GOOG', 'qty': 80}
#     ],
#     'Bob': [
#         {'trader': 'Bob', 'symbol': 'MSFT', 'qty': 50},
#         {'trader': 'Bob', 'symbol': 'AAPL', 'qty': 30}
#     ]
# }

# Example 3 — deque for Market Data Rolling Windows
# deque gives O(1) append/pop from both ends → perfect for rolling metrics,
# e.g., VWAP, moving averages.
# Used for:
# - real‑time analytics
# - signal generation
# - algorithmic trading windows
from collections import deque

window = deque(maxlen=3)

prices = [100.2, 100.4, 100.1, 101.0, 99.8]

for p in prices:
    window.append(p)
    print("Window:", list(window), "Avg:", sum(window)/len(window))

# Example 4 — namedtuple for Lightweight Trade Records
# Faster and lighter than classes.
# namedtuple is useful in:
# - backtesting
# - data pipelines
# - high-performance trade records
from collections import namedtuple

Trade = namedtuple("Trade", ["id", "symbol", "qty", "price"])

t = Trade("T1", "AAPL", 100, 175.50)

print(t.symbol, t.qty * t.price)

from collections import namedtuple
# Define the namedtuple type
account_fields = ["account_number", "customer_name", "balance"]
BankAccount = namedtuple("BankAccount", account_fields)

# Create account instances
acct1 = BankAccount(account_number="00123456", customer_name="Alice", balance=1500.00)
acct2 = BankAccount("00987654", "Bob", 320.75) # can be done positionally

# Accessing fields
print(f"{acct1.customer_name} has £{acct1.balance}")
print(f"Account {acct2.account_number} belongs to {acct2.customer_name}")

# Updating a balance using _replace (namedtuples are immutable)
acct1_updated = acct1._replace(balance=acct1.balance + 200)
print(f"After deposit: {acct1_updated.customer_name} now has £{acct1_updated.balance}")

### Deques  ###
from collections import deque

# A transaction is represented as a simple dictionary for demo purposes
transaction_queue = deque()

# Incoming transactions (arrive in real time)
transaction_queue.append({"type": "deposit", "amount": 500})
transaction_queue.append({"type": "withdrawal", "amount": 120})
transaction_queue.append({"type": "deposit", "amount": 220})
transaction_queue.append({"type": "withdrawal", "amount": 80})

balance = 1000  # Starting balance for the customer account

print("Initial balance:", balance)
print()

# Process transactions in the order they arrived
while transaction_queue:
    txn = transaction_queue.popleft()   # Efficient O(1) FIFO removal

    if txn["type"] == "deposit":
        balance += txn["amount"]
        print(f"Processed deposit of £{txn['amount']}")
    elif txn["type"] == "withdrawal":
        # Simple overdraft check
        if balance >= txn["amount"]:
            balance -= txn["amount"]
            print(f"Processed withdrawal of £{txn['amount']}")
        else:
            print(f"Insufficient funds for £{txn['amount']} withdrawal")

    print("Current balance:", balance)
    print()

    # ChainMap

    from collections import ChainMap

    # Three separate directories
    employees = {
        "Alice Green": "020 7000 1234",
        "John Smith": "020 7000 5678",
    }

    customers = {
        "Mary Brown": "01632 960111",
        "Tom Harris": "01632 960222",
    }

    suppliers = {
        "ACME Supplies": "0141 555 2020",
        "PaperCo": "0141 555 3030",
    }

    # Combine them into a single searchable directory
    phone_directory = ChainMap(employees, customers, suppliers)
    # phone_directory = employees | customers | suppliers

    # Look up entries
    print(phone_directory["John Smith"])  # From employees
    print(phone_directory["Mary Brown"])  # From customers
    print(phone_directory["PaperCo"])  # From suppliers

    # Adding a new employee (affects ONLY the first map)
    employees["Chris Miles"] = "020 7000 9999"
    print(phone_directory["Chris Miles"]) # Fails for union of dictionaries

    # Adding a new layer — e.g., temporary contractors
    contractors = {"Zara Khan": "07700 900111"}
    phone_directory = phone_directory.new_child(contractors)  # Fails for union of dictionaries

    print(phone_directory["Zara Khan"])  # Found in the new top layer  # Fails for union of dictionaries
    print(phone_directory.parents["Alice Green"])  # Underlying maps unaffected

text = "Alas poor Yorrick, I knew him, Horatio"
print(Counter(text))

from collections import defaultdict

# Incoming transactions across many accounts
# positive = deposit, negative = withdrawal
transactions = [
    ("ACC1001", 500.00),
    ("ACC1002", 125.00),
    ("ACC1001", -75.00),
    ("ACC1003", 300.00),
    ("ACC1002", -25.00),
    ("ACC1001", 50.00),
]

# Start each unseen account at 0.0 automatically
balances = defaultdict(float)

for account_id, amount in transactions:
    balances[account_id] += amount

# Accessing a missing account safely returns 0.0 (and creates the key)
print("ACC9999 balance:", balances["ACC9999"])

# Report balances
for acc, bal in balances.items():
    print(f"{acc}: £{bal:.2f}")

dd = defaultdict(lambda:f"val-{len(dd)}")
print(dd['key1'], dd['key2'], dd['key3'], dd['key4'])


from collections import namedtuple
# Define the namedtuple type
account_fields = ["account_number", "customer_name", "balance"]
BankAccount = namedtuple("BankAccount", account_fields)

# Create account instances
acct1 = BankAccount(account_number="00123456", customer_name="Alice", balance=1500.00)
acct2 = BankAccount("00987654", "Bob", 320.75) # can be done positionally

# 1) _fields: see the schema (field names) of the namedtuple
print("BankAccount fields:", BankAccount._fields)   # ('account_number', 'customer_name', 'balance')

# 2) Example: turn a list of accounts into a list of plain dicts (e.g., for JSON)
accounts = [acct1, acct2]
as_dicts = [a._asdict() for a in accounts]
print("All accounts as dicts:", as_dicts)

my_account_data = ["0000234567", "Kamran", 1250.00]
my_account = BankAccount._make(my_account_data)
print(my_account)

my_new_account = my_account._replace(balance=2500.00)
print(my_new_account)
