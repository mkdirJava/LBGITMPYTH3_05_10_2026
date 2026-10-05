from typing import TypeVar, Generic, List
from decimal import Decimal
# Define a Type Variable for generic support
T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        # Internal storage using a list
        self._items: List[T] = []

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def enqueue(self, item: T) -> None:
        """Add an item to the end of the queue."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)

# Example: A queue specifically for integers
decimal_queue = Queue[Decimal]()
decimal_queue.enqueue(Decimal("12.99"))
decimal_queue.enqueue(250.00) # mypy error
print(f"Is empty? {decimal_queue.is_empty()}") # Output: False
print(f"Dequeued: {decimal_queue.dequeue()}")   # Output: 12.99
