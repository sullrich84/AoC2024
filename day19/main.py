from collections import deque


def parseData(name="task"):
    first, second = open(f"{name}.txt").read().split("\n\n")
    return [first.split(", "), second.splitlines()]


def solve(data):
    pattern, towels = data

    def match(s1, s2):
        if s1 == s2:
            return True

        if len(s1) <= len(s2):
            return False

        for i, c in enumerate(list(s2)):
            if c != s1[i]:
                return False

        return True

    def lookup(t):
        stack = deque([])

        # Fill stack with inital matches
        for p in pattern:
            if match(t, p):
                stack.append(p)

        # Find matching combination
        while stack:
            m = stack.pop()
            for p in pattern:
                if t == m + p:
                    return True
                if match(t, m + p):
                    stack.append(m + p)

        return False

    designs = 0
    for t in towels:
        if lookup(t):
            designs += 1

    return designs


print("🎄 Day 19: Linen Layout")
print("Part 1:", solve(parseData("task")))
print(f"Part 2:", solve(parseData("task")))
