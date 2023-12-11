import itertools
import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def expand(arr):
    dups = []
    for idx, row in enumerate(arr):
        if all(e == "." for e in row):
            dups.append(idx)

    for r_idx in dups:
        arr.insert(r_idx, ["."] * len(arr[0]))

    dups = []
    for col_idx in range(len(arr[0])):
        if all(arr[idx][col_idx] == "." for idx in range(len(arr))):
            dups.append(col_idx)

    for idx, row in enumerate(arr):
        for c_idx in dups:
            arr[idx].insert(c_idx, ".")

    return arr


def sum_pairs(arr):
    # find every galaxy
    d = []

    for ridx, row in enumerate(arr):
        for cidx, col in enumerate(row):
            if col == "#":
                d.append((ridx, cidx))
    s = 0
    # print(len(list(itertools.combinations(d, 2))))
    for g in itertools.combinations(d, 2):
        dis = abs(g[0][0] - g[1][0]) + abs(g[0][1] - g[1][1])
        s += dis - 1
        # dist = math.dist(g[0], g[1])
        # print(g, dis - 1)

    print(s)

    # for prev, cur in zip(d, d[1:]):
    #     dist = math.dist(prev, cur)
    #     print(prev, cur, dist)

    # sum_ = sum([math.dist(prev, cur) for prev, cur in zip(d, d[1:])])

    # print(sum_)


def task1(file_):
    arr = []
    with open(file_, "r") as f:
        arr = [list(line[0:-1]) for line in f.readlines()]
    # print("\n".join(map(lambda b: "".join(map(str, b)), arr)))
    arr = expand(arr)
    print("\n".join(map(lambda b: "".join(map(str, b)), arr)))
    sum_pairs(arr)


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == 374
# print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 2
# print(task2(f"{file_}.txt"))
