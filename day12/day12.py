import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def task1(file_):
    uniq = 0
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            (springs, goal) = line.replace("\n", "").split()
            target = ""
            for num in goal.split(","):
                target += "#" * int(num)
                target += "."
            target = target[:-1]
            print(target, len(target), len(springs))


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == None  # 21
# print(task1(f"{file_}.txt"))

# assert task2(f"{file_}_test.txt") == 2
# print(task2(f"{file_}.txt"))
