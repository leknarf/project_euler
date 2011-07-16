from __future__ import division

MAX_VAL = 10000

def divisors(n):
    yield 1
    for i in range(2, int(n**.5)):
        if int(n / i) == n / i:
            yield i
            yield n // i

def amicable(n, m):
    return (sum(divisors(n)) == m) and (sum(divisors(m)) == n)
            
def find_amicables():
    for i in range(1, MAX_VAL):
        s = sum(divisors(i))
        if s != i and sum(divisors(s)) == i:
            yield i
                
print(sum(find_amicables()))