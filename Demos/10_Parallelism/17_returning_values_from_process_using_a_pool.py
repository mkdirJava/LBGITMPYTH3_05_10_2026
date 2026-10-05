from multiprocessing import Pool

def apply_interest(args):
    # Apply 5% interest and return result.
    account_index, initial_balances = args
    current_balance = initial_balances[account_index]
    updated_balance = int(current_balance * 1.05)
    return (account_index, updated_balance)

if __name__ == "__main__":
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]

    tasks = [(i, initial_balances) for i in range(len(initial_balances))]
    with Pool(processes=4) as pool:
        # Map runs apply_interest across all tasks
        results_list = pool.map(apply_interest, tasks)

    # Convert list of tuples into dictionary
    results = dict(results_list)

    print(f"Raw dictionary (Ordered!): {results}")