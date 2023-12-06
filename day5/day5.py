import heapq
import os

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day5_test.txt")

seeds = []
soil_range = []
seed2soil = {}
soil2fert = {}
fert2water = {}
water2light = {}
light2temp = {}
temp2hum = {}
hum2loc = {}


sections = 0


def find_overlap_and_non_overlap(ranges):
    starts, ends = zip(*ranges)
    overlap = range(max(starts), min(ends) + 1)
    if not overlap:
        return ([], range(min(starts), max(ends) + 1), [])

    less_non_overlap = range(*heapq.nsmallest(2, starts))
    end, start = heapq.nlargest(2, ends)
    greater_non_overlap = range(start + 1, end + 1)
    return (overlap, less_non_overlap, greater_non_overlap)


def seed_fn(line):
    # seed 2 soil
    nums = [int(x) for x in line.split()]
    print(f"line: {nums}, looking for: {seeds}")

    for idx in range(0, len(seeds), 2):
        start_seed = seeds[idx]
        end_seed = seeds[idx] + seeds[idx + 1]

        start_map = nums[1]
        end_map = nums[1] + nums[2]

        start = max(start_seed, start_map)
        end = min(end_map, end_seed)

        # r = find_overlap_and_non_overlap([(start_seed, end_seed), (start_map, end_map)])
        # print(r)

        if start < end:
            diff = nums[0] - nums[1]
            soil_range.append(start + diff)
            soil_range.append(end - start + diff)
        # if overlap range starts at map, the we missed the first values
        # if start == start_map:
        #     soil_range.append(start_seed)
        #     soil_range.append(start_map - start_seed)
        #     # print(start_seed, start_map)
        # if end == end_map:
        #     soil_range.append(end_map)
        #     soil_range.append(end_seed - end_map)
        # print(end_seed, end_map)


def missing():
    # after we have gone all the oveerlaps, we can go back and find the

    for idx in range(0, len(seeds), 2):
        for idx_2 in range(0, len(soil_range), 2):
            start_seed = seeds[idx]
            end_seed = seeds[idx] + seeds[idx + 1]

            start_overlap = soil_range[idx]
            end_overlap = soil_range[idx] + soil_range[idx + 1]

            start = max(start_seed, start_overlap)
            end = min(end_overlap, end_seed)

            if start == start_overlap:
                soil_range.append(start_seed)
                soil_range.append(start_overlap - start_seed)
                # print(start_seed, start_overlap)
            if end == end_overlap:
                soil_range.append(end_overlap)
                soil_range.append(end_seed - end_overlap)


with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        if line == "\n":
            print(soil_range)
            seeds = soil_range
            soil_range = None
            sections += 1
            continue

        if sections == 0:
            seeds = [int(v) for v in line.split("seeds:")[1].split()]
            sections += 1

        if sections == 1:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 2:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 3:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 4:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 5:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 6:
            if line[:1].isalpha():
                continue
            seed_fn(line)

        if sections == 7:
            if line[:1].isalpha():
                continue
            seed_fn(line)

m = float("inf")
