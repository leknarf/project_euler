with open('13.data') as ff:
    vals =  (int(ll.strip()) for ll in ff)
    print(str(sum(vals))[:10])