from icecream import ic


def parseData(name="task"):
    return [int(c) for c in open(f"{name}.txt").read().splitlines()[0]]


def solve1(data):
    id = 0
    disk = []

    for i, char in enumerate(data):
        if i % 2 == 0:
            disk += [id] * char
            id += 1
        else:
            disk += ["."] * char

    nums = [i for i, c in enumerate(disk) if c != "."]

    for i, c in enumerate(disk):
        if c == ".":
            ii = nums.pop()
            if i > ii:
                break
            disk[i] = disk[ii]
            disk[ii] = "."

    ans = [i * c for i, c in enumerate(disk) if c != "."]
    return sum(ans)


def solve2(data):
    id = 0
    disk = []

    for i, char in enumerate(data):
        if i % 2 == 0:
            disk += [id] * char
            id += 1
        else:
            disk += ["."] * char

    def free_blocks(length):
        count = 0
        for i, c in enumerate(disk):
            if c == ".":
                count += 1
                if count == length:
                    return i - length + 1
            else:
                count = 0

    # ic("".join(map(str, disk)), free_blocks(7))

    for c in range(9, 0, -1):
        files = [i for i, f in enumerate(disk) if f == c]
        length = len(files)
        space = free_blocks(length)

        if not space or space >= files[0]:
            continue

        # ic("Move", c, length, "to index", space)
        print("".join(map(str, disk)))

        for i in range(space, space + length):
            disk[i] = c
        for i in files:
            disk[i] = "."

    ans = [i * c for i, c in enumerate(disk) if c != "."]
    # assert sum(ans) != 15888670915219
    return sum(ans)


print("🎄 Day 9: Disk Fragmenter")
# print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
