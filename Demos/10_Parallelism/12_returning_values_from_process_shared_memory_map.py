from multiprocessing import Process, Array

def apply_interest(account_index, balances):
    #Simulate a banking operation:
    # Apply 5% interest to the account balance at the given index.
    current_balance = balances[account_index]
    updated_balance = int(current_balance * 1.05)  # apply 5% interest
    balances[account_index] = updated_balance

if __name__ == "__main__":
    # Initial account balances (shared memory)
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]
    balances = Array('i', initial_balances)  # shared integer array
    # balances = initial_balances # won't work each process gets a copy of the collection which they update. The original collection remains unchanged
    processes = []

    for i in range(len(balances)):
        p = Process(target=apply_interest, args=(i, balances))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Updated balances: {list(balances)}")