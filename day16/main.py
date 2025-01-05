from collections import deque
from heapq import heapify, heappop, heappush


def parseData(name="task"):
    grid = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in grid]


def solve(grid):
    nodes = []
    start, end = (0, 0), (0, 0)
    rows, cols = len(grid), len(grid[0])

    rev = {"N": "S", "S": "N", "E": "W", "W": "E"}
    hDirs = [(-1, 0, "N"), (1, 0, "S")]
    vDirs = [(0, 1, "E"), (0, -1, "W")]
    dirs = hDirs + vDirs

    # Discover all nodes
    for r in range(rows):
        for c in range(cols):
            pos = (r, c)
            t = grid[r][c]
            if t == "S":
                start = pos
                nodes.append(start)
            elif t == "E":
                end = pos
                nodes.append(end)
            elif t == ".":
                adj = []
                for dr, dc, d in dirs:
                    if grid[r + dr][c + dc] != "#":
                        adj.append(d)
                if len(adj) == 3:
                    nodes.append(pos)
                elif len(adj) == 2:
                    if set(adj) not in [{"N", "S"}, {"E", "W"}]:
                        nodes.append(pos)

    # for r in range(len(grid)):
    #     out = ""
    #     for c in range(len(grid[0])):
    #         out += ":" if (r, c) in nodes else grid[r][c]
    #     print(out)

    # Discover paths between nodes
    visited = set()
    stack = deque([(end, end, 0), (start, start, 0)])
    paths = {}

    while stack:
        pos, origin, steps = stack.popleft()
        r, c = pos
        visited.add(pos)

        for dr, dc, dn in dirs:
            nr, nc = nPos = (r + dr, c + dc)
            nt = grid[nr][nc]

            if nt == "#" or nPos in visited:
                continue
            else:
                if nPos in nodes:
                    if origin not in paths:
                        paths[origin] = {}
                    if nPos not in paths:
                        paths[nPos] = {}

                    paths[origin][dn] = (nPos, steps + 1)
                    paths[nPos][rev[dn]] = (origin, steps + 1)
                    stack.append((nPos, nPos, 0))
                else:
                    stack.append((nPos, origin, steps + 1))

    pq = [(0, start)]
    heapify(pq)
    seen = set()

    while pq:
        score, pos = heappop(pq)
        print(score, pos)

    # for node in paths:
    #     print(f"Node: {node}")
    #     for o in paths[node]:
    #         adj, steps = paths[node][o]
    #         print(f"   {o}: {adj} with {steps} steps")

    return 0


print("🎄 Day 16: Reindeer Maze")
print("Part 1:", solve(parseData("sample")))
# print("Part 1:", solve(parseData("task")))
# print(f"Part 2:", solve(parseData("sample")))
