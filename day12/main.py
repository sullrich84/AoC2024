from collections import defaultdict, deque
from icecream import ic


def parseData(name="task"):
    return [list(l) for l in open(f"{name}.txt").read().splitlines()]


def solve(data):
    rows, cols = len(data), len(data[0])

    regions = defaultdict(list)
    stack = deque([(0, 0, (0, 0))])
    assigned = set([])

    while stack:
        r, c, g = stack.popleft()
        t = data[r][c]

        if (r, c) in assigned:
            continue

        regions[g].append((r, c))
        assigned.add((r, c))

        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if nr not in range(rows) or nc not in range(cols):
                continue
            if (nr, nc) in assigned:
                continue

            nt = data[nr][nc]
            if nt == t:
                stack.appendleft((nr, nc, g))
            else:
                stack.append((nr, nc, (nr, nc)))

    total = 0
    for region, members in regions.items():
        area = len(members)
        type = data[region[0]][region[1]]
        perimeter = 0

        rr = [r for r, _ in members]
        cc = [c for _, c in members]

        for r in range(min(rr), max(rr) + 1):
            for c in range(min(cc), max(cc) + 1):
                if (r, c) in members:
                    p = 4
                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if (nr, nc) in members:
                            p -= 1
                    perimeter += p

        total += area * perimeter

    return total


print("🎄 Day 12: Garden Groups")
print("Part 1:", solve(parseData("task")))
# print("Part 2:", solve(parseData("sample")))
