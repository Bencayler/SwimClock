import asyncio

async def main():
    print('Tim')
    await foo('Text')

async def foo(text):
    print(text)
    await asyncio.sleep(1)
# Await its execution
# print(main())
# await main() # There is an await outside the funciton
# The await keyword must be inside an asynchronous function

# We have to create the event loop or at least start one
asyncio.run(main())