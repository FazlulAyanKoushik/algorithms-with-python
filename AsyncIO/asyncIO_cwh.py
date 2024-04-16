import threading
import time
import asyncio
import requests


async def function_1():
    url = "https://www.instagram.com/favicon.ico"
    print(f"Started function_1 at {time.strftime('%X')}")
    response = requests.get(url)
    open("favicon.ico", "wb").write(response.content)
    await asyncio.sleep(4)
    print(f"Ended function_1 at {time.strftime('%X')}")
    return "function_1 is returned"


async def function_2():
    print(f"Started function_2 at {time.strftime('%X')}")
    await asyncio.sleep(2)
    print(f"Ended function_2 at {time.strftime('%X')}")
    return "function_2 is returned"


async def function_3():
    print(f"Started function_3 at {time.strftime('%X')}")
    await asyncio.sleep(5)
    print(f"Ended function_3 at {time.strftime('%X')}")
    return "function_3 is returned"


async def main():
    # task1 = asyncio.create_task(function_1())
    # task2 = asyncio.create_task(function_2())
    # task3 = asyncio.create_task(function_3())
    #
    # await task1
    # await task2
    # await task3

    tasks = await asyncio.gather(
        function_1(),
        function_2(),
        function_3()
    )

    print("Tasks are running...", tasks)

    print("All tasks are completed")


asyncio.run(main())
