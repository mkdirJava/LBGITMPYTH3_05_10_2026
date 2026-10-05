import time
from datetime import datetime, timezone


class TransactionReferenceIterator:
    """
    A Customer Iterator that yields unique transaction references.

    Format:
    PREFIX-YYYYMMDD-HHMMSS-SEQ

    Sequence resets each second.
    """

    def __init__(self, prefix: str = "TXN"):
        self.prefix = prefix
        self.last_timestamp = None
        self.seq = 0

    def __iter__(self):
        return self

    def __next__(self):
        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y%m%d-%H%M%S")
        if timestamp == self.last_timestamp:
            self.seq += 1
        else:
            self.seq = 1
            self.last_timestamp = timestamp

        return f"{self.prefix}-{timestamp}-{self.seq:04d}"

def test_transaction_reference_iterator():
    iterator = TransactionReferenceIterator()
    # Print the first 20 transaction numbers
    for _ in range(20):
        print(next(iterator))
        time.sleep(0.10)

# Run our test sequence
if __name__ == "__main__":
    test_transaction_reference_iterator()
