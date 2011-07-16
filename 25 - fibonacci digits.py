def _fibonacci():
    fibs = {1: 1, 2: 1}
    def fib(n):
        if n not in fibs:
            fibs[n] = fib(n-1) + fib(n-2)
        return fibs[n]
    return fib
fibonacci = _fibonacci()

n = 1    
while len(str(fibonacci(n))) < 1000:
    n += 1
    
print(n)