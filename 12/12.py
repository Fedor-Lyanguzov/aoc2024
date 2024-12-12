from collections import defaultdict
d4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]



def make_field(data):
    data = data.strip().split("\n")
    data = ['.'*len(data[0])] + data + ['.'*len(data[0])]
    data = ['.'+x+'.' for x in data]
    return data

def regions(data, collect=len):
    def walk(i, j, c):
        nonlocal borders
        if data[i][j]!=c:
            return
        if (i, j) not in region:
            region.add((i, j))
            for di, dj in d4:
                if (i+di, j+dj) not in region:
                    borders += 1
                else:
                    borders -= 1
            for di, dj in d4:
                walk(i+di, j+dj, c)
    unmarked = {(i, j) for i in range(1, len(data)-1) for j in range(1, len(data)-1)}
    regions = []
    while unmarked:
        i, j = next(iter(unmarked))
        region = set()
        borders = 0
        walk(i, j, data[i][j])
        regions.append((collect(region), borders))
        unmarked -= region
    return regions

def sides(data):        
    for region, _ in regions(data, collect=lambda x: x):
        net = defaultdict(lambda: [0,0,0,0])
        for i, j in region:
            net[(i, j)][3] = 1
            net[(i+1, j)][0] = 1
            net[(i, j+1)][2] = 1
            net[(i+1, j+1)][1] = 1
        net2 = defaultdict(list)
        for (i, j), (a,b,c,d) in net.items():
            if a!=d:
                net2[(i, j)].append((i, j+1))
            if a!=b:
                net2[(i, j)].append((i-1, j))
            if b!=c:
                net2[(i, j)].append((i, j-1))
            if c!=d:
                net2[(i, j)].append((i+1, j))
        borders = 0
        while net2:
            s = min(net2)
            p = s
            n = net2[s][0]
            net2[s].remove(n)
            
            borders += 1
            while not n==s:
                pi, pj = p
                ni, nj = n
                net2[n].remove(p)
                if len(net2[n])!=1:
                    a = (ni + nj-pj, nj + ni-pi)
                else:
                    a = (ai, aj) = net2[n][0]
                net2[n].remove(a)
                if len(net2[n])==0:
                    del net2[n]
                if not((abs(ni-pi)==abs(ai-ni)==1) or (abs(nj-pj)==abs(aj-nj)==1)):
                    borders += 1
                p = n
                n = a
            del net2[n]
        yield len(region), borders
                
                
data = open("input.txt").read()

print(sum(a*b for a, b in regions(make_field(data))))

print(sum(a*b for a, b in sides(make_field(data))))

import cProfile
cProfile.run('sum(a*b for a, b in sides(make_field(data)))')
