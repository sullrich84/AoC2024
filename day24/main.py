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

def solve1(data):
    inputs, connections = data

    state = {}
    for wire, value in inputs:
        state[wire] = value

    unresolved = deque(connections.items())
    while len(unresolved) > 0:
        wire, (w1, op, w2) = unresolved.popleft()
        if w1 not in state or w2 not in state:
            unresolved.append(((w1, op, w2), wire))
            continue
        elif op == "AND":
            state[wire] = state[w1] and state[w2]
        elif op == "XOR":
            state[wire] = state[w1] ^ state[w2]
        elif op == "OR":
            state[wire] = state[w1] or state[w2]

    zk = reversed(sorted(list(filter(lambda k: k[0] == "z", state.keys()))))
    binary = "".join([str(state[k]) for k in zk])
    return int(binary, 2)


def compute(inputs, connections):
    state = {}
    for wire, value in inputs:
        state[wire] = value

    unresolved = deque(connections.items())
    while len(unresolved) > 0:
        wire, (w1, op, w2) = unresolved.popleft()
        if w1 not in state or w2 not in state:
            unresolved.append(((w1, op, w2), wire))
            continue
        elif op == "AND":
            state[wire] = state[w1] and state[w2]
        elif op == "XOR":
            state[wire] = state[w1] ^ state[w2]
        elif op == "OR":
            state[wire] = state[w1] or state[w2]

    return state


def get_binary(state, char):
    raw = reversed(sorted(list(filter(lambda k: k[0] == char, state.keys()))))
    return "".join([str(state[r]) for r in raw])


def solve2(data):
    inputs, connections = data
    zKeys = list(filter(lambda c: c[0] == "z", [c[1] for c in connections]))
    zKey_combo = list(combinations(zKeys, 4))

    for combo in zKey_combo:
        pairs = list(combinations(combo, 2))
        for k1, k2 in pairs:
            swapped_conns = connections.copy()
            print(k1, k2)

        exit()
        state = compute(inputs, connections)

        x = get_binary(state, "x")
        y = get_binary(state, "y")
        z = get_binary(state, "z")
        print("x", x, int(x, 2))
        print("y", y, int(y, 2))
        print("z", z, int(z, 2))

    return 0


print("🎄 Day 0: Crossed Wires")
# print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
