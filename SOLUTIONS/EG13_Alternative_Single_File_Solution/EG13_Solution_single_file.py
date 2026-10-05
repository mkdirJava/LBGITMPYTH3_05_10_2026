from __future__ import annotations

import asyncio
from pprint import pprint
from typing import Any

from EG12_Solution import clean_account_number, query_transactions


async def fetch_transactions_for_account(
    account_number: str,
    result_queue: asyncio.Queue[dict[str, Any]],
) -> None:
    """Query transactions for one account number and put the result in a queue."""
    cleaned_account_number = clean_account_number(account_number)

    if cleaned_account_number is None:
        await result_queue.put(
            {
                "account_number": account_number,
                "status_code": 400,
                "error": "account_number must be an 8-digit numeric string",
                "count": 0,
                "transactions": [],
            }
        )
        return

    transactions = await asyncio.to_thread(
        query_transactions,
        cleaned_account_number,
    )

    if not transactions:
        await result_queue.put(
            {
                "account_number": cleaned_account_number,
                "status_code": 404,
                "error": "No transactions found for the supplied account_number",
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


def drain_queue(
    result_queue: asyncio.Queue[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Pull all items from the queue into a list."""
    results: list[dict[str, Any]] = []

    while not result_queue.empty():
        results.append(result_queue.get_nowait())

    return results


def pretty_print_results(results: list[dict[str, Any]]) -> None:
    """Pretty print the collected query results."""
    for index, result in enumerate(results, start=1):
        print(f"\nResult {index}")
        print("-" * 60)
        pprint(result, sort_dicts=False)


async def main() -> None:
    """Run five account-number queries in parallel and print the results."""
    account_numbers = [
        "10872248",
        "44187304",
        "25001881",
        "99999999",
        "bad-input",
    ]

    result_queue = await fetch_transactions_for_accounts(account_numbers)
    results = drain_queue(result_queue)
    pretty_print_results(results)


if __name__ == "__main__":
    asyncio.run(main())