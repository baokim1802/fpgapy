import fpgapy as fp

async def add(*a):
    # fake implementation
    res = fp.empty_like(a[0])
    for i in range(a[0].size):
        res[i] = a[0][i] + a[1][i]
    return res
