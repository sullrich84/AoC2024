data1, data2 = open("task.txt").read().split("\n\n")

grid = [list(line) for line in data1.splitlines()]
moves = data2.replace("\n", "")
mVec = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

rows = len(grid)
cols = len(grid[0])
pos, boxes, walls = (0, 0), [], []


def print_grid():
    for r in range(rows):
        out = ""
        for c in range(cols):
            p = (r, c)
            if p == pos:
                out += "@"
            elif p in boxes:
                out += "O"
            elif p in walls:
                out += "#"
            else:
                out += "."
        print(out)
    print()


for r in range(rows):
    for c in range(cols):
        t = grid[r][c]
        p = (r, c)
        if t == "@":
            pos = p
        elif t == "#":
            walls.append(p)
        elif t == "O":
            boxes.append(p)

for m in moves:
    dr, dc = mVec[m]
    rr, rc = pos
    nr, nc = (rr + dr, rc + dc)
    nPos = (nr, nc)

    if nPos in boxes:
        # Check if box is movable
        nBoxes = 1
        tPos = nPos
        movable = True
        while True:
            tPos = (tPos[0] + dr, tPos[1] + dc)
            if tPos in boxes:
                nBoxes += 1
                continue
            elif tPos in walls:
                movable = False
            break

        # print("dir:", m, "boxes:", nBoxes, "movable:", movable)

        if movable:
            tPos = nPos
            for i in range(0, nBoxes):
                boxes.remove(tPos)
                tPos = (tPos[0] + dr, tPos[1] + dc)
                boxes.append(tPos)
            pos = nPos
    elif nPos not in walls:
        pos = nPos

    # print_grid()

res = 0
for r, c in boxes:
    res += 100 * r + c

print("Answer:", res)
