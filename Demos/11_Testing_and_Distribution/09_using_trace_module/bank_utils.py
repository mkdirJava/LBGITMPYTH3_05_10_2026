def calc_daily_interest(accounts, days):
    results = {}
    if days == 0:
        days = 1

    for acc_id, data in accounts.items():
        balance = data["opening_balance"]
        rate = data["interest_rate"]
        transactions_by_day = data["transactions_by_day"]

        for day in range(days):
            # Apply that day's transactions
            for txn in transactions_by_day.get(day, []):
                balance += txn["amount"]

            # Inefficient: recompute rolling balance history each day
            cumulative = 0
            for past_day in range(day + 1):
                for txn in transactions_by_day.get(past_day, []):
                    cumulative += txn["amount"]

            interest = (balance + cumulative) * rate / 365
            balance += interest

        results[acc_id] = balance

    return results

def calc_daily_interest_optimized(accounts, days):
    results = {}
    if days == 0:
        return results

    for acc_id, data in accounts.items():
        balance = data["opening_balance"]
        rate = data["interest_rate"]
        transactions_by_day = data["transactions_by_day"]

        cumulative = 0  # Running total of all past transactions

        for day in range(days):
            # Apply today's transactions and update cumulative total once
            for txn in transactions_by_day.get(day, []):
                amount = txn["amount"]
                balance += amount
                cumulative += amount

            # Now reuse cumulative instead of recomputing it
            interest = (balance + cumulative) * rate / 365
            balance += interest

        results[acc_id] = balance

    return results

