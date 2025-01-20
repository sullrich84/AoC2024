from icecream import ic
from functools import reduce


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    lines = [line.split(" ") for line in lines]
    return [list(map(int, line)) for line in lines]


def is_safe(nums):
    diffs = [a - b for a, b in zip(nums, nums[1:])]
    return all(d in [1, 2, 3] for d in diffs) or all(d in [-1, -2, -3] for d in diffs)


def solve1(data):
    safe = 0
    for nums in data:
        if is_safe(nums):
            safe += 1

    return safe


def solve2(data):
    safe = 0
    for nums in data:
        for i in range(len(nums)):
            nnums = nums[:i] + nums[i + 1 :]
            if is_safe(nnums):
                safe += 1
                break
    return safe


print("🎄 Day 2: Red-Nosed Reports")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
