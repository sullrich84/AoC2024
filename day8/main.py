from __future__ import annotations
from itertools import combinations
from collections import defaultdict
from icecream import ic


def parseData(name="task"):
    grid = open(f"{name}.txt").read().splitlines()
    return [list(line) for line in grid]


def scan(grid):
    results = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                results[grid[r][c]].append((r, c))
    return results


def solve1(grid):
    scanning = scan(grid)
    antinodes = defaultdict(list)

    for freq, antennas in scanning.items():
        pairs = list(combinations(antennas, 2))
        for (ar, ac), (br, bc) in pairs:
            dr = ar - br
            dc = ac - bc
            anode1 = (ar + dr, ac + dc)
            anode2 = (br - dr, bc - dc)
            antinodes[freq].append(anode1)
            antinodes[freq].append(anode2)
            if (ar, ac) == (2, 5) and (br, bc) == (4, 4):
                ic((ar, ac), (br, bc), (dr, dc), anode1, anode2)

    h, w = len(grid), len(grid[0])

    unique = set()
    for freq, anodes in antinodes.items():
        for r, c in anodes:
            if r in range(h) and c in range(w):
                unique.add((r, c))

    return len(unique)


def solve2(grid):
    scanning = scan(grid)
    antinodes = defaultdict(list)
    rows, cols = len(grid), len(grid[0])

    for freq, antennas in scanning.items():
        pairs = list(combinations(antennas, 2))
        for (ar, ac), (br, bc) in pairs:
            dr = ar - br
            dc = ac - bc

            c = 1
            while True:
                a1r, a1c = (ar + dr * c, ac + dc * c)
                a2r, a2c = (br - dr * c, bc - dc * c)

                in_range = False
                if a1r in range(rows) and a1c in range(cols):
                    antinodes[freq].append((a1r, a1c))
                    in_range = True
                if a2r in range(rows) and a2c in range(cols):
                    antinodes[freq].append((a2r, a2c))
                    in_range = True

                if not in_range:
                    break

                if (ar, ac) == (8, 8) and (br, bc) == (9, 9):
                    ic((a1r, a1c), (a2r, a2c))

                c += 1

    unique = set()
    for _, antennas in scanning.items():
        unique.update(antennas)

    for freq, anodes in antinodes.items():
        for r, c in anodes:
            if r in range(rows) and c in range(cols):
                unique.add((r, c))

    return len(unique)


print("🎄 Day 8: Resonant Collinearity")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
