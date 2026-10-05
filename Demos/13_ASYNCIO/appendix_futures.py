import asyncio

def callback(future):
    print(f"future done! : {future.result()}")

async def register_callbacks(future_obj):
    future_obj.add_done_callback(callback)

async def main():
    my_future = asyncio.Future()
    await register_callbacks(my_future)
    my_future.set_result('future result!!!')

asyncio.run(main())
