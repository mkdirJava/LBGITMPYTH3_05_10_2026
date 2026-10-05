import time
from datetime import datetime, timezone


def transaction_reference_generator(prefix: str = "TXN"):
    """
    A generator that yields unique transaction references.

    Format:
    PREFIX-YYYYMMDD-HHMMSS-SEQ

    The sequence facet will reset each second.
    """
    last_timestamp = None
    seq = 0

    while True:
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y%m%d-%H%M%S")

        if timestamp == last_timestamp:
            seq += 1
        else:
            seq = 1
            last_timestamp = timestamp

        yield f"{prefix}-{timestamp}-{seq:04d}"


# Demo: print first 20 values
gen = transaction_reference_generator()

for _ in range(20):
    print(next(gen))
    # A small delay to show sequencing behaviour
    time.sleep(0.10)  