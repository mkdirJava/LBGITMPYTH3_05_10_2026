from multiprocessing import Process, Manager

def apply_interest(account_index, results_dict, initial_balances):
    """
    Apply 5% interest and store result in a shared dictionary.
    """
    current_balance = initial_balances[account_index]
    updated_balance = int(current_balance * 1.05)
    results_dict[account_index] = updated_balance

if __name__ == "__main__":
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]

    with Manager() as manager:
        results = manager.dict()  # shared dictionary
        processes = []

        for i in range(len(initial_balances)):
            p = Process(target=apply_interest,
                        args=(i, results, initial_balances))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print(f"Raw dictionary (likely unordered):\n{dict(results)}")

        print("\nSorted results (by account index):")
        for k in sorted(results):
            print(f"Account {k}: {results[k]}")
