from collections import deque


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    coords = [line.split(",") for line in lines]
    return [tuple((int(x), int(y))) for x, y in coords]


def solve(part, data, kb):
    size = max([r for r, _ in data] + [c for _, c in data])
    start_grid = data[:kb]

    def bfs(grid, sr, sc, er, ec):
        stack = deque([(sr, sc, 0, [])])
        seen = []

        while stack:
            r, c, s, p = stack.popleft()

            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if nr < 0 or nc < 0 or nr > size or nc > size:
                    # out of range
                    continue

                if (nr, nc) in grid:
                    # corrupted field
                    continue

                if (nr, nc) in seen:
                    # detour
                    continue

                np = p.copy()
                np.append((nr, nc))

                if nr == er and nc == ec:
                    # reached end
                    return np

                seen.append((nr, nc))
                stack.append((nr, nc, s + 1, np))

    path = bfs(start_grid, 0, 0, size, size)
    
    if part == 1:
        return len(path) 
    
    for i in range(len(data), 0, -1):
        grid2 = data[:i]
        path2 = bfs(grid2, 0, 0, size, size)
        if path2:
            r,c = data[i]
            return f"{r},{c}" 


print("🎄 Day 18: RAM Run")
print("Part 1:", solve(1, parseData("task"), 1024))
print("Part 2:", solve(2, parseData("task"), 1024))
