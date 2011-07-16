def triplet(a, b, c):
    return a**2 + b**2 == c**2
    
max_val = 1000
for a in range(1,max_val + 1):
    for b in range(1, max_val + 1):
        c = max_val - a - b
        if triplet(a,b,c):
            print(a*b*c)
            exit()