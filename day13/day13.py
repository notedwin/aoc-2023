import os
from itertools import groupby

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def find_inflection(arr):
    possible = []
    for idx, (prev, cur) in enumerate(zip(arr, arr[1:])):
        if cur == prev:
            possible.append(idx + 1)

    for mid in possible:
        print("found matching row\n")

        good = True

        l = mid - 1
        r = mid
        while l >= 0 and r < len(arr):
            if arr[l] != arr[r]:
                good = False
                break
            l -= 1
            r += 1

        if good:
            print(f"valid row: {mid}")
            return mid * 100

    possible = []

    for idx in range(len(arr[0]) - 1):
        l = [row[idx] for row in arr]
        r = [row[idx + 1] for row in arr]
        if l == r:
            possible.append(idx + 1)

    for mid in possible:
        good = True
        l = mid - 1
        r = mid

        while l >= 0 and r < len(arr[0]):
            arrl = [row[l] for row in arr]
            arrr = [row[r] for row in arr]

            print(arrl, arrr)

            if arrl != arrr:
                good = False
                break
            l -= 1
            r += 1

        if good:
            print(f"valid col: {mid}")
            return mid

    return 0


def task1(file_):
    with open(file_, "r") as f:
        groups = [
            list(g)
            for k, g in groupby(map(str.strip, f), key=lambda line: line != "")
            if k
        ]

    s = 0
    for group in groups:
        s += find_inflection(group)
    print(s)
    return s


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == 405
print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 2
# print(task2(f"{file_}.txt"))
