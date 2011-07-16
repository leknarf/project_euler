from __future__ import division

def hotpo(n):
    """half or third plus one"""
    while n != 1:
        yield n
        if n % 2:
            n = 3*n + 1
        else:
            n = n // 2
    yield n
    
seqs = ( (nn, list(hotpo(nn))) for nn in range(1, 1000000))
print(max(seqs, key=lambda t: len(t[1]))[0])    