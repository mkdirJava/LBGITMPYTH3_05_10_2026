import os
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from multiprocessing import Manager
from typing import Iterator


def transaction_reference_generator(
    prefix: str,
    node_id: str,
    worker_id: str,
    shared_seq,
    lock,
) -> Iterator[str]:
    """
    Multiprocess-safe transaction reference generator using shared sequence + lock.
    """

    pid = os.getpid()

    while True:
        timestamp_ms = time.time_ns() // 1_000_000

        # Critical section
        with lock:
            shared_seq.value += 1
            sequence = shared_seq.value

        dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
        ts = dt.strftime("%Y%m%dT%H%M%S") + f"{timestamp_ms % 1000:03d}"

        yield f"{prefix}-{node_id}-{worker_id}-{ts}-{pid:05d}-{sequence:06d}"


def generate_ids(worker_id: str, count: int, shared_seq, lock):
    """
    Worker task executed in a process from the pool.
    """
    pid = os.getpid()
    print(f"{worker_id} running in PID {pid}")

    gen = transaction_reference_generator(
        prefix="TXN",
        node_id="BANK01",
        worker_id=worker_id,  # SAME for all workers now
        shared_seq=shared_seq,
        lock=lock,
    )

    return [(worker_id, next(gen)) for _ in range(count)]


def demo_process_pool():
    worker_count = 4
    ids_per_worker = 10
    shared_worker_id = "WZZ"   # same worker ID for all

    results = []

    with Manager() as manager:
        shared_seq = manager.Value("i", 0)  # shared integer
        lock = manager.Lock()

        with ProcessPoolExecutor(max_workers=worker_count) as executor:
            futures = [
                executor.submit(
                    generate_ids,
                    shared_worker_id,
                    ids_per_worker,
                    shared_seq,
                    lock,
                )
                for _ in range(worker_count)
            ]

            for future in futures:
                results.extend(future.result())

    ids = [txn_id for _, txn_id in results]
    unique_ids = set(ids)

    print("\nGenerated IDs:")
    for worker_id, txn_id in sorted(results):
        print(f"{worker_id}: {txn_id}")

    print("\nSummary")
    print(f"Total generated: {len(ids)}")
    print(f"Unique generated: {len(unique_ids)}")
    print(f"Collisions found: {len(ids) - len(unique_ids)}")

    if len(ids) == len(unique_ids):
        print("No collisions detected across workers.")


if __name__ == "__main__":
    demo_process_pool()