from heapq import heapify, heappop, heappush


def parseData(name="task"):
    grid = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in grid]


def solve1(grid):
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
    pq = [(0, "E", start)]
    heapify(pq)

    while pq:
        score, facing, pos = heappop(pq)
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
                    return nScore
                else:
                    heappush(pq, (nScore, dn, nPos))


def solve2(grid):
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

    pq = [(0, "E", start, set())]
    heapify(pq)

    costs = {}
    paths = set()

    while pq:
        score, facing, pos, path = heappop(pq)
        r, c = pos

        posCosts = costs.get((pos, facing), float("inf"))
        if score > posCosts:
            continue
        elif score < posCosts:
            costs[(pos, facing)] = score

        path.add(pos)

        for dr, dc, dn in dirs:
            nr, nc = (dr + r, dc + c)
            nPos = (nr, nc)
            nt = grid[nr][nc]

            if nt == "#":
                continue

            mod = 1 if facing == dn else 1001
            nScore = score + mod

            if nPos == end:
                if nScore > costs.get(end, float("inf")):
                    break
               
                path.add(end)
                paths = paths.union(path)
                costs[end] = nScore
            else:
                heappush(pq, (nScore, dn, nPos, path.copy()))

    return len(path)


print("🎄 Day 16: Reindeer Maze")
print("Part 1:", solve1(parseData("sample")))
print(f"Part 2:", solve2(parseData("sample")))
