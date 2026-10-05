import asyncio


async def do_something(myarg):
    pass

#@asyncio.coroutine      # Now deprecated!
async def do_something_times_table(my_num):
    # Perform some calculations here..!
    result = ""
    for i in range(10):
        await asyncio.sleep(my_num/10)
        result +=  f"{i * my_num}, \n"
    return result

print(asyncio.run(do_something_times_table(10)))

