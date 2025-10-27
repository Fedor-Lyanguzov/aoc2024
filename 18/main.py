from collections import deque

with open("input") as f:
    data = f.read().strip().split("\n")
    data = list(map(lambda x: list(map(int, x.split(","))), data))


def make_field(data, w=71, h=71):
    field = [["."] * (w + 2) for _ in range(h + 2)]
    for i, j in data:
        field[i + 1][j + 1] = "#"
    for i in range(w + 2):
        field[0][i] = "#"
        field[h + 1][i] = "#"
    for i in range(h + 2):
        field[i][0] = "#"
        field[i][w + 1] = "#"
    return field


def part1(field):
    w = len(field[0])
    h = len(field)
    scores = [[float("+inf")] * w for _ in range(h)]
    scores[1][1] = 0
    q = deque([(1, 2), (2, 1)])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        i, j = q.popleft()
        if scores[i][j] == float("+inf") and field[i][j] != "#":
            m = min(scores[i + di][j + dj] for di, dj in d)
            scores[i][j] = m + 1
            for di, dj in d:
                if (
                    scores[i + di][j + dj] == float("+inf")
                    and field[i + di][j + dj] != "#"
                ):
                    q.append((i + di, j + dj))

    return scores


def print_field(scores, field):
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == "#":
                print("#", end="")
            elif scores[i][j] == float("+inf"):
                print("i", end="")
            else:
                print(".", end="")
        print()


field = make_field(data[:1024])
# print_field(part1(field), field)
print(part1(field)[-2][-2])
