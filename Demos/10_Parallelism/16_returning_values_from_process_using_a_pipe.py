from multiprocessing import Process, Pipe

def apply_interest(account_index, conn, initial_balances):
    # Apply 5% interest and send result back via pipe.
    current_balance = initial_balances[account_index]
    updated_balance = int(current_balance * 1.05)
    conn.send((account_index, updated_balance))
    conn.close()

if __name__ == "__main__":
    initial_balances = [1000, 1500, 2000, 2500, 3000,
                        3500, 4000, 4500, 5000, 5500]
    processes = []
    parent_conns = []

    # Create a pipe per process
    for i in range(len(initial_balances)):
        parent_conn, child_conn = Pipe()
        p = Process(target=apply_interest,
                    args=(i, child_conn, initial_balances))
        processes.append(p)
        parent_conns.append(parent_conn)
        p.start()

    # Collect results
    results = {}
    for conn in parent_conns:
        key, value = conn.recv()
        results[key] = value
        conn.close()

    for p in processes:
        p.join()

    print(f"Raw dictionary (Ordered!): {results}")
