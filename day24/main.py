from collections import deque


def parseData(name="task"):
    left, right = open(f"{name}.txt").read().split("\n\n")
    inputs = [tuple(i.split(": ")) for i in left.splitlines()]
    connections = [tuple(c.split(" -> ")) for c in right.splitlines()]
    return (
        [(k, int(v)) for k, v in inputs],
        [(tuple(k.split()), v) for k, v in connections],
    )


def solve1(data):
    inputs, connections = data

    state = {}
    for wire, value in inputs:
        state[wire] = value

    unresolved = deque(connections)
    while len(unresolved) > 0:
        (w1, op, w2), wire = unresolved.popleft()
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


def solve2(data):
    inputs, connections = data

    state = {}
    for wire, value in inputs:
        state[wire] = value

    unresolved = deque(connections)
    while len(unresolved) > 0:
        (w1, op, w2), wire = unresolved.popleft()
        print("Resolving wire:", wire)

        if w1 not in state or w2 not in state:
            print("~~> Requeued")
            unresolved.append(((w1, op, w2), wire))
            continue

        outcome = 0
        if op == "AND":
            outcome = state[w1] and state[w2]
        elif op == "XOR":
            outcome = state[w1] ^ state[w2]
        elif op == "OR":
            outcome = state[w1] or state[w2]

        print("--> Outcome:", outcome)
        state[wire] = outcome

    zk = reversed(sorted(list(filter(lambda k: k[0] == "z", state.keys()))))
    binary = "".join([str(state[k]) for k in zk])
    return (binary, int(binary, 2))


print("🎄 Day 0: Crossed Wires")
print("Part 1:", solve1(parseData("sample")))
# print(f"Part 2:", solve(parseData("sample")))
