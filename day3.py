d = {"red": 12, "green": 13, "blue": 14}

file_ = "day3_test.txt"

arr = []
with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        arr.append(list(line)[:-1])


def check(line_idx, r_idx, len_):
    l_idx = r_idx - len_
    # print(line_idx, l_idx, r_idx)

    moves = [(-1, -1), (-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (0, 1), (1, 1)]

    for move in moves:
        if line_idx + move[0] < 0 or line_idx + move[0] > len(arr):
            continue

        rvalue = "."
        if r_idx + move[1] > 0 and r_idx + move[1] < len(arr[line_idx]):
            rvalue = arr[line_idx + move[0]][r_idx + move[1]]

        lvalue = "."
        if l_idx + move[1] > 0 and l_idx + move[1] < len(arr[line_idx]):
            rvalue = arr[line_idx + move[0]][l_idx + move[1]]

        # print(
        #     f"moving {move[0],move[1]} for line: arr[{line_idx}]][{r_idx + move[1], l_idx + move[1]}]"
        # )
        # print(rvalue, lvalue)
        if rvalue != "." and not rvalue.isdigit():
            return True
        if lvalue != "." and not lvalue.isdigit():
            return True

    return False

    # if l_idx == 0 and move[0] == -1:
    #     # remove moves with -1 in y
    #     continue
    # if left_idx == 0 and move[1] == -1:
    #     # remove moves with -1 in x
    #     continue
    # if r_idx == len(arr[l_idx]) and move[1] == 1:
    #     # removes moves with 1 in x
    #     continue
    # if l_idx == len(arr) and move[0] == 1:
    #     # remove moves with 1 in y
    #     continue

    # new = r_idx if moves[1] == 1 else left_idx
    #

    # print(f"checking value {value}")
    # if value != ".":
    #     print("valid")
    #     return True
    # return False


s = 0
# print(arr)
for l_idx, line in enumerate(arr):
    num = ""
    for idx, c in enumerate(line):
        # print(c)
        if c.isdigit():
            num += c
        else:
            if num:
                # print("check for", num)
                if check(l_idx, idx, len(num)):
                    print(f"valid: {num}")
                    s += int(num)
            num = ""

print(s)
