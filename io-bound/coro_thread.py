import asyncio, types

async def do_something(fname, data, loop):
    await write(fname, data, loop)

@types.coroutine
def write(f, data, loop):
    yield from loop.run_in_executor(None, do_write, f, data)

def do_write(f, data):
    with open(f, 'w') as f:
        for line in data:
            f.write(line)

loop = asyncio.get_event_loop()
tasks= [
        do_something('test1.dat', ['asdf'] * 200000, loop),
        do_something('test2.dat', ['asdf'] * 1500000, loop),
        do_something('test3.dat', ['asdf'] * 1000000, loop),
        do_something('test4.dat', ['asdf'] * 100000, loop),
        do_something('test5.dat', ['asdf'] * 1200000, loop)]

coro = asyncio.gather(*(task for task in tasks))
loop.run_until_complete(coro)
loop.close()

