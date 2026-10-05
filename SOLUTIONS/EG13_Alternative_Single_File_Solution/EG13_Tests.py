from __future__ import annotations
import asyncio
import pytest

from EG13_Solution import (
    drain_queue,
    fetch_transactions_for_account,
    fetch_transactions_for_accounts,
)


@pytest.mark.asyncio
async def test_fetch_transactions_for_account_success() -> None:
    result_queue: asyncio.Queue[dict[str, object]] = asyncio.Queue()

    await fetch_transactions_for_account("10872248", result_queue)

    result = result_queue.get_nowait()
    assert result["status_code"] == 200
    assert result["account_number"] == "10872248"
    assert result["count"] >= 5
    assert isinstance(result["transactions"], list)


@pytest.mark.asyncio
async def test_fetch_transactions_for_account_invalid_input() -> None:
    result_queue: asyncio.Queue[dict[str, object]] = asyncio.Queue()

    await fetch_transactions_for_account("bad-input", result_queue)

    result = result_queue.get_nowait()
    assert result["status_code"] == 400
    assert result["account_number"] == "bad-input"
    assert result["count"] == 0
    assert result["transactions"] == []


@pytest.mark.asyncio
async def test_fetch_transactions_for_account_not_found() -> None:
    result_queue: asyncio.Queue[dict[str, object]] = asyncio.Queue()

    await fetch_transactions_for_account("99999999", result_queue)

    result = result_queue.get_nowait()
    assert result["status_code"] == 404
    assert result["account_number"] == "99999999"
    assert result["count"] == 0
    assert result["transactions"] == []


@pytest.mark.asyncio
async def test_fetch_transactions_for_accounts_returns_all_results() -> None:
    account_numbers = [
        "10872248",
        "44187304",
        "99999999",
        "bad-input",
        "25001881",
    ]

    result_queue = await fetch_transactions_for_accounts(account_numbers)
    results = drain_queue(result_queue)

    assert len(results) == 5
    returned_accounts = {result["account_number"] for result in results}
    assert "10872248" in returned_accounts
    assert "44187304" in returned_accounts
    assert "25001881" in returned_accounts
    assert "99999999" in returned_accounts
    assert "bad-input" in returned_accounts


def test_drain_queue_returns_all_items() -> None:
    result_queue: asyncio.Queue[dict[str, object]] = asyncio.Queue()

    result_queue.put_nowait({"account_number": "11111111", "status_code": 200})
    result_queue.put_nowait({"account_number": "22222222", "status_code": 404})

    results = drain_queue(result_queue)

    assert len(results) == 2
    assert result_queue.empty()