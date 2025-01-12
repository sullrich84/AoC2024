from icecream import ic


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve(data):
    return data


print("🎄 Day 0: XXX")
print("Part 1:", solve(parseData("sample")))
print("Part 2:", solve(parseData("sample")))
