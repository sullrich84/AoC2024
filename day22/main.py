from functools import cache
from math import floor

def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [int(line) for line in lines]


def solve(data):

    @cache
    def mix_prune(i, sn):
        return (i ^ sn) % 16777216

    @cache
    def sec_num(sn):
        step1 = mix_prune(sn * 64, sn)
        step2 = mix_prune(floor(step1 / 32), step1) 
        step3 = mix_prune(step2 * 2048, step2)
        return step3

    results = []
    for init_sn in data:
        sn = init_sn
        for _ in range(2000):
            sn = sec_num(sn)
        results.append(sn)

    return sum(results)


print("🎄 Day 22: Monkey Market")
print("Part 1:", solve(parseData("task")))
# print(f"Part 2:", solve(parseData("sample")))
