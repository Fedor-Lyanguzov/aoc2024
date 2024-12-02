



data = open('input.txt').read().strip().split("\n")
data = [list(map(int, x.strip().split(" "))) for x in data]

less = lambda a, b: a<b
more = lambda a, b: a>b
q = lambda a, b: abs(a-b)<=3

def safe1(l):
    if l[0]<l[1]:
        f = less
    elif l[0]>l[1]:
        f = more
    else:
        return False
    return all(f(a, b) and q(a, b) for a, b in zip(l, l[1:]))

print(sum(1 for x in data if safe1(x)))

def safe2(l):
    r = False
    for i in range(len(l)):
        t = l[:]
        del t[i]
        r = r or safe1(t)
    return r

print(sum(1 for x in data if safe2(x)))
