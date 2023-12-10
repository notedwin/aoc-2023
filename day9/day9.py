import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def find_pattern(line):
    return [cur - prev for prev, cur in zip(line, line[1:])]


def task1(file_):
    tot = 0
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = [int(e) for e in line.split()]

            diff = find_pattern(line)
            diffs = [line, diff]
            while any(diff[0] != d for d in diff):
                diff = find_pattern(diff)
                diffs.append(diff)
            next_add = 0
            # print(line)
            for row in reversed(diffs):
                if all(e == row[0] for e in row):
                    next_add = row[0]
                    continue
                next_add = row[-1] + next_add
            tot += next_add
    return tot


def task2(file_):
    tot = 0
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = [int(e) for e in line.split()]

            diff = find_pattern(line)
            diffs = [line, diff]
            while any(diff[0] != d for d in diff):
                diff = find_pattern(diff)
                diffs.append(diff)
            next_add = 0
            print(line)
            for row in reversed(diffs):
                if all(e == row[0] for e in row):
                    next_add = row[0]
                    continue
                next_add = row[0] - next_add
            tot += next_add
    return tot


assert task1(f"{file_}_test.txt") == 114
print(task1(f"{file_}.txt"))

assert task2(f"{file_}_test.txt") == 2
print(task2(f"{file_}.txt"))
