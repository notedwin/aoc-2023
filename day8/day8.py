import math
import os

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day8.txt")

path_order = None

d = {"L": 0, "R": 1}
network = {}

with open(file_, "r") as f:
    for idx, line in enumerate(f.readlines()):
        line = line.replace("\n", "")

        if idx == 0:
            path_order = list(line)
            continue

        (cur, loc) = line.replace("(", "").replace(")", "").split("=")
        loc = [c.strip() for c in loc.split(",")]
        cur = cur.strip()

        network[cur] = loc

a_nodes = [key for key in network.keys() if key[-1] == "A"]
all_steps = []

for node in a_nodes:
    count = 0
    while node[-1] != "Z":
        print(node)
        direction = path_order[count % len(path_order)]
        node = network[node][d[direction]]
        count += 1
    all_steps.append(count)

print(math.lcm(*all_steps))
