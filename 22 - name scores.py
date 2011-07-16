def name_score(i, name):
    return i*sum(ord(c) - 64 for c in name)

with open('22 - name scores.txt') as data:
    names = next(data).split(',')
    
names = sorted(name.strip('"') for name in names)
names = ((ii + 1, name) for ii, name in enumerate(names))

print(sum(name_score(*name) for name in names))