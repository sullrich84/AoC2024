from functools import cache
from math import floor


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return [int(line) for line in lines]


def solve2(data):
    def mix(x, y):
        return x ^ y

    def prune(x):
        return x % 16777216

    def prices(x):
        ans = [x % 10]
        for _ in range(2000):
            x = prune(mix(x * 64, x))
            x = prune(mix(floor(x / 32), x))
            x = prune(mix(x * 2048, x))
            ans.append(x % 10)
        return ans

    def changes(p):
        return [p[i + 1] - p[i] for i in range(len(p) - 1)]

    def score(prices, changes):
        score = {}
        for i in range(len(changes) - 3):
            pattern = tuple(changes[i : i + 4])
            if pattern not in score:
                # We only care about the first occurence
                score[pattern] = prices[i + 4]
        return score

    global_score = {}
    for line in data:
        p = prices(line)
        c = changes(p)
        s = score(p, c)
        for pat, prc in s.items():
            # Sum up all prices depending on their pattern
            if pat not in global_score:
                global_score[pat] = prc
            else:
                global_score[pat] += prc

    best_price = max(global_score.values())
    return best_price


print("🎄 Day 22: Monkey Market")
print("Part 2:", solve2(parseData("task")))
