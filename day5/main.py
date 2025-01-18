from math import floor
from icecream import ic


def parseData(name="task"):
    order, input = open(f"{name}.txt").read().split("\n\n")
    order = [tuple(line.split("|")) for line in order.splitlines()]
    input = [line.split(",") for line in input.splitlines()]
    return order, input


def solve(data, sort):
    order, input = data

    def is_ordered(row):
        for i in range(len(row)):
            for o1, o2 in filter(lambda p: p[0] == row[i] or p[1] == row[i], order):
                if o1 == row[i] and o2 in row:
                    if row.index(o2) < i:
                        return False
                if o2 == row[i] and o1 in row:
                    if row.index(o1) > i:
                        return False
        return True

    def apply_order(row):
        unsorted = True
        while unsorted:
            unsorted = False
            for i in range(len(row)):
                for o1, o2 in filter(lambda p: p[0] == row[i] or p[1] == row[i], order):
                    if o1 == row[i] and o2 in row:
                        ii = row.index(o2)
                        if ii < i:
                            row[ii], row[i] = row[i], row[ii]
                            unsorted = True
                    if o2 == row[i] and o1 in row:
                        ii = row.index(o1)
                        if ii > i:
                            row[ii], row[i] = row[i], row[ii]
                            unsorted = True

        return row

    ans = 0
    for row in input:
        if not sort and is_ordered(row):
            i = int(floor(len(row) / 2))
            ans += int(row[i])
        if sort and not is_ordered(row):
            apply_order(row)
            i = int(floor(len(row) / 2))
            ans += int(row[i])
    return ans


print("🎄 Day 5: Print Queue")
print("Part 1:", solve(parseData("task"), False))
print("Part 2:", solve(parseData("task"), True))
