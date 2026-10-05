import threading
from concurrent.futures import ThreadPoolExecutor

def apply_interest(args):
    # Apply 5% interest and return result.
    account_index, initial_balances = args
    current_balance = initial_balances[account_index]
    updated_balance = int(current_balance * 1.05)
    print(f'executing {threading.current_thread().name}')
    return (account_index, updated_balance)

if __name__ == "__main__":
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]

    tasks = [(i, initial_balances) for i in range(len(initial_balances))]

    with ThreadPoolExecutor(max_workers=4) as executor:
        # map applies the function to each item in tasks
        results_list = list(executor.map(apply_interest, tasks))

    # Convert list of tuples into dictionary
    results = dict(results_list)

    print(f"Raw dictionary (Ordered!): {results}")

