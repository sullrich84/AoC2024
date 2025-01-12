from icecream import ic


vec = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
grid, moves = open("sample.txt").read().split("\n\n")
grid = [list(l) for l in grid.splitlines()]
moves = [vec[m] for m in list(moves.replace("\n", ""))]

walls = []
boxes = []

pr, pc = 0, 0
rows = len(grid)
cols = len(grid[0])


def lookup(r, c):
    if (r, c) in boxes:
        return "O"
    elif (r, c) in walls:
        return "#"
    elif (r, c) == (pr, pc):
        return "@"
    return "."


def draw():
    for r in range(rows):
        out = ""
        for c in range(cols):
            out += lookup(r, c)
        print(out)
    print()


for r in range(rows):
    for c in range(cols):
        pos = (r, c)
        if grid[r][c] == "O":
            boxes.append(pos)
        elif grid[r][c] == "#":
            walls.append(pos)
        elif grid[r][c] == "@":
            pr, pc = pos


for dr, dc in moves:
    nr, nc = pr + dr, pc + dc
    if lookup(nr, nc) == ".":
        pr, pc = nr, nc
    elif lookup(nr, nc) == "O":
        mboxes = [(nr, nc)]
        nnr, nnc = nr + dr, nc + dc
        while True:
            if lookup(nnr, nnc) == ".":
                break
            elif lookup(nnr, nnc) == "#":
                mboxes.clear()
                break
            mboxes.append((nnr, nnc))
            nnr, nnc = nnr + dr, nnc + dc

        for br, bc in mboxes:
            boxes.remove((br, bc))
            boxes.append((br + dr, bc + dc))

        if mboxes != []:
            pr, pc = nr, nc

draw()

print("Part 1:", sum(list(map(lambda e: 100 * e[0] + e[1], boxes))))
