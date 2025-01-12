from icecream import ic
from math import floor


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()

    pos, vec = {}, {}
    for bot, line in enumerate(lines):
        p, v = line.replace("p=", "").replace("v=", "").split()
        (c, r), (dc, dr) = p.split(","), v.split(",")
        pos[bot] = (int(r), int(c))
        vec[bot] = (int(dr), int(dc))

    return (pos, vec)


def print_map(pos, mr, mc):
    for r in range(mr):
        out = ""
        for c in range(mc):
            out += "X" if (r, c) in pos.values() else "."
        print(out)


def solve1(pos, vec, max_time, mr, mc):
    bots = [*pos.keys()]

    for _ in range(max_time):
        for bot in bots:
            (r, c), (dr, dc) = pos[bot], vec[bot]
            pos[bot] = ((r + dr) % mr, (c + dc) % mc)

    print_map(pos, mr, mc)

    cline = floor(mc / 2)
    rline = floor(mr / 2)
    q1, q2, q3, q4 = 0, 0, 0, 0

    for r, c in pos.values():
        if r == rline or c == cline:
            continue
        if r < rline:
            if c < cline:
                q1 += 1
            else:
                q2 += 1
        else:
            if c < cline:
                q3 += 1
            else:
                q4 += 1

    return q1 * q2 * q3 * q4




def solve2(pos, vec, mr, mc):
    bots = [*pos.keys()]
    rr = floor(mr / 2)
    cc = floor(mc / 2)

    for time in range(25_000):
        for bot in bots:
            (r, c), (dr, dc) = pos[bot], vec[bot]
            pos[bot] = ((r + dr) % mr, (c + dc) % mc)

        if time == 7093:
            print_map(pos, mr, mc)
            exit()
       


print("🎄 Day 17: Chronospatial Computer")
# print("Part 1:", solve1(*parseData("sample"), 100, 7, 11))
# print("Part 1:", solve1(*parseData("task"), 100, 103, 101))
print("Part 2:", solve2(*parseData("task"), 103, 101))
