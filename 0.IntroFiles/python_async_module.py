import asyncio

async def task1():
    print("Send the first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(5) # Simulation time as 2 sec
    print("First Email reply")
    # task2()

async def task2():
    print("Send the second Email")
    asyncio.create_task(task3())
    await asyncio.sleep(5)
    print("Second Email reply")
    # task3()

async def task3():
    print("Send third reply")
    await asyncio.sleep(5)
    print("Third Email reply")
    print("------------End-----------")


asyncio.run(task1())