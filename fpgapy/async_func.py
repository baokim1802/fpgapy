import asyncio
from .fpga_func import add

async def async_add(a0, a1):
    if type(a0) is asyncio.Task:
        a0 = await a0
    if type(a1) is asyncio.Task:
        a1 = await a1
    res = await add(a0, a1)
    return res

