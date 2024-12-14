import re

pattern = re.compile(r'''
Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)
'''.strip(), re.MULTILINE)


data = open("input.txt").read().strip().split("\n\n")

data = [tuple(map(int, pattern.match(x).groups())) for x in data]

tok = lambda x: x[0]*3+x[1]
def f(data):
    s = 0
    for n, (xa, ya, xb, yb, xt, yt) in enumerate(data):
        s1 = set()
        for i in range(min(xt//xa+1, 101)):
            for j in range(min(xt//xb+1, 101)):
                    if xa*i+xb*j==xt:
                        s1.add((i, j))
        s2 = set()
        for i in range(min(yt//ya+1, 101)):
            for j in range(min(yt//yb+1, 101)):
                    if ya*i+yb*j==yt:
                        s2.add((i, j))
        if s1&s2:
            s += tok(min(s1&s2, key=tok))
    return s


def f2(data):
    s = 0
    for i, (xa, ya, xb, yb, xt, yt) in enumerate(data):
        xt += 10_000_000_000_000
        yt += 10000000000000
        d = xa*yb - xb*ya
        da = xt*yb - xb*yt
        db = xa*yt - xt*ya
        if da%d==db%d==0:
            a = da//d
            b = db//d
            s += a*3+b
    return s
print(f(data))
print(f2(data))
