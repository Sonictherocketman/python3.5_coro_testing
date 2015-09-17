import asyncio, types

async def do_something(n, loop):
    await count(n, loop)

@types.coroutine
def count(n, loop):
    yield from loop.run_in_executor(None, do_count, n)

def do_count(n):
    for i in range(n):
        for x in range(i):
            continue

loop = asyncio.get_event_loop()
tasks= [
        do_something(2000, loop),
        do_something(15000, loop),
        do_something(10000, loop),
        do_something(1000, loop),
        do_something(12000, loop)]

coro = asyncio.gather(*(task for task in tasks))
loop.run_until_complete(coro)
loop.close()

