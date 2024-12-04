
d = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i==j==0]
p = {"MSMS", "MSSM", "SMMS", "SMSM"}

def f(i, j, w, di, dj):
    if len(w)==0:
        return True
    if data[i][j]!=w[0]:
        return False
    return f(i+di, j+dj, w[1:], di, dj)

data = open("input.txt").read().strip().split("\n")

assert len(set(len(x) for x in data))==1

for i in range(len(data)):
    data[i] = '.'+data[i]+'.'
data.append('.'*(len(data[0])+2))
data.insert(0, '.'*len(data[0]))

xs = [(i, j) for i in range(len(data[0])) for j in range(len(data)) if data[i][j]=='X']
print(sum(1 for i, j in xs for di, dj in d if f(i, j, 'XMAS', di, dj)))

As = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j]=="A"]
cs = [(data[i-1][j-1], data[i+1][j+1], data[i-1][j+1], data[i+1][j-1]) for i, j in As]
print(sum(1 for x in cs if ''.join(x) in p))
