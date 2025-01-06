def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in lines]


def solve(data):
    return data


print("🎄 Day 0: XXX")
print("Part 1:", solve(parseData("sample")))
print(f"Part 2:", solve(parseData("sample")))
