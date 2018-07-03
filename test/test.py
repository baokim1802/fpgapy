import asyncio
import fpgapy as fp

event_loop = asyncio.get_event_loop()
fp.set_event_loop(event_loop)

async def main():
    a = fp.array([0, 1, 2, 3])
    b = fp.array([1, 1, 1, 1])
    c = a + b
    d = c + b
    print(c)            # <Task pending coro=<async_add() running at ...>>
    print(d)            # <Task pending coro=<async_add() running at ...>>
    print(await d)      # array([2, 3, 4, 5], dtype='int64')
    print(c)            # <Task finished coro=<async_add() done, defined at ...> result=array([1, 2, ...dtype='int64')>
    print(d)            # <Task finished coro=<async_add() done, defined at ...> result=array([2, 3, ...dtype='int64')>

event_loop.run_until_complete(main())
