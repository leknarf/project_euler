known_numbers = {0: False, 1 : True, 89: False}
def _test_happy(n):
    if n in known_numbers:
        return known_numbers[n]
    return _test_happy(sum(int(d)**2 for d in str(n)))

def happy(n):
    """
    Returns True if n is a happy number
    >>> happy(44)
    True
    >>> happy(89)
    False
    """
    if n not in known_numbers:
        known_numbers[n] = _test_happy(n)
    return known_numbers[n]        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
#    import timeit
#    t = timeit.Timer("sum(1 for n in range(10**6) if not h.happy(n))", 
#        "h = __import__('92 - happy numbers')")
#    print(min(t.repeat(3, 1)))
    
    print(sum(1 for n in range(10**7 -1) if not happy(n)))