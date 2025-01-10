from collections import deque
from itertools import product
from functools import cache


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve(data, keypads):
    num_pad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["X", "0", "A"],
    ]

    arr_pad = [
        ["X", "^", "A"],
        ["<", "v", ">"],
    ]

    def build_paths(pad):
        paths = {}
        rows, cols = len(pad), len(pad[0])
        for rr in range(rows):
            for cc in range(cols):
                start_key = pad[rr][cc]
                if start_key == "X":
                    continue

                paths[start_key] = {start_key: ["A"]}
                stack = deque([(rr, cc, "")])
                while stack:
                    r, c, seq = stack.popleft()
                    for nr, nc, key, okey in [
                        (r - 1, c, "^", "v"),
                        (r + 1, c, "v", "^"),
                        (r, c - 1, "<", ">"),
                        (r, c + 1, ">", "<"),
                    ]:
                        if okey in seq:
                            continue
                        if nr not in range(rows) or nc not in range(cols):
                            continue

                        dest_key = pad[nr][nc]
                        if dest_key == "X":
                            continue

                        if dest_key not in paths[start_key]:
                            paths[start_key][dest_key] = []

                        paths[start_key][dest_key].append(seq + key + "A")
                        stack.append((nr, nc, seq + key))
        return paths

    num_paths = build_paths(num_pad)
    arr_paths = build_paths(arr_pad)

    def get_instructions(seq):
        possibilities = []
        prev = "A"
        for s in list(seq):
            possibilities.append(num_paths[prev][s])
            prev = s
        return ["".join(s) for s in list(product(*possibilities))]

    @cache
    def calc_length(src, dest, depth):
        if depth == 1:
            # Since every path has the same length
            # we can work with first length only
            return len(arr_paths[src][dest][0])

        optimal = float("inf")
        for seq in arr_paths[src][dest]:
            length = 0
            for nSrc, nDest in zip("A" + seq, seq):
                length += calc_length(nSrc, nDest, depth - 1)
            optimal = min(optimal, length)
        return optimal

    complexity = 0

    for line in data:
        sequences = get_instructions(line)
        optimal = float("inf")
        for seq in sequences:
            length = 0
            for src, dest in zip("A" + seq, seq):
                length += calc_length(src, dest, keypads)
            optimal = min(optimal, length)
        complexity += optimal * int(line[:-1])

    return complexity


print("🎄 Day 21: Keypad Conundrum")
print("Part 1:", solve(parseData("task"), 2))
print(f"Part 2:", solve(parseData("task"), 25))
