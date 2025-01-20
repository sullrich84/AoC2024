from icecream import ic


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [line.split("   ") for line in lines]


def solve1(data):
    left, right = [], []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    ans = 0
    while left:
        l = min(left)
        r = min(right)
        left.remove(l)
        right.remove(r)
        ans += abs(l - r)
    return ans


def solve2(data):
    left, right = [], []
    for l, r in data:
        left.append(int(l))
        right.append(int(r))

    ans = 0
    for l in left:
        count = len(list(filter(lambda r: r == l, right)))
        ans += l * count
    return ans


print("🎄 Day 1: Historian Hysteria")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
