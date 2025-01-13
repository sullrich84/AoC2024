from functools import cache


def parseData(name="task"):
    return [int(s) for s in open(f"{name}.txt").read().split()]


def solve(stones, t):
    @cache
    def evolve(n, t):
        if t == 0:
            return 1
        if n == 0:
            return evolve(1, t - 1)
        string = str(n)
        length = len(string)
        if length % 2 == 0:
            l, r = int(string[: length // 2]), int(string[length // 2 :])
            return evolve(l, t - 1) + evolve(r, t - 1)
        else:
            return evolve(n * 2024, t - 1)


    result = 0
    for stone in stones:
        result += evolve(stone, t)
    return result


print("🎄 Day 11: Plutonian Pebbles")
print("Part 1:", solve(parseData("task"), 25))
print("Part 2:", solve(parseData("task"), 75))
