from my_web_app.app import app
# from fastapi.testclient import TestClient
import pytest
import asyncio


import httpx
import asyncio
import uvicorn
import time
import threading

@pytest.fixture(scope="function")
def run_fastapi_server():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="warning")
    server = uvicorn.Server(config)
    
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    
    time.sleep(0.5)  # Let port binding complete
    yield

async def fetch_transactions(account_number:str):
    url = f"http://127.0.0.1:8000/transaction/?account_number={account_number}"
    
    # Pass query parameters as a clean dictionary
    params = {
        "account_number": "003",
        "transaction_type": "DEBIT"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()



async def get_queue_results(queue : asyncio.Queue, expected_count:int) ->[]:
    results = []
    
    # Run the loop exactly the number of times as items pushed
    for _ in range(expected_count):
        item = await queue.get()
        try:
            res = await item  # Await the coroutine directly
            results.append(res)
        except Exception as e:
            print(f"Error processing item: {e}")
        finally:
            queue.task_done()
            
    return results


@pytest.mark.asyncio
async def test_web_app(run_fastapi_server):
    queue = asyncio.Queue()
    tasks = [
        fetch_transactions("001"),
        fetch_transactions("002"),
        fetch_transactions("003"),
        fetch_transactions("004"),
        fetch_transactions("abc")
    ]
    for task in tasks:
        await queue.put(task)
    results = await get_queue_results(queue, expected_count=len(tasks))
    print(results)
    