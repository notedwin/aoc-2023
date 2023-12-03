d = {"red": 12, "green": 13, "blue": 14}

file_ = "day3_test.txt"

arr = []
with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        arr.append(list(line)[:-1])


def check(line_idx, r_idx, len_, num):
    l_idx = r_idx - len_
    # print(num, line_idx, l_idx, r_idx)
    # print(list(range(l_idx, r_idx)))
    for num_idx in range(l_idx, r_idx):
        # print(num_idx)
        if num_idx == l_idx:
            # check up down left + diags
            if line_idx + 1 < len(arr):
                if arr[line_idx + 1][num_idx] != ".":
                    return True

            if line_idx - 1 >= 0:
                if arr[line_idx - 1][num_idx] != ".":
                    return True

            if l_idx - 1 >= 0:
                if arr[line_idx][l_idx - 1] != ".":
                    return True

                if line_idx - 1 >= 0:
                    if arr[line_idx - 1][num_idx - 1] != ".":
                        return True

                if line_idx + 1 < len(arr):
                    if arr[line_idx + 1][num_idx - 1] != ".":
                        return True

        elif num_idx == r_idx - 1:
            # check up down right
            # print(
            #     arr[line_idx][num_idx + 1],
            #     arr[line_idx + 1][num_idx + 1],
            # )

            if line_idx + 1 < len(arr):
                if arr[line_idx + 1][num_idx] != ".":
                    return True

            if line_idx - 1 >= 0:
                if arr[line_idx - 1][num_idx] != ".":
                    return True

            if r_idx + 1 < len(arr[line_idx]):
                if arr[line_idx][num_idx + 1] != ".":
                    return True

                if line_idx + 1 < len(arr):
                    if arr[line_idx + 1][num_idx + 1] != ".":
                        return True

                if line_idx - 1 >= 0:
                    if arr[line_idx - 1][num_idx + 1] != ".":
                        return True

        else:
            # check up and down
            if line_idx + 1 < len(arr):
                if arr[line_idx + 1][num_idx] != ".":
                    return True

            if line_idx - 1 >= 0:
                if arr[line_idx - 1][num_idx] != ".":
                    return True

        # print(num_idx)
    return False

    # moves = [(-1, -1), (-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (0, 1), (1, 1)]

    # for move in moves:
    #     if line_idx + move[0] < 0 or line_idx + move[0] > len(arr):
    #         continue

    #     rvalue = "."
    #     if r_idx + move[1] > 0 and r_idx + move[1] < len(arr[line_idx]):
    #         rvalue = arr[line_idx + move[0]][r_idx + move[1]]

    #     lvalue = "."
    #     if l_idx + move[1] > 0 and l_idx + move[1] < len(arr[line_idx]):
    #         rvalue = arr[line_idx + move[0]][l_idx + move[1]]

    #     # print(
    #     #     f"moving {move[0],move[1]} for line: arr[{line_idx}]][{r_idx + move[1], l_idx + move[1]}]"
    #     # )
    #     # print(rvalue, lvalue)
    #     if rvalue != "." and not rvalue.isdigit():
    #         return True
    #     if lvalue != "." and not lvalue.isdigit():
    #         return True

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
                if check(l_idx, idx, len(num), num):
                    print(f"valid: {num}")
                    s += int(num)
            num = ""

print(s)
