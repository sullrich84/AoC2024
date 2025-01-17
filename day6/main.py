from icecream import ic


def parseData(name="task"):
    grid = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in grid]


def solve1(grid):
    pr, pc = (0, 0)
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                pr, pc = r, c
                break

    pv = 0
    vec = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()

    while True:
        seen.add((pr, pc))
        nr, nc = pr + vec[pv][0], pc + vec[pv][1]
        if nr not in range(rows) or nc not in range(cols):
            break
        if grid[nr][nc] == "#":
            pv = (pv + 1) % 4
        else:
            pr, pc = nr, nc

    return len(seen)


def solve2(grid):
    pr, pc = (0, 0)
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                pr, pc = r, c
                break

    def simulate(pr, pc, block):
        pv = 0
        vec = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()

        while True:
            seen.add((pr, pc, pv))
            nr, nc = pr + vec[pv][0], pc + vec[pv][1]
            if nr not in range(rows) or nc not in range(cols):
                break
            if (nr, nc, pv) in seen:
                return True
            if grid[nr][nc] == "#" or (nr, nc) == block:
                pv = (pv + 1) % 4
            else:
                pr, pc = nr, nc

        return False

    loops = 0
    for r in range(rows):
        for c in range(cols):
            if simulate(pr, pc, (r, c)):
                loops += 1

    return loops


print("🎄 Day 6: ")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
