import re

pattern = re.compile(r'''
Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)
'''.strip(), re.MULTILINE)


data = open("input.txt").read().strip().split("\n\n")
data = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''.strip().split("\n\n")

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
            print("@0", n, s1&s2)
            s += tok(min(s1&s2, key=tok))
    return s


def f2(data):
    s = 0
    for i, (xa, ya, xb, yb, xt, yt) in enumerate(data):
        print(f'@1 {i} {xa=}, {ya=}, {xb=}, {yb=}, {xt=}, {yt=}')
        #xt += 10_000_000_000_000
        #yt += 10000000000000
        b = 0
        a = 0
        al = 0
        ar = max(xt//xa+1, yt//ya+1)
        while ar-al>1:
            am = (ar+al)//2
            bl = 0
            br = max(xt//xb+1, yt//yb+1)
            f = False
            while br-bl>1:
                bm = (bl+br)//2
                if xa*am+xb*bm>xt and ya*am+yb*bm>xt:
                    br = bm
                elif xa*am+xb*bm<xt and ya*am+yb*bm<xt:
                    bl = bm
                elif xa*am+xb*bm==xt and ya*am+yb*bm==xt:
                    f = True
                    b = bm
                    break
                else:
                    break
            print(al, ar)
            if f:
                a = am
                ar = am
            else:
                if a>3*br:
                    al = am
                else:
                    ar = am
        print('@end', a, b, a*3+b)
        s += a*3+b
    return s
print(f(data))
print(f2(data))
