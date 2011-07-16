def products():
    a, b = 100, 999
    for ii in range(b, a, -1):
        for jj in range(b, a, -1):
            yield ii * jj
            
def is_palindrome(x):
    s = str(x)
    return s == ''.join(reversed(s))
        
def find_largest_palindrome():
    return max(p for p in products() if is_palindrome(p))
        
if __name__ == '__main__':
    print(find_largest_palindrome())