#from __future__ import annotations

import os
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from typing import Iterator


def transaction_reference_generator(
    prefix: str,
    node_id: str,
    worker_id: str,
) -> Iterator[str]:
    """
    Multiprocess-safe transaction reference generator.

    Format:
        PREFIX-NODEID-WORKERID-YYYYMMDDTHHMMSSmmm-PID-SEQ

    Example:
        TXN-BANK01-W01-20260405T153210123-04217-0001
    """
    pid = os.getpid()
    last_timestamp_ms = -1
    sequence = 0

    while True:
        timestamp_ms = time.time_ns() // 1_000_000

        if timestamp_ms == last_timestamp_ms:
            sequence += 1
        else:
            last_timestamp_ms = timestamp_ms
            sequence = 1

        dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
        ts = dt.strftime("%Y%m%dT%H%M%S") + f"{timestamp_ms % 1000:03d}"

        yield f"{prefix}-{node_id}-{worker_id}-{ts}-{pid:05d}-{sequence:04d}"


def generate_ids(worker_id: str, count: int) -> list[tuple[str, str]]:
    """
    Worker task executed in a process from the pool.
    """
    pid = os.getpid()
    print(f"{worker_id} running in PID {pid}")

    gen = transaction_reference_generator(
        prefix="TXN",
        node_id="BANK01",
        worker_id=worker_id,
    )

    return [(worker_id, next(gen)) for _ in range(count)]


def demo_process_pool() -> None:
    worker_count = 4
    ids_per_worker = 10

    results: list[tuple[str, str]] = []

    with ProcessPoolExecutor(max_workers=worker_count) as executor:
        futures = [
            executor.submit(generate_ids, f"W{i+1:02d}", ids_per_worker)
            for i in range(worker_count)
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