import asyncio
import inspect

#coroutine
async def say_hello1(name, delay):
    await asyncio.sleep(delay)
    print("Hello,", name)

def say_hello2(name, delay):
    asyncio.sleep(delay) # Error: won't be awaited but rest of code will still run
    #yield asyncio.sleep(delay)
    print("Hello,", name)

#decorated legacy generator-based coroutine
#@asyncio.coroutine # No longer supported in Python versions >= 3.11
def say_hello3(name, delay):
    # await asyncio.sleep(delay)
    yield "hello"
    yield name
    print("Hello,", name)

async def main():
    res = await say_hello1("Ted 1", 3)
    res =  say_hello2("Ted 2", 2)
    #async for res in say_hello3("Ted 3", 1):
    #    print(res)

    print(f"Is coroutine? {inspect.iscoroutinefunction(say_hello1)}")
    print(f"Is coroutine? {inspect.iscoroutinefunction(say_hello2)}")
    #print(f"Is coroutine? {inspect.iscoroutinefunction(say_hello3)}")

asyncio.run(main())
