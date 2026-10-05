from concurrent.futures import ThreadPoolExecutor
import time, random

# Simulate processing a bank transfer
def process_transfer(account_id, amount):
    time.sleep(random.uniform(0.2, 0.6))  # simulate delay
    new_balance = 1000 + amount  # assume initial balance
    return (account_id, amount, new_balance)

# Callback function that runs when the task is done
def notify_completion(future):
    if future.cancelled():
        print(f"Cancelled: {future.arg}")
    elif future.done():
        if err := future.exception():
            print(f"Error: {future.arg} {err}")
        else:
            account_id, amount, new_balance = future.result()
            print(f"[Callback] Acc {account_id}: "
                  f"Proc: £{amount:+.2f}, new bal: £{new_balance:.2f}")

if __name__ == "__main__":
    transfers = [(301, 200),(302, -100),(303, 350),(304, -50),]

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []

        # Submit tasks and attach callbacks
        for acc_id, amount in transfers:
            future = executor.submit(process_transfer, acc_id, amount)
            future.add_done_callback(notify_completion)
            futures.append(future)

        # Optional: wait for all tasks to complete
        for f in futures:
            f.result()  # ensures main thread waits