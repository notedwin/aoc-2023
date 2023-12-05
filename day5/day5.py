import os
from collections import defaultdict

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day5_test.txt")


cards = defaultdict(lambda: 1)


seeds = []
seed2soil = {}
soil2fert = {}
fert2water = {}
water2light = {}
light2temp = {}
temp2hum = {}
hum2loc = {}


sections = 0


def line2dict(line, d):
    nums = [int(x) for x in line.split()]
    for idx, src in enumerate(range(nums[1], nums[1] + nums[2])):
        # print(f"chaning d[{src} to {nums[0]} + {nums[2]}]")
        d[src] = nums[0] + idx


def fill(d):
    keys = d.keys()

    def num_exists(num):
        return num not in keys

    for num in filter(num_exists, range(100)):
        d[num] = num


# we can optimze later and only look at ranges containing one of the inital seeds
with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        if line == "\n":
            if sections == 1:
                fill(seed2soil)
            if sections == 2:
                fill(soil2fert)
            if sections == 3:
                fill(fert2water)
            if sections == 4:
                fill(water2light)
            if sections == 5:
                fill(light2temp)
            if sections == 6:
                fill(temp2hum)
            if sections == 7:
                fill(hum2loc)

            sections += 1
            continue

        if sections == 0:
            seeds = line.split("seeds:")[1].split()

        if sections == 1:
            if line[:1].isalpha():
                continue
            line2dict(line, seed2soil)

        if sections == 2:
            if line[:1].isalpha():
                continue
            line2dict(line, soil2fert)

        if sections == 3:
            if line[:1].isalpha():
                continue
            line2dict(line, fert2water)

        if sections == 4:
            if line[:1].isalpha():
                continue
            line2dict(line, water2light)

        if sections == 5:
            if line[:1].isalpha():
                continue
            line2dict(line, light2temp)

        if sections == 6:
            if line[:1].isalpha():
                continue
            line2dict(line, temp2hum)

        if sections == 7:
            if line[:1].isalpha():
                continue
            line2dict(line, hum2loc)

print(hum2loc)


r = min(
    hum2loc[
        temp2hum[light2temp[water2light[fert2water[soil2fert[seed2soil[int(seed)]]]]]]
    ]
    for seed in seeds
)
print(r)
