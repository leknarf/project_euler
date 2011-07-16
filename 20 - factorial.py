def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)
        
print(sum(int(d) for d in str(factorial(100))))