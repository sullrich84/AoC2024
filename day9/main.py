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
    files = {}
    blanks = []

    fid = 0
    pos = 0

    for i, char in enumerate(data):
        if i % 2 == 0:
            files[fid] = (pos, char)
            fid += 1
        else:
            if char != 0:
                blanks.append((pos, char))
        pos += char

    while fid > 0:
        fid -= 1
        pos, size = files[fid]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break

    total = 0

    for fid, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += fid * x

    return total


print("🎄 Day 9: Disk Fragmenter")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
