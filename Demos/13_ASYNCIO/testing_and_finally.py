import asyncio

async def timed_warning(msg: str="Resume in...", counter: int=5) -> str:
    while counter > 0:
        print(f"{msg} {counter} seconds")
        await asyncio.sleep(1)
        counter -= 1
    return "Completed!"

if __name__ == "__main__":
    print("Action #1")
    result: str = asyncio.run(timed_warning("Go in..", 3))
    print(result)
    print("Action #2")
