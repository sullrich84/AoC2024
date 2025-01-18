import re


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve1(data):
    ans = 0
    for row in data:
        muls = re.findall("mul\(\d+,\d+\)", row)
        for mul in muls:
            l, r = mul.replace("mul(", "").replace(")", "").split(",")
            ans += int(l) * int(r)
    return ans


def solve2(data):
    ans = 0
    enabled = True
    for row in data:
        muls = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", row)
        for mul in muls:
            if mul == "do()":
                enabled = True
            elif mul == "don't()":
                enabled = False
            elif enabled:
                l, r = mul.replace("mul(", "").replace(")", "").split(",")
                ans += int(l) * int(r)
    return ans


print("🎄 Day 3: Mull It Over")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
