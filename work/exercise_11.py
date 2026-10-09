import asyncio
import time 



async def bacon(cook_time: float)-> str:
    time.sleep(cook_time)
    print("bacon done")
    return "Really Good Bacon "
async def eggs(cook_time: float)-> str:
    time.sleep(cook_time)
    print("eggs done")
    return "eggs over easy "
async def hash_brown(cook_time: float)-> str:
    print("hash brown done")
    time.sleep(cook_time)
    return "Cripsy Hash Browns "
async def beans(cook_time: float)-> str:
    time.sleep(cook_time)
    print("beans done")
    return "Very Beany beans"
async def sausages(cook_time:float)-> str:
    time.sleep(cook_time)
    print("really nice links")
    return "Sausages done"

async def make_breakfast():
    tasks = [
        asyncio.create_task(eggs(1.)),
        asyncio.create_task(bacon(2.0)),
        asyncio.create_task(hash_brown(3.0)),
        asyncio.create_task(beans(4.0)),
        asyncio.create_task(sausages(5.0)),
        ]
    result = await asyncio.gather(*tasks)
    print("".join(result))



if __name__ == "__main__":
    asyncio.run(make_breakfast())
