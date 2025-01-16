from collections import deque
from inspect import stack
from typing import Deque
from icecream import ic


def parseData(name="task"):
    data = open(f"{name}.txt").read().splitlines()
    data = [line.replace(":", "").split(" ") for line in data]
    data = [list(map(int, line)) for line in data]
    return data


def solve1(data):
    solvable = 0
    for row in data:
        res = row[0]
        numbers = row[1:]
        stack = deque([(numbers[0], 1)])
        while stack:
            r, i = stack.pop()
            if r == res:
                solvable += res
                stack.clear()
                break
            if r > res or i > len(numbers) - 1:
                continue

            stack.append((r * numbers[i], i + 1))
            stack.append((r + numbers[i], i + 1))

    return solvable


print("🎄 Day 0: XXX")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve1(parseData("sample")))
