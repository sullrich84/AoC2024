from icecream import ic
from functools import reduce
from operator import concat


def parseData(name="task"):
    return [int(s) for s in open(f"{name}.txt").read().split()]


def solve(stones):
    def evolve(n, t):
        if t == 0:
            return [n]
        elif n == 0:
            return reduce(concat, [evolve(1, t - 1)])
        elif len(str(n)) % 2 == 0:
            s = int(len(str(n)) / 2)
            l, r = int(str(n)[:s]), int(str(n)[s:])
            return reduce(concat, [evolve(l, t - 1), evolve(r, t - 1)])
        else:
            return reduce(concat, [evolve(n * 2024, t - 1)])

    result = []
    for stone in stones:
        result += evolve(stone, 25)
    return len(result)


print("🎄 Day 11: Plutonian Pebbles")
print("Part 1:", solve(parseData("task")))
print("Part 2:", solve(parseData("sample")))
