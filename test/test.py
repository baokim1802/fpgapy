import asyncio
import numpy as np
import fpgapy as fp

event_loop = asyncio.get_event_loop()
fp.set_event_loop(event_loop)

async def main():
    a = fp.array(np.arange(10))
    b = fp.array(np.ones(10))
    c = a + b
    print(c)        # it's a Task
    print(await c)  # it's an array

event_loop.run_until_complete(main())
