import fpgapy as fp
import asyncio

def set_add(a0, a1):
    # fake implementation
    res = fp.empty_like(a0)
    for i in range(a0.size):
        res[i] = a0[i] + a1[i]
    return res
    
async def get_add(res):
    # fake implementation
    await asyncio.sleep(0.1)
    return res
