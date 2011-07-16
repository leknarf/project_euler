from __future__ import division

max_val = 20
factors = range(max_val, 1, -1)
def div_by_all(x):
    return all(x/factor == int(x/factor) for factor in factors)
    
def find_smallest():
    x = 1
# Actual answer    
#    x = 232792560
    while True:
        if div_by_all(x):
            return x
        x += max_val
    
if __name__ == '__main__':
    print(find_smallest())