from collections import defaultdict

data = list(map(int, open("input.txt").read().strip().split()))

def rules(x):
    if x==0:
        return [1]
    s = str(x)
    if len(s)%2==0:
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    return [x*2024]


def f(data, n):
    d = defaultdict(int)
    for x in data:
        d[x] += 1
    for i in range(n):
        t = defaultdict(int)
        for j, k in d.items():
            for x in rules(j):
                t[x] += k
        d = t
    return sum(d.values())

assert f(data, 25)==203609
print(f(data, 25))
print(f(data, 75))
