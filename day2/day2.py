# part 1
# d = {"red": 12, "green": 13, "blue": 14}

# with open("day2.txt", "r") as f:
#     games = 0
#     for line in f.readlines():
#         (game, blocks) = line.split(":")

#         valid = True

#         for block in blocks.split(";"):
#             for pulled in block.split(","):
#                 (num_blocks, color) = pulled.split()
#                 if d[color] < int(num_blocks):
#                     print(f"too many {color}: {num_blocks}")
#                     valid = False
#                     break
#             if not valid:
#                 break
#         if valid:
#             games += int(game.split()[1])

#         print(games)

from collections import defaultdict
from functools import reduce

d = {"red": 12, "green": 13, "blue": 14}


with open("day2.txt", "r") as f:
    sum_ = 0
    for line in f.readlines():
        (game, blocks) = line.split(":")
        d = defaultdict(int)

        for block in blocks.split(";"):
            for pulled in block.split(","):
                (num_blocks, color) = pulled.split()

                d[color] = max(d[color], int(num_blocks))
        sum_ += reduce(lambda x, y: x * y, d.values())

print(sum_)
