import asyncio
import aiohttp

async def fetch(my_session, url):
    async with my_session.get(url) as http_response:
        return await http_response.json()

async def grab_data(url):
    async with aiohttp.ClientSession() as my_session:
        response = await fetch(my_session, url)
        return response

async def test_http_client():
    url = 'http://httpbin.org/json'
    resp = await grab_data(url)
    assert "Yours Truly" in resp['slideshow']['author']

if __name__ == '__main__':
    url = 'http://httpbin.org/json'
    my_loop = asyncio.get_event_loop()
    resp = my_loop.run_until_complete(grab_data(url))
    print(resp)
