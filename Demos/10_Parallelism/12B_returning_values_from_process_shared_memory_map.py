from multiprocessing import Process, Array

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def __repr__(self):
        return f"Account({self.account_id}, Balance={self.balance})"


def apply_interest(index, shared_balances):
    """
    Apply 5% interest to the account balance at the given index.
    """
    balance = shared_balances[index]
    updated_balance = int(balance * 1.05)
    shared_balances[index] = updated_balance


if __name__ == "__main__":
    # Create Account objects
    accounts = []
    for i, val in enumerate(range(1000, 6000, 500), 1):
        accounts.append(Account(i, val))

    # Extract balances into shared memory array
    shared_balances = Array('i', [acc.balance for acc in accounts])

    processes = []

    # Launch processes
    for i in range(len(accounts)):
        p = Process(target=apply_interest, args=(i, shared_balances))
        processes.append(p)
        p.start()

    # Wait for completion
    for p in processes:
        p.join()

    # Copy results back into Account objects
    for i, acc in enumerate(accounts):
        acc.balance = shared_balances[i]

    print("Finished processing accounts")
    print(accounts)