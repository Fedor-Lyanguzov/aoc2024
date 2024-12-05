from collections import defaultdict
from itertools import permutations

data1, data2 = open('input.txt').read().strip().split("\n\n")

rules = defaultdict(list)
for x in data1.split('\n'):
    v, k = x.split('|')
    rules[k].append(v)

chains = [x.split(",") for x in data2.split('\n')]
def correct(c):
    for i, k in enumerate(c):
        y = c[i+1:]
        if any(x in y for x in rules[k]):
            return False
    return True


s = 0
incorrect = []
for c in chains:
    if correct(c):
        s += int(c[len(c)//2])
    else:
        incorrect.append(c)
print(s)

s = 0
for c in incorrect:
    while not correct(c):
        nc = []
        for i, k in enumerate(c):
            n = [x for x in rules[k] if x in set(c[i+1:])]
            for x in n:
                c.remove(x)
            nc.extend(n)
            nc.append(k)
        c = nc
    
    s += int(c[len(c)//2])
print(s)
