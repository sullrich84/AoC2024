from collections import defaultdict, deque
from icecream import ic


def parseData(name="task"):
    return [list(l) for l in open(f"{name}.txt").read().splitlines()]


def solve1(data):
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
    for members in regions.values():
        area = len(members)
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


def solve2(data):
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
    for members in regions.values():
        corner_candidates = set()
        for r, c in members:
            for cr, cc in [ (r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
                corner_candidates.add((cr, cc))
        corners = 0
        for cr, cc in corner_candidates:
            config = [
                (sr, sc) in members
                for sr, sc in [
                    (cr - 0.5, cc - 0.5),
                    (cr + 0.5, cc - 0.5),
                    (cr + 0.5, cc + 0.5),
                    (cr - 0.5, cc + 0.5),
                ]
            ]
            number = sum(config)
            if number == 1:
                corners += 1
            elif number == 2:
                if config == [True, False, True, False] or config == [
                    False,
                    True,
                    False,
                    True,
                ]:
                    corners += 2
            elif number == 3:
                corners += 1

        total += len(members) * corners
    return total


print("🎄 Day 12: Garden Groups")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
