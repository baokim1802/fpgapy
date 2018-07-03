import asyncio
from .fpga_func import *

def await_args(func):
    async def func_wrapper(*args):
        a = [await arg if type(arg) is asyncio.Task else arg for arg in args]
        return await func(*a)
    return func_wrapper

@await_args
async def async_add(*args):
    res = await add(*args)
    return res

