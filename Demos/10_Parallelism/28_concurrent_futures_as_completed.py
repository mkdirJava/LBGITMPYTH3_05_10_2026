
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

# Simulate a bank transaction (e.g., fraud check or balance update)
def process_transaction(account_id, amount):
    processing_time = random.uniform(0.1, 0.6)
    time.sleep(processing_time)  # simulate variable delay

    new_bal = 1000 + amount  # pretend starting balance is 1000
    return f"Acc {account_id}: proc: £{amount:+.2f}, new bal: £{new_bal:.2f}"

if __name__ == "__main__":
    transactions = [(201, 200),(202, -150),(203, 500),(204, -50),(205, 300),]

    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks and keep track of futures
        future_to_account = {
            executor.submit(process_transaction, acc_id, amount):
                acc_id for acc_id, amount in transactions
        }

        # Process results as they complete (order may vary)
        for future in as_completed(future_to_account):
            result = future.result()
            print(result)
