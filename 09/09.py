



data = open("input.txt").read().strip()
def f(data):
    data = list(map(int, data))

    nl = 1
    nr = len(data)//2
    l = data[0]
    s = data[0]*0
    i = 1
    j = -1
    while i<len(data)+j:
        if data[i]<=data[j]:
            s += sum(range(l, l+data[i]))*nr
            l += data[i]
            data[j] -= data[i]
            i += 1
            s += sum(range(l, l+data[i]))*nl
            l += data[i]
            nl += 1
            i += 1
        else:
            s += sum(range(l, l+data[j]))*nr
            l += data[j]
            nr -= 1
            data[i] -= data[j]
            j -= 2
    return s

print(f(data))

def fat(data):
    "FAT - File Allocation Table"
    data = list(map(int, data))

    files = []
    emptys = []
    l = 0
    n = 0
    for i in range(len(data)):
        if i%2==0:
            files.append((n, l, l+data[i]))
            n += 1
        else:
            emptys.append((l, l+data[i]))
        l += data[i]
    return files, emptys

def f2(files, emptys):
    for i in reversed(range(len(files))):
        n, s, e = files[i]
        j = 0
        l, r = emptys[0]
        while not (j==len(emptys) or e-s<=r-l or s<l):
            j += 1
            l, r = emptys[j]
        if e-s<=r-l:
            files[i] = (n, l, l+e-s)
            emptys[j] = (l+e-s, r)
    return sum(n*(sum(range(s, e))) for n, s, e in files)

assert f2(*fat("2333133121414131402"))==2858

print(f2(*fat(data)))
