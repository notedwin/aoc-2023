import os

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day5.txt")

seeds = []
seed2soil = {}
soil2fert = {}
fert2water = {}
water2light = {}
light2temp = {}
temp2hum = {}
hum2loc = {}


sections = 0


def line2dict(line, d, values):
    nums = [int(x) for x in line.split()]

    for value in values:
        num = int(value)

        if nums[1] <= num < nums[1] + nums[2]:
            diff = nums[0] - nums[1]
            d[num] = num + diff


look = None
with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        if line == "\n":
            # print(look)
            match sections:
                case 1:
                    look = [seed2soil.get(int(seed), int(seed)) for seed in seeds]
                case 2:
                    look = [soil2fert.get(v, v) for v in look]
                case 3:
                    look = [fert2water.get(v, v) for v in look]
                case 4:
                    look = [water2light.get(v, v) for v in look]
                case 5:
                    look = [light2temp.get(v, v) for v in look]
                case 6:
                    look = [temp2hum.get(v, v) for v in look]
            sections += 1
            continue

        if sections == 0:
            seeds = line.split("seeds:")[1].split()

        if sections == 1:
            if line[:1].isalpha():
                continue
            line2dict(line, seed2soil, seeds)

        if sections == 2:
            if line[:1].isalpha():
                continue
            line2dict(line, soil2fert, look)

        if sections == 3:
            if line[:1].isalpha():
                continue
            line2dict(line, fert2water, look)

        if sections == 4:
            if line[:1].isalpha():
                continue
            line2dict(line, water2light, look)

        if sections == 5:
            if line[:1].isalpha():
                continue
            line2dict(line, light2temp, look)

        if sections == 6:
            if line[:1].isalpha():
                continue
            line2dict(line, temp2hum, look)

        if sections == 7:
            if line[:1].isalpha():
                continue
            line2dict(line, hum2loc, look)

m = float("inf")
look = [hum2loc.get(v, v) for v in look]
print(min(look))
