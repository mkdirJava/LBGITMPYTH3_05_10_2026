import random

def generate_dummy_accounts(num_accounts=50, num_days=30, max_txns_per_day=5):
    accounts = {}

    for i in range(num_accounts):
        acc_id = f"ACC{1000 + i}"
        opening_balance = round(random.uniform(500, 5000), 2)
        interest_rate = round(random.uniform(0.01, 0.05), 4)

        transactions_by_day = {}

        for day in range(num_days):
            num_txns = random.randint(0, max_txns_per_day)
            if num_txns > 0:
                transactions_by_day[day] = [
                    {"amount": round(random.uniform(-200, 500), 2)}
                    for _ in range(num_txns)
                ]

        accounts[acc_id] = {
            "opening_balance": opening_balance,
            "interest_rate": interest_rate,
            "transactions_by_day": transactions_by_day,
        }

    return accounts


# Generate a reasonably heavy dataset
accounts = generate_dummy_accounts(
    num_accounts=500,     # scale this up for more load
    num_days=180,
    max_txns_per_day=10
)

days = 60

import bank_utils
import cProfile
cProfile.run('bank_utils.calc_daily_interest(accounts, days)', 'start.prof')
cProfile.run('bank_utils.calc_daily_interest(accounts, days)')
print("**************************************************")
cProfile.run('bank_utils.calc_daily_interest_optimized(accounts, days)')
