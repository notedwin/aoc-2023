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

count = 0
a_nodes = [key for key in network.keys() if key[-1] == "A"]
traveled = {}

while any(node[-1] != "Z" for node in a_nodes):
    # print(a_nodes)
    direction = path_order.pop(0)
    path_order.append(direction)
    for idx, node in enumerate(a_nodes):
        a_nodes[idx] = network[node][d[direction]]
    if tuple(a_nodes) in traveled:
        # print(traveled)
        break
    count += 1
    traveled[tuple(a_nodes)] = 1

print(count)
