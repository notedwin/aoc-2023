import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def total_load(arr):
    s = 0

    for idx in range(len(arr[0])):
        col = [row[idx] for row in arr]
        last_rock = 0
        rocks_fallen = 0
        idx = 0
        len_col = len(col)
        print(col)
        while idx < len_col:
            if col[idx] == "O":
                rocks_fallen += 1
            elif col[idx] == "#":
                e = [len_col - x for x in range(last_rock, last_rock + rocks_fallen)]
                s += sum(e)
                if e:
                    print(e)
                rocks_fallen = 0
                last_rock = idx + 1
            idx += 1
        e = [len_col - x for x in range(last_rock, last_rock + rocks_fallen)]
        s += sum(e)
        if e:
            print(e)
    print(s)
    return s


def task1(file_):
    arr = None
    with open(file_, "r") as f:
        arr = [list(line[0:-1]) for line in f.readlines()]
    return total_load(arr)


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == 136
print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 64
# print(task2(f"{file_}.txt"))
