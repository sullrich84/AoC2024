dirs = {
    "^": (-1, 0),
    "v": (+1, 0),
    ">": (0, +1),
    "<": (0, -1),
}


def parseData(name="task", extend=False):
    grid, moves = open(f"{name}.txt").read().split("\n\n")
    grid = grid.splitlines()
    if extend:
        for i, row in enumerate(grid):
            grid[i] = (
                row.replace("#", "##")
                .replace(".", "..")
                .replace("@", "@.")
                .replace("O", "[]")
            )
    grid = [list(c) for c in grid]
    moves = list(map(lambda c: dirs[c], list(moves.replace("\n", ""))))
    return grid, moves


def find(grid, char):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == char:
                return (r, c)
    return (-1, -1)


def solve1(grid, moves):
    rows, cols = len(grid), len(grid[0])
    r, c = find(grid, "@")

    for dr, dc in moves:
        targets = [(r, c)]
        cr = r
        cc = c
        go = True
        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            if char == "#":
                go = False
                break
            if char == "O":
                targets.append((cr, cc))
            if char == ".":
                break
        if not go:
            continue
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = "O"
        r += dr
        c += dc

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                ans += 100 * r + c

    return ans


def solve2(grid, moves):
    rows, cols = len(grid), len(grid[0])
    r, c = find(grid, "@")

    for dr, dc in moves:
        targets = [(r, c)]
        go = True
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in targets:
                continue
            char = grid[nr][nc]
            if char == "#":
                go = False
                break
            if char == "[":
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            if char == "]":
                targets.append((nr, nc))
                targets.append((nr, nc - 1))
        if not go:
            continue
        copy = [list(row) for row in grid]
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grid[br][bc] = "."
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = copy[br][bc]
        r += dr
        c += dc

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "[":
                ans += 100 * r + c

    return ans


print("🎄 Day 15: Warehouse Woes")
print("Part 1:", solve1(*parseData("task", extend=False)))
print("Part 2:", solve2(*parseData("task", extend=True)))
