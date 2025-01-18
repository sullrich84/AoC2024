def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve1(data):
    rows = len(data)
    cols = len(data[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "X":
                for dr, dc in [
                    (-1, 0),
                    (+1, 0),
                    (0, -1),
                    (0, +1),
                    (-1, -1),
                    (+1, +1),
                    (-1, +1),
                    (+1, -1),
                ]:
                    check = "X"
                    rr, cc = r, c
                    while check in "XMAS":
                        rr, cc = rr + dr, cc + dc
                        if rr in range(rows) and cc in range(cols) and check in "XMAS":
                            check += data[rr][cc]
                            continue
                        break
                    if check.startswith("XMAS"):
                        count += 1

    return count


def solve2(data):
    rows = len(data)
    cols = len(data[0])
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                ul = data[r - 1][c - 1]
                dr = data[r + 1][c + 1]
                ur = data[r - 1][c + 1]
                dl = data[r + 1][c - 1]
                if "MS" in [ul + dr, dr + ul] and "MS" in [ur + dl, dl + ur]:
                    count += 1

    return count


print("🎄 Day 4: ")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
