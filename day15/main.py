from icecream import ic


vec = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
grid, moves = open("test2.txt").read().split("\n\n")
grid = [list(l) for l in grid.splitlines()]
moves = [vec[m] for m in list(moves.replace("\n", ""))]

for i, row in enumerate(grid):
    nrow = ""
    for e in row:
        if e == ".":
            nrow += ".."
        elif e == "O":
            nrow += "[]"
        elif e == "#":
            nrow += "##"
        elif e == "@":
            nrow += "@."
    grid[i] = list(nrow)

walls = []
boxes = []

pr, pc = 0, 0
rows = len(grid)
cols = len(grid[0])


def lookup(r, c):
    if (r, c) in boxes:
        return "["
    elif (r, c - 1) in boxes:
        return "]"
    elif (r, c) in walls:
        return "#"
    elif (r, c) == (pr, pc):
        return "@"
    return "."


def find_box(r, c):
    if (r, c) in boxes:
        return (r, c)
    elif (r, c - 1) in boxes:
        return (r, c - 1)


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
        if grid[r][c] == "[":
            boxes.append((r, c))
        elif grid[r][c] == "#":
            walls.append(pos)
        elif grid[r][c] == "@":
            pr, pc = pos


def safe_guard():
    for r, c in boxes:
        if (r, c + 1) in boxes:
            raise AssertionError("Overlapping boxes", (r, c + 1))
        if (r, c) in walls or (r, c + 1) in walls:
            raise AssertionError("Box in wall")


for dr, dc in moves:
    safe_guard()
    draw()

    nr, nc = pr + dr, pc + dc
    if lookup(nr, nc) == ".":
        pr, pc = nr, nc

    elif lookup(nr, nc) in ["[", "]"]:
        # At this point we know we'll hit
        # a box with the next move
        mboxes = [find_box(nr, nc)]

        ndr = dr
        ndc = 2 * dc if dr == 0 else dc
        nnr, nnc = nr + ndr, nc + ndc

        while True:
            if lookup(nnr, nnc) == ".":
                break
            elif lookup(nnr, nnc) == "#":
                mboxes.clear()
                break
            elif lookup(nnr, nnc) in ["[", "]"]:
                # Also check left and right corner of
                # closest box when moving vertically
                if dc == 0:
                    # WARN: This doesnt work, we need cs, ce per row! 
                    rs = min(map(lambda b: b[0], mboxes))
                    re = max(map(lambda b: b[0], mboxes))

                    cs = min(map(lambda b: b[1], mboxes))
                    ce = max(map(lambda b: b[1], mboxes)) + 1

                    ic(rs, re, cs, ce)
                    
                    for nnr in range(rs, re + 1):
                        for nnc in range(cs, ce + 1, 2):
                            if lookup(nnr, nnc) in ["[", "]"]:
                                nbox = find_box(nnr, nnc)
                                mboxes.append(nbox)
                                ic(cs, ce, nnc, nbox)
                            elif lookup(nnr, nnc) == "#":
                                ic("collision with wall")
                                mboxes.clear()
                                break
                else:
                    nbox = find_box(nnr, nnc)
                    mboxes.append(nbox)

            nnr, nnc = nnr + ndr, nnc + ndc
            ic((pr, pc), mboxes, (nnr, nnc))

        for br, bc in mboxes:
            boxes.remove((br, bc))
            boxes.append((br + dr, bc + dc))

        if mboxes != []:
            pr, pc = nr, nc

safe_guard()
draw()

print("Part 1:", sum(list(map(lambda e: 100 * e[0] + e[1], boxes))))
