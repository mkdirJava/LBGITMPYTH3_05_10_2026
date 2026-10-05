import asyncio
import aiofiles
my_files = ["badfiles.txt",  "goodfiles.txt", "otherfiles.txt"]

async def save_data(filename, data):
    fp = await aiofiles.open(filename, "w")
    await fp.write(data + "\n")
    await fp.close()

async def main():
    await asyncio.gather(save_data(my_files[0], "bad stuff"),
   		      save_data(my_files[1], "good stuff"),
		      save_data(my_files[2], "other stuff"))

if __name__ == '__main__':
    asyncio.run(main())
