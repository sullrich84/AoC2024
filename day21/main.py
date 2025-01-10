from collections import deque
from itertools import product


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve(data):
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
                        stack.append([nr, nc, seq + key])
        return paths

    num_paths = build_paths(num_pad)
    arr_paths = build_paths(arr_pad)

    def get_instructions(string, paths):
        possibilities = []
        prev = "A"
        for s in list(string):
            possibilities.append(paths[prev][s])
            prev = s
        return ["".join(s) for s in list(product(*possibilities))]

    complexity = 0
    for line in data:
        sequences = get_instructions(line, num_paths)
        for _ in range(2):
            next_sequences = []
            for seq in sequences:
                next_sequences += get_instructions(seq, arr_paths)
            minlen = min(map(len, next_sequences))
            sequences = [seq for seq in next_sequences if len(seq) == minlen]
        complexity += len(sequences[0]) * int(line[:-1])
    
    return complexity


print("🎄 Day 21: Keypad Conundrum")
print("Part 1:", solve(parseData("task")))
# print(f"Part 2:", solve(parseData("sample")))
