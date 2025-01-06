from collections import deque


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    coords = [line.split(",") for line in lines]
    return [tuple((int(y), int(x))) for x, y in coords]


def solve(data, kb):
    grid_size = max([r for r, _ in data] + [c for _, c in data])
    grid = data[:kb]

    print(grid_size, kb)

    # row, col, steps
    stack = deque([(0, 0, 0)])
    seen = []

            
    while stack:
        r, c, s = stack.popleft()
        seen.append((r, c))

        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > grid_size or nc > grid_size:
                # out of range
                continue

            if (nr, nc) in grid:
                # corrupted field
                continue

            if (nr, nc) in seen:
                # detour
                continue

            if nr == nc == grid_size:
                # reached end
                return s + 1

            stack.append((nr, nc, s + 1))

    # for r in range(grid_size + 1):
    #     out = ""
    #     for c in range(grid_size + 1):
    #         if (r, c) in path:
    #             out += "O"
    #         elif (r, c) in grid:
    #             out += "#"
    #         else:
    #             out += "."
    #     print(out)


print("🎄 Day 18: RAM Run")
print("Part 1:", solve(parseData("sample"), 12))
# < 310
print("Part 1:", solve(parseData("task"), 1024))
# print(f"Part 2:", solve(parseData("sample")))
