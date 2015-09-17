import asyncio, types
from concurrent.futures import ProcessPoolExecutor as PPE

ppe = PPE()

# IO bound

async def do_something(fname, data, loop):
    await write(fname, data, loop)

@types.coroutine
def write(f, data, loop):
    yield from loop.run_in_executor(ppe, do_write, f, data)

def do_write(f, data):
    with open(f, 'w') as f:
        for line in data:
            f.write(line)

# CPU bound

async def do_something_else(n, loop):
    await count(n, loop)

@types.coroutine
def count(n, loop):
    for i in range(n):
        yield from loop.run_in_executor(ppe, do_count, i)

def do_count(i):
    for x in range(i):
        pass


loop = asyncio.get_event_loop()
tasks= [
        do_something_else(2000, loop),
        do_something_else(15000, loop),
        do_something('test3.dat', ['asdf'] * 1000000, loop),
        do_something('test4.dat', ['asdf'] * 100000, loop),
        do_something('test5.dat', ['asdf'] * 1200000, loop)]

coro = asyncio.gather(*(task for task in tasks))
loop.run_until_complete(coro)
loop.close()

