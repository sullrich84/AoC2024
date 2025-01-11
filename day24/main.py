from collections import deque
from itertools import combinations


def parseData(name="task"):
    left, right = open(f"{name}.txt").read().split("\n\n")
    inputs = [tuple(i.split(": ")) for i in left.splitlines()]
    connections = [tuple(c.split(" -> ")) for c in right.splitlines()]
    return (
        [(k, int(v)) for k, v in inputs],
        {v: tuple(k.split()) for k, v in connections},
    )


def compute_state(inputs, connections):
    state = {}
    for wire, value in inputs:
        state[wire] = value

    unresolved = deque(connections.items())
    while len(unresolved) > 0:
        wire, (w1, op, w2) = unresolved.popleft()
        if w1 not in state or w2 not in state:
            unresolved.append((wire, (w1, op, w2)))
            continue
        elif op == "AND":
            state[wire] = state[w1] and state[w2]
        elif op == "XOR":
            state[wire] = state[w1] ^ state[w2]
        elif op == "OR":
            state[wire] = state[w1] or state[w2]

    return state


def get_binary(state, char):
    keys = reversed(sorted(list(filter(lambda k: k[0] == char, state.keys()))))
    return "".join([str(state[k]) for k in keys])


def solve1(data):
    inputs, connections = data
    state = compute_state(inputs, connections)
    return int(get_binary(state, "z"), 2)


def solve2(data):
    _, connections = data

    print(connections)

    for row in connections.items():
        print(*row)
    return 0


print("🎄 Day 0: Crossed Wires")
# print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
