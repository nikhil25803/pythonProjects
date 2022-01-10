import asyncio

# @asyncio.coroutine
async def send_email():
    print("Hello")
    await asyncio.sleep(2)
    print("Awake Now") # Executes after two seconds

print(asyncio.iscoroutinefunction(send_email))





asyncio.run(send_email())