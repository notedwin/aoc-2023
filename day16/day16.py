import os

# \
f_slash = {(0, 1): (-1, 0), (0, -1): (1, 0), (-1, 0): (0, -1), (1, 0): (0, 1)}

# /
b_slash = {(0, 1): (1, 0), (0, -1): (-1, 0), (-1, 0): (0, 1), (1, 0): (0, -1)}

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")

seen = None
arr = None


def traverse(start, direction):
    r, c = start
    print(arr)
    need = []
    while r >= 0 and c >= 0 and r < len(arr) and c < len(arr[0]):
        ele = arr[r][c]
        if ele == "\\":
            direction = f_slash[direction]
        elif ele == "/":
            direction = b_slash[direction]
        elif ele == "|" and direction in [(0, 1), (0, -1)]:
            direction = (1, 0)
            # need (-1, 0)
        elif ele == "-" and direction in [(1, 0), (-1, 0)]:
            direction = (0, 1)
            # 0, -1
        print(r, c, arr[r][c], direction)
        seen[r][c] = True
        r += direction[0]
        c += direction[1]


def task1(file_):
    with open(file_, "r") as f:
        global arr
        arr = [line.replace("\n", "") for line in f.readlines()]
    global seen
    seen = [[False] * len(arr[0])] * len(arr)
    start = (0, 0)
    direction = (0, 1)
    traverse(start, direction)


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == None
# print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 2
# print(task2(f"{file_}.txt"))
