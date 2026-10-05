from collections import deque

transactions = deque([
    {"id": 1, "type": "payment", "amount": 200},
    {"id": 2, "type": "withdrawal", "amount": 5000},  # suspicious
    {"id": 3, "type": "deposit", "amount": 150},
])

processed = []
retry_limit = 2

while transactions:
    txn = transactions.popleft()

    # Simulate rules
    if txn["amount"] > 3000 and not txn.get("reviewed"):
        print(f"Transaction {txn['id']} flagged for review")

        txn["reviewed"] = True
        transactions.appendleft(txn)  # PRIORITY: re-process soon
        continue

    if txn.get("attempts", 0) < retry_limit:
        txn["attempts"] = txn.get("attempts", 0) + 1

        if txn["type"] == "payment":
            print(f"Temporary failure on txn {txn['id']}, retrying later")
            transactions.append(txn)  # push to END for retry
            continue

    print(f"Processed txn {txn['id']}")
    processed.append(txn)