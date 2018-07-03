import fpgapy as fp

async def add(a0, a1):
    # fake implementation
    res = fp.empty_like(a0)
    for i in range(a0.size):
        res[i] = a0[i] + a1[i]
    return res
