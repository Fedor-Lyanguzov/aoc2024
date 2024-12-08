from collections import defaultdict
import string
from itertools import combinations

data = open("input.txt").read().strip().split("\n")

d = defaultdict(list)
t = set(string.ascii_letters+string.digits)
for i, l in enumerate(data):
    for j, c in enumerate(l):
        if c in t:
            d[c].append((i, j))
width = len(data[0])
height = len(data)

def bound(x, width, height):
    i, j = x
    return 0<=i<height and 0<=j<width

def f(d):
    for v in d.values():
        for (ia, ja), (ib, jb) in combinations(v, 2):
            di = ib-ia
            dj = jb-ja
            yield (ib+di, jb+dj)
            yield (ia-di, ja-dj)

print(len(set(filter(lambda x: bound(x, width, height), f(d)))))


def f2(d):
    for v in d.values():
        for (ia, ja), (ib, jb) in combinations(v, 2):
            di = ib-ia
            dj = jb-ja
            x = 0
            while bound((ib+x*di, jb+x*dj), width, height):
                yield (ib+x*di, jb+x*dj)
                x += 1
            x = 0
            while bound((ia-x*di, ja-x*dj), width, height):
                yield (ia-x*di, ja-x*dj)
                x += 1


print(len(set(f2(d))))
