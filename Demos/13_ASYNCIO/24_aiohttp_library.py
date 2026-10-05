import aiohttp
import asyncio

async def fetch(my_session, url):
    async with my_session.get(url) as http_response:
        return await http_response.text()

async def main():
    async with aiohttp.ClientSession() as my_session:
        html = await fetch(my_session, "http://bbc.co.uk")
        print(html)

if __name__ == '__main__':
    my_loop = asyncio.new_event_loop()
    my_loop.run_until_complete(main())
