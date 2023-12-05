# # part 1
# s = 0
# with open("day1.txt", "r") as f:
#     for line in f.readlines():
#         num = ""
#         digit = None
#         for c in line:
#             if c.isdigit():
#                 if not digit:
#                     num += c
#                 digit = c
#         num += digit
#         s += int(num)

# print(s)

# part 2
d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
# if we find a letter that isn't in
s = 0
with open("day1.txt", "r") as f:
    for line in f.readlines():
        num = ""
        digit = None
        word = ""
        for c in line:
            if c.isdigit():
                if not digit:
                    num += c
                digit = c
            else:
                word += c
                if word in d:
                    # first digit
                    if not digit:
                        num += str(d[word])
                    # otherwise set digit to num
                    digit = str(d[word])
                    # reuse last char
                    word = c
                else:
                    # for every word
                    for key in d:
                        # check if word can be found in str
                        if key in word:
                            # check if first num
                            if not digit:
                                num += str(d[key])
                            # keep track of digits seen
                            digit = str(d[key])
                            # reuse last char
                            word = c

        num += digit
        s += int(num)

print(s)
