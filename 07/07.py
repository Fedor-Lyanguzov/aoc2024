



data = open("input.txt").read().strip().split("\n")

def f(t, l, x=0, i=0):
    if i==len(l):
        return t==x
    return f(t, l, x+l[i], i+1) or \
           f(t, l, x*l[i], i+1)

def f2(t, l, x=0, i=0):
    if i==len(l):
        return t==x
    return f2(t, l, x+l[i], i+1) or \
           f2(t, l, x*l[i], i+1) or \
           f2(t, l, int(str(x)+str(l[i])), i+1)
s = 0
s2 = 0
for x in data:
    t, l = x.split(': ')
    t = int(t)
    l = [int(y) for y in l.split()]
    if f(t, l):
        s += t
    if f2(t, l):
        s2 += t
print(s)
print(s2)
