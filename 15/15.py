test_input = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip()


def parse(input):
    m, c = input.split("\n\n")
    c = "".join(c.split("\n"))
    m = list(map(list, m.split("\n")))
    return m, c


d = {"v": (1, 0), "^": (-1, 0), "<": (0, -1), ">": (0, 1)}


def gps(c):
    i, j = c
    return i * 100 + j


def start(m):
    for i, row in enumerate(m):
        for j, ch in enumerate(row):
            if ch == "@":
                return i, j
    raise ValueError("no start position")


def boxes(m):
    for i, row in enumerate(m):
        for j, ch in enumerate(row):
            if ch == "O":
                yield i, j


def field(m):
    return "\n".join("".join(y for y in x) for x in m)


def part1(m, c):
    ri, rj = start(m)
    # print("1", ri, rj)
    for ch in c:
        di, dj = d[ch]
        # print("2", di, dj)
        move = True
        ci = ri + di
        cj = rj + dj
        while move and m[ci][cj] != ".":
            if m[ci][cj] == "#":
                move = False
            ci += di
            cj += dj
        # print("3", move, ci, cj)
        if move:
            m[ci][cj] = m[ri + di][rj + dj]
            m[ri + di][rj + dj] = "@"
            m[ri][rj] = "."
            ri = ri + di
            rj = rj + dj
            # print(field(m))
    return sum(map(gps, boxes(m)))


print(part1(*parse(open("input").read())))
