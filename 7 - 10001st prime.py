from __future__ import division

def primes():
    ps = [2]
    yield 2
    c = 3
    while True:
        test_limit = c**.5
        if all(c/p != int(c/p) for p in ps if p < test_limit + 1):
            ps.append(c)
            yield c
        c += 2

def last(g, n):
    for ii in range(n-1):
        next(g)
    return next(g)
        
print(last(primes(), 10001))