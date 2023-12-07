import os
from collections import defaultdict

pwd = os.path.dirname(os.path.realpath(__file__))
file_ = os.path.join(pwd, "day7.txt")

r = {
    0: "no match",
    1: "pair",
    2: "2 pair",
    3: "three kind",
    4: "full house",
    5: "four of kind",
    6: "five kind",
}


def categorize_hand(cards):
    d = defaultdict(int)
    for card in cards:
        d[card] += 1
    c = sorted(d.values(), reverse=True)
    # print(c, c[0])
    if c[0] == 5:
        return 6
    elif c[0] == 4:
        if d["J"] == 4:
            return 6

        return 5 + d["J"]
    elif c[0] == 3 and c[1] == 2:
        if d["J"] == 2 or d["J"]:
            return 6
        return 4
    elif c[0] == 3:
        if d["J"]:
            # found kind
            return 5

        return 3 + d["J"]
    elif c[0] == 2 and c[1] == 2:
        if d["J"] == 2:
            # four of a kind
            return 5

        if d["J"] == 1:
            # full house
            return 4

        return 2 + d["J"]
    elif c[0] == 2:
        if d["J"] in [1, 2]:
            # three of a kind is more than 2 pair
            return 3

        return 1
    elif c[0] == 1:
        return 0 + d["J"]


def hand2num(cards):
    arr = []
    for card in cards:
        if card == "A":
            arr.append(14)
        elif card == "K":
            arr.append(13)
        elif card == "Q":
            arr.append(12)
        elif card == "J":
            arr.append(1)
        elif card == "T":
            arr.append(10)
        else:
            arr.append(int(card))
    return arr


with open(file_, "r") as f:
    hands = []

    for player in f.readlines():
        (cards, bid) = player.split()
        cat = categorize_hand(cards)
        if "J" in cards:
            print(cards, r[cat])
        cards = hand2num(cards)
        hands.append([cat, cards, bid])
    # print(hands)
    hands.sort(key=lambda x: (x[0], x[1]))
    # print(hands)

    tot = sum([(idx + 1) * int(hand[2]) for idx, hand in enumerate(hands)])
    print(tot)
