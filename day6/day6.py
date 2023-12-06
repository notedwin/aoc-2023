import os

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day6.txt")

with open(file_, "r") as f:
    arr = f.readlines()
    time = int("".join(arr[0].split("Time:")[1].split()))
    max_dist = int("".join(arr[1].split("Distance:")[1].split()))
    freedom = 0
    for t in range(time):
        speed = t
        dist = speed * (time - t)
        if dist > max_dist:
            freedom += 1
    print(freedom)
