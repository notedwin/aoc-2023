d = {"red": 12, "green": 13, "blue": 14}

file_ = "day3.txt"

arr = []
with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        arr.append(list(line)[:-1])

print("\n".join(["".join([item for item in row]) for row in arr]))


def check_up(line_idx, idx, num=None):
    if line_idx + 1 < len(arr):
        ele = arr[line_idx + 1][idx]
        if num:
            print(num, ele)
        if ele != ".":
            return True

    if line_idx - 1 >= 0:
        ele = arr[line_idx - 1][idx]
        if num:
            print(num, ele)
        if ele != ".":
            return True
    return False


def check(line_idx, r_idx, num):
    l_idx = r_idx - len(num)

    for num_idx in range(l_idx, r_idx):
        # print(num_idx)
        if num_idx == l_idx:
            if check_up(
                line_idx,
                num_idx,
                num=num
                if num
                in ("101", "161", "3", "308", "398", "424", "5", "511", "694", "7")
                else None,
            ):
                return True

            if l_idx - 1 >= 0:
                if arr[line_idx][num_idx - 1] != ".":
                    return True
                if check_up(
                    line_idx,
                    num_idx - 1,
                    num=num
                    if num
                    in ("101", "161", "3", "308", "398", "424", "5", "511", "694", "7")
                    else None,
                ):
                    return True

        elif num_idx == r_idx - 1:
            if check_up(
                line_idx,
                num_idx,
                num=num
                if num
                in ("101", "161", "3", "308", "398", "424", "5", "511", "694", "7")
                else None,
            ):
                return True

            if r_idx + 1 < len(arr[line_idx]):
                if arr[line_idx][num_idx + 1] != ".":
                    return True

                if check_up(
                    line_idx,
                    num_idx + 1,
                    num=num
                    if num
                    in ("101", "161", "3", "308", "398", "424", "5", "511", "694", "7")
                    else None,
                ):
                    return True
        else:
            if check_up(
                line_idx,
                num_idx,
                num=num
                if num
                in ("101", "161", "3", "308", "398", "424", "5", "511", "694", "7")
                else None,
            ):
                return True

        # print(num_idx)
    return False


s = 0
# print(arr)
with open("output.txt", "w") as f:
    for l_idx, line in enumerate(arr):
        num = ""
        for idx, c in enumerate(line):
            # print(c)
            if c.isdigit():
                num += c
            else:
                if num:
                    # print("check for", num)

                    if check(l_idx, idx, num):
                        f.write(num + "\n")
                        s += int(num)
                num = ""

# 118 right and down should have worked

print(s)
