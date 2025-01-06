from collections import deque
from heapq import heapify, heappop, heappush


def parseData(name="task"):
    grid = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in grid]


def solve(grid):
    start, end = (0, 0), (0, 0)
    rows, cols = len(grid), len(grid[0])
    dirs = [(-1, 0, "N"), (1, 0, "S"), (0, 1, "E"), (0, -1, "W")]

    # Discover all nodes
    for r in range(rows):
        for c in range(cols):
            pos = (r, c)
            t = grid[r][c]
            if t == "S":
                start = pos
            elif t == "E":
                end = pos

    visited = set()
    pq = [(0, "E", start, 1)]
    heapify(pq)

    while pq:
        score, facing, pos, spots = heappop(pq)
        r, c = pos
        visited.add((r, c, facing))

        for dr, dc, dn in dirs:
            nr, nc = (dr + r, dc + c)
            nPos = (nr, nc)
            nt = grid[nr][nc]

            if nt == "#" or (nr, nc, dn) in visited:
                continue
            else:
                mod = 1 if facing == dn else 1001
                nScore = score + mod

                if nPos == end:
                    return (nScore, spots + 1)
                else:
                    heappush(pq, (nScore, dn, nPos, spots + 1))


print("🎄 Day 16: Reindeer Maze")
print("Part 1:", solve(parseData("sample")))
# print("Part 1:", solve(parseData("task")))
# print(f"Part 2:", solve(parseData("sample")))
