# result = 142913828922

m_val = 20000

def using_list_comps():
    def sieve(m_val):
        cs = range(2,m_val)
        while cs:
            yield cs[0]
            cs = [c for c in cs if c % cs[0] != 0]

    print(sum(sieve(m_val)))
    
using_list_comps()