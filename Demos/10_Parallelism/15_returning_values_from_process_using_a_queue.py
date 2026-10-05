from multiprocessing import Process, Queue

def apply_interest(account_index, result_queue, initial_balances):
    # Apply 5% interest and send result back via queue.
    current_balance = initial_balances[account_index]
    updated_balance = int(current_balance * 1.05)
    # Send result as a (key, value) tuple
    result_queue.put((account_index, updated_balance))


if __name__ == "__main__":
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]
    result_queue = Queue()
    processes = []
    for i in range(len(initial_balances)):
        p = Process(target=apply_interest,
                    args=(i, result_queue, initial_balances))
        processes.append(p)
        p.start()

    # Collect results
    results = {}
    for _ in range(len(initial_balances)):
        key, value = result_queue.get()
        results[key] = value

    for p in processes:
        p.join()

    print(f"Raw dictionary (likely unordered): {results}")

    print("\nSorted results (by account index):")
    for k in sorted(results):
        print(f"Account {k}: {results[k]}")