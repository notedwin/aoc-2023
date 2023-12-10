import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(os.getcwd())
file_ = os.path.join(pwd, f"{folder_name}")


def task1(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


def task2(file_):
    with open(file_, "r") as f:
        for idx, line in enumerate(f.readlines()):
            line = line.replace("\n", "")
            print(line)


assert task1(f"{file_}_test.txt") == 114
print(task1(f"{file_}.txt"))

assert task2(f"{file_}_test.txt") == 2
print(task2(f"{file_}.txt"))
