import asyncio
import aiohttp
import pytest, pytest_asyncio

async def fetch(my_session, url, request):
    # for captured stdout
    print(url, request)   
    async with my_session.post(url, json=request) as http_response:
        return await http_response.json()

async def grab_data(url, request):
    async with aiohttp.ClientSession() as my_session:
        response = await fetch(my_session, url, request)
        return response 

@pytest_asyncio.fixture
async def make_bulk():
    # simulate getting test postcodes from another source with I/O delay
    await asyncio.sleep(0.1)
    postcodes = ["gl13qn", "gl26hn", "gl11nu"]
    return {"postcodes": postcodes}

async def test_service_any_valid_responses(make_bulk):
    url = 'http://api.postcodes.io/postcodes'
    resp = await grab_data(url, make_bulk)
    outcomes = [result['result'] is not None for result in resp['result']]
    assert any(outcomes)

async def test_service_all_valid_responses(make_bulk):
    url = 'http://api.postcodes.io/postcodes'
    resp = await grab_data(url, make_bulk)
    outcomes = [result['result'] is not None for result in resp['result']]
    assert all(outcomes)


if __name__ == '__main__':
    url = 'http://api.postcodes.io/postcodes'
    postcode = "W1A 1AA"
    post_json = {"postcodes": [postcode]}
    my_loop = asyncio.get_event_loop()
    resp = my_loop.run_until_complete(grab_data(url, post_json))
    print(f"Response:\n{resp}\n")

