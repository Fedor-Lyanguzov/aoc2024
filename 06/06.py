


data = open("input.txt").read().strip().split("\n")
data = [list(x) for x in data]
v = set()
si, sj = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j]=="^"][0]
i, j = si, sj
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
k = 0
c = -1
di, dj = d[0]
while True:
    while 0<=i<len(data) and 0<=j<len(data[0]) and data[i][j]!='#':
        v.add((i, j))
        i, j = i+di, j+dj
    if not (0<=i<len(data) and 0<=j<len(data[0])):
        break
    i -= di
    j -= dj
    k = (k+1)%4
    di, dj = d[k]
print(len(v))

s = 0
v.remove((si, sj))
for xi, xj in v:
    v2 = set()
    data[xi][xj] = '#'
    di, dj = d[0]
    k = 0
    i, j = si, sj
    while True:
        while 0<=i<len(data) and 0<=j<len(data[0]) and data[i][j]!='#' and (i,j,k) not in v2:
            v2.add((i, j, k))
            i, j = i+di, j+dj
        if (i,j,k) in v2:
            s += 1
            break
        if not (0<=i<len(data) and 0<=j<len(data[0])):
            break
        i -= di
        j -= dj
        k = (k+1)%4
        di, dj = d[k]
    data[xi][xj] = '.'

print(s)
    
