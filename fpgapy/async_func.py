import asyncio
from .fpga_func import *

async def async_add(*args):
    a = []
    for arg in args:
        if type(arg) is asyncio.Task:
            arg = await arg
        a.append(arg)
    res = await add(a[0], a[1])
    return res

