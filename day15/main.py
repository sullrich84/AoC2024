from icecream import ic
import os

dirs = {
    "^": (-1, 0),
    "v": (+1, 0),
    ">": (0, +1),
    "<": (0, -1),
}


def parseData(name="task"):
    grid, moves = open(f"{name}.txt").read().split("\n\n")
    grid = [list(c) for c in grid.splitlines()]
    moves = list(map(lambda c: dirs[c], list(moves.splitlines()[0])))
    return grid, moves


def find(grid, char):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == char:
                return (r, c)
    return (-1, -1)


def find_all(grid, char):
    all = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == char:
                all.append((r, c))
    return all


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def draw(grid, pos, walls, boxes):
    for r in range(len(grid)):
        out = ""
        for c in range(len(grid[0])):
            if (r, c) == pos:
                out += "@"
            elif (r, c) in boxes:
                out += "O"
            elif (r, c) in walls:
                out += "#"
            else:
                out += "."
        print(out)
    print()


def in_range(pos, rows, cols):
    r, c = pos
    return r in range(rows) and c in range(cols)


def sum_coords(boxes):
    ans = 0
    for r, c in boxes:
        ans += 100 * r + c
    return ans


def safe_guard(walls, boxes):
    for b in boxes:
        if b in walls:
            raise Warning("Box in Wall")


def solve1(grid, moves):
    rows, cols = len(grid), len(grid[0])
    boxes = find_all(grid, "O")
    walls = find_all(grid, "#")
    pos = find(grid, "@")

    for mvec in moves[:44]:
        npos = add(pos, mvec)
        safe_guard(walls, boxes)

        if not in_range(npos, rows, cols) or npos in walls:
            continue
        if npos in boxes:
            to_move = []
            search_pos = npos
            while in_range(search_pos, rows, cols) and search_pos in boxes:
                to_move.append(search_pos)
                search_pos = add(search_pos, mvec)
            if add(to_move[-1], mvec) not in walls:
                pos = npos
                for m in to_move:
                    boxes.remove(m)
                    boxes.append(add(m, mvec))
        else:
            pos = npos

    ic(mvec)
    draw(grid, pos, walls, boxes)
    # draw(grid, pos, walls, boxes)
    return sum_coords(boxes)


print("🎄 Day 15: Warehouse Woes")
print("Part 1:", solve1(*parseData("sample")))
# print("Part 2:", solve(*parseData("sample")))
