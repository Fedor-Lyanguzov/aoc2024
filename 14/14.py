from math import prod



data = open("input.txt").read().strip().split("\n")
w = 101
h = 103

def robot(r):
    'p=0,4 v=3,-3'
    p, v = r.split()
    return tuple(map(int, p[2:].split(',')+v[2:].split(',')))
robots = [robot(r) for r in data]


def bound(a, m):
    return a%m
bound_x = lambda x: bound(x, w)
bound_y = lambda x: bound(x, h)

def step(robots):
    return [(bound_x(x+vx), bound_y(y+vy), vx, vy) for x, y, vx, vy in robots]

def quadrants(robots):
    res = [[] for _ in range(4)]
    for x, y, _, _ in robots:
        if x==w//2 or y==h//2:
            pass
        elif x<w//2 and y<h//2:
            res[0].append((x,y))
        elif x>w//2 and y<h//2:
            res[1].append((x,y))
        elif x<w//2 and y>h//2:
            res[2].append((x,y))
        elif x>w//2 and y>h//2:
            res[3].append((x,y))
    return res

def part1(robots):
    for _ in range(100):
        robots = step(robots)
    return prod(map(len, quadrants(robots)))

def print_robots(r):
    t = [[' ']*w for _ in range(h)]
    for x, y, _, _ in robots:
        t[y][x] = '*'
    print('\n'.join(''.join(x for x in y) for y in t))

def difference(q1, q2):
    q2 = [(w-1-x, y) for x, y in q2]
    return len(set.difference(set(q1), set(q2)))

def part2(robots):
    i = 0
    print_robots(robots)
    while not input("next?"):
        same = False
        while not same:
            robots = step(robots)
            i += 1
            r = quadrants(robots)
            same = difference(r[0], r[1])<30
        print(difference(r[0], r[1]))
        print_robots(robots)
    return i
p2 = part2(robots)
print(part1(robots))
print(p2)
