from itertools import product
from collections import deque
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


def solve2(data):
    solvable = 0

    for row in data:
        res, *nums = row
        for combo in product("+*|", repeat=len(nums) - 1):
            ans = nums[0]
            for i in range(1, len(nums)):
                if combo[i - 1] == "+":
                    ans += nums[i]
                elif combo[i - 1] == "*":
                    ans *= nums[i]
                elif combo[i - 1] == "|":
                    ans = int(str(ans) + str(nums[i]))
            if ans == res:
                solvable += res
                break

    return solvable


print("🎄 Day 7: Bridge Repair")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
