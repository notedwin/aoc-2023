import os
from collections import deque

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


d = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, 1), (1, 0)],
    "J": [(0, 1), (-1, 0)],
    "7": [(0, -1), (-1, 0)],
    "F": [(0, -1), (1, 0)],
    ".": [],
}


def find_S(arr):
    for r_idx, row in enumerate(arr):
        for c_idx, col in enumerate(row):
            if col == "S":
                return (r_idx, c_idx)


def isValid(arr, visited, row, col):
    # If cell lies out of bounds
    if row < 0 or col < 0 or row >= 5 or col >= 5:
        return False

    # If cell is already visited
    if visited[row][col]:
        return False

    if arr[row][col] == ".":
        return False

    # Otherwise
    return True


def bfs(arr, start):
    visited = [[False for i in range(len(arr[0]))] for i in range(len(arr))]
    q = deque()

    dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    (x, y) = start
    visited[x][y] = True

    for dx, dy in dir_:
        new_x = x + dx
        new_y = y + dy

        if isValid(arr, visited, new_x, new_y):
            print(new_x, new_y, arr[new_x][new_y])
            for dx2, dy2 in d[arr[new_x][new_y]]:
                new_x = x + dx2
                new_y = y + dy2
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
        visited[new_x][new_y] = True

    while q:
        (x, y) = q.popleft()
        v = arr[x][y]
        print("\n".join(map(lambda b: " ".join(map(str, b)), visited)))
        print(x, y, v)

        if d[v]:
            for dx, dy in d[v]:
                new_x = x + dx
                new_y = y + dy
                if isValid(arr, visited, new_x, new_y):
                    # check also if they connect validly
                    q.append((new_x, new_y))
                visited[new_x][new_y] = True


def task1(file_):
    arr = []
    with open(file_, "r") as f:
        arr = [list(line) for line in f.readlines()]

    print("".join(map(lambda b: "".join(map(str, b)), arr)))
    print("_____________________________")
    start = find_S(arr)
    ret = bfs(arr, start)


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == None
# print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 4
# print(task2(f"{file_}.txt"))
