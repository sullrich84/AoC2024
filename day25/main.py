def parseData(name="task"):
    schematics = open(f"{name}.txt").read().split("\n\n")
    schematics = [line.splitlines() for line in schematics]

    locks, keys = [], []
    for schema in schematics:
        if "#####" in schema[0]:
            locks.append(schema)
        else:
            keys.append(schema)

    return (locks, keys)


def solve(locks, keys):
    mr, mc = 7, 5

    lock_heights = []
    for lock in locks:
        h = []
        for c in range(0, mc):
            count = 0
            for r in range(1, mr):
                if lock[r][c] == ".":
                    h.append(count)
                    break
                count += 1
        lock_heights.append(tuple(h))

    key_heights = []
    for key in keys:
        h = []
        for c in range(0, mc):
            count = 0
            for r in range(mr - 2, -1, -1):
                if key[r][c] == ".":
                    h.append(count)
                    break
                count += 1
        key_heights.append(tuple(h))

    unique = 0
    for key in key_heights:
        for lock in lock_heights:
            zips = list(zip(key, lock))
            overlaps = list(map(lambda e: (5 - e[0] - e[1]) < 0, zips))
            if not sum(overlaps):
                unique += 1

    return unique


print("🎄 Day 25: Code Chronicle")
print("Part 1:", solve(*parseData("task")))
