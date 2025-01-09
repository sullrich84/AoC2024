from collections import deque, defaultdict


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in lines]


def solve(grid):
    rows, cols = len(grid), len(grid[0])
    r, c = 0, 0

    for cr in range(rows):
        for cc in range(cols):
            t = grid[cr][cc]
            if t == "S":
                r = cr
                c = cc

    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0

    while grid[r][c] != "E":
        # Single path, no crossings
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            if nr not in range(rows) or nc not in range(cols):
                continue
            if grid[nr][nc] == "#":
                continue
            if dists[nr][nc] != -1:
                # Way we came
                continue
            dists[nr][nc] = dists[r][c] + 1
            r, c = nr, nc

    # for row in dists:
    #     print(*row, sep="\t")

    cheats = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in [
                        # To avoid double checks, we only check
                        # one half of all possible directions
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    ]:
                        if nr not in range(rows) or nc not in range(cols):
                            continue
                        if grid[nr][nc] == "#":
                            continue
                        if dists[r][c] - dists[nr][nc] >= 100 + radius:
                            cheats += 1

    return cheats


print("🎄 Day 20: Race Condition")
# print("Part 1:", solve(parseData("task")))
print(f"Part 2:", solve(parseData("task")))
