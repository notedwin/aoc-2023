import os

pwd = os.path.dirname(__file__)
folder_name = os.path.basename(pwd)
file_ = os.path.join(pwd, f"{folder_name}")


def string2hash(s):
    current_value = 0
    for ch in s:
        ascii_num = ord(ch)
        current_value += ascii_num
        current_value *= 17
        current_value = current_value % 256
    return current_value


def task1(file_):
    with open(file_, "r") as f:
        line = f.readlines()[0].split(",")
        sum_ = sum(string2hash(s) for s in line)
        return sum_


def task2(file_):
    boxes = {}
    with open(file_, "r") as f:
        line = f.readlines()[0].split(",")
        for op in line:
            if "=" in op:
                (s, num) = op.split("=")
                current_value = string2hash(s)
                if current_value in boxes:
                    found = False
                    for idx, val in enumerate(boxes[current_value]):
                        if s[:2] == val[:2]:
                            found = True
                            boxes[current_value][idx] = op
                    if not found:
                        boxes[current_value].append(op)
                else:
                    boxes[current_value] = [op]
            else:
                s = op.split("-")[0]
                current_value = string2hash(s)
                if current_value in boxes:
                    for idx, val in enumerate(boxes[current_value]):
                        if s[:2] == val[:2]:
                            del boxes[current_value][idx]
            # print(boxes)

    total = 0
    for k, box in boxes.items():
        box_num = k + 1
        total += sum(
            (idx + 1) * box_num * (int(v.split("=")[1])) for idx, v in enumerate(box)
        )
    return total


assert task1(f"{file_}_test.txt") == 1320
print(task1(f"{file_}.txt"))

assert task2(f"{file_}_test.txt") == 145
print(task2(f"{file_}.txt"))
