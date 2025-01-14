from collections import defaultdict
from icecream import ic
from heapq import heapify, heappop, heappush


def parseData(name="task"):
    data = open(f"{name}.txt").read().splitlines()
    data = [list(line) for line in data]
    return [[int(num) for num in line] for line in data]


def solve(data):
    rows = len(data)
    cols = len(data[0])

    stack = []
    heapify(stack)

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 0:
                heappush(stack, (0, 0, r, c, []))

    paths = defaultdict(set)

    while stack:
        steps, height, r, c, path = heappop(stack)
        path.append((r, c))

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr not in range(rows) or nc not in range(cols):
                continue
            if data[nr][nc] == height + 1:
                if data[nr][nc] == 9:
                    paths[path[0]].add((nr, nc))
                else:
                    heappush(stack, (steps + 1, height + 1, nr, nc, path))

    scores = 0
    for root in paths:
        scores += len(paths[root])

    return scores


print("🎄 Day 10: Hoof It")
print("Part 1:", solve(parseData("task")))
# print("Part 2:", solve(parseData("sample")))
