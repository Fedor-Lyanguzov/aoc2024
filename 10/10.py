


data = open("input.txt").read().strip().split("\n")
data = [list(map(int, x)) for x in data]

def make_bound(data):
    N = len(data)
    M = len(data)
    def bound(i, j):
        return 0<=i<N and 0<=j<M
    return bound

def f1(data, collect=set):
    def score(i, j, x=0):
        if not bound(i, j):
            return
        if data[i][j]!=x:
            return
        if x==9:
            yield (i, j)
        for di, dj in d:
            yield from score(i+di, j+dj, x+1)
    zeroes = [(i, j) for i, l in enumerate(data) for j, x in enumerate(l) if x==0]
    bound = make_bound(data)
    d = [(1,0), (0,1), (-1,0), (0,-1)]
    return sum(1 for z in zeroes for _ in collect(score(*z)))
print(f1(data))
d = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''.strip().split("\n")
d = [list(map(int, x)) for x in d]
print(f1(d))

print(f1(data, iter))
