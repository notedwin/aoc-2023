from collections import defaultdict

file_ = "day4.txt"

points = 0
d = []
cards = defaultdict(lambda: 1)


with open(file_, "r") as f:
    for line in f.readlines():
        arrs = [group.split() for group in line.split(":")[1].split("|")]
        d.append(len(list(set(arrs[0]) & set(arrs[1]))))
    # print(d)
    for idx, ele in enumerate(d):
        points += cards[idx]

        for c_idx in range(idx + 1, idx + d[idx] + 1):
            cards[c_idx] += cards[idx]
    # print(cards)

print(points)
