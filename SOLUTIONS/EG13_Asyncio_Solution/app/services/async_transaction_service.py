import asyncio
from typing import Any

from app.utils.cleaners import clean_account_number
from app.services.transaction_service import query_transactions


# Single account fetch
async def fetch_transactions_for_account(
    account_number: str,
    result_queue: asyncio.Queue[dict[str, Any]],
) -> None:
    """Query transactions for one account number and put the result in our queue."""
    cleaned_account_number = clean_account_number(account_number)

    if cleaned_account_number is None:
        await result_queue.put(
            {
                "account_number": account_number,
                "status_code": 400,
                "error": "Invalid account number",
                "count": 0,
                "transactions": [],
            }
        )
        return

    # Run blocking function in thread
    transactions = await asyncio.to_thread(
        query_transactions,
        cleaned_account_number,
    )

    if not transactions:
        await result_queue.put(
            {
                "account_number": cleaned_account_number,
                "status_code": 404,
                "error": "No transactions found for the supplied account number",
                "count": 0,
                "transactions": [],
            }
        )
        return

    await result_queue.put(
        {
            "account_number": cleaned_account_number,
            "status_code": 200,
            "count": len(transactions),
            "transactions": transactions,
        }
    )


# Parallel execution
async def fetch_transactions_for_accounts(
    account_numbers: list[str],
) -> asyncio.Queue[dict[str, Any]]:
    """Run account queries concurrently and return a queue of results."""
    result_queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()

    tasks = [
        asyncio.create_task(
            fetch_transactions_for_account(account_number, result_queue)
        )
        for account_number in account_numbers
    ]

    await asyncio.gather(*tasks)
    return result_queue


# Drain queue
def drain_queue(
    result_queue: asyncio.Queue[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Pull all items from the queue into a list."""
    results: list[dict[str, Any]] = []

    while not result_queue.empty():
        results.append(result_queue.get_nowait())

    return results