from concurrent.futures import ThreadPoolExecutor
import time, random

# Simulate applying interest to a bank account
def apply_interest(account_id, balance):
    time.sleep(random.uniform(0.1, 0.5))  # simulate processing delay
    new_balance = balance * 1.05
    return f"Account {account_id}: £{balance:.2f} -> £{new_balance:.2f}"

if __name__ == "__main__":
    accounts = {101: 1000, 102: 1500, 103: 2000, 104: 2500, }

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []

        # Submit tasks individually
        for acc_id, balance in accounts.items():
            future = executor.submit(apply_interest, acc_id, balance)
            futures.append(future)

        # Retrieve results
        for future in futures:
            result = future.result()  # blocks until the task is complete
            print(result)