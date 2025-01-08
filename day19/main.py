from collections import deque


def parseData(name="task"):
    first, second = open(f"{name}.txt").read().split("\n\n")
    return [first.split(", "), second.splitlines()]


def solve(data):
    pattern, towels = data
    cache = {"": 1}
    max_pattern_len = max(map(len, pattern))

    def possible_designs(design):
        if design in cache:
            return cache[design]

        count = 0
        oRange = min(len(design), max_pattern_len)
        for i in range(oRange + 1):
            snippet, remainder = design[:i], design[i:]
            if snippet in pattern:
                count += possible_designs(remainder)

        cache[design] = count
        return count

    return [possible_designs(design) for design in towels]


print("🎄 Day 19: Linen Layout")
print("Part 1:", sum([bool(r) for r in solve(parseData("task"))]))
print(f"Part 2:", sum(solve(parseData("task"))))
