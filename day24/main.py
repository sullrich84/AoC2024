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

    def make_wire(char, num):
        return char + str(num).rjust(2, "0")

    def verify_z(wire, num):
        if wire not in connections:
            return False

        w1, op, y = connections[wire]
        if op != "XOR":
            return False

        if num == 0:
            return sorted([w1, y]) == ["x00", "y00"]

        return (
            verify_intermediate_xor(w1, num)
            and verify_carry_bit(y, num)
            or verify_intermediate_xor(y, num)
            and verify_carry_bit(w1, num)
        )

    def verify_intermediate_xor(wire, num):
        if wire not in connections:
            return False

        w1, op, y = connections[wire]
        if op != "XOR":
            return False

        return sorted([w1, y]) == [make_wire("x", num), make_wire("y", num)]

    def verify_carry_bit(wire, num):
        if wire not in connections:
            return False

        w1, op, w2 = connections[wire]
        if num == 1:
            if op != "AND":
                return False
            return sorted([w1, w2]) == ["x00", "y00"]

        if op != "OR":
            return False

        return (
            verify_direct_carry(w1, num - 1)
            and verify_recarry(w2, num - 1)
            or verify_direct_carry(w2, num - 1)
            and verify_recarry(w1, num - 1)
        )

    def verify_direct_carry(wire, num):
        if wire not in connections:
            return False

        w1, op, w2 = connections[wire]
        if op != "AND":
            return False

        return sorted([w1, w2]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        if wire not in connections:
            return False

        w1, op, y = connections[wire]
        if op != "AND":
            return False

        return (
            verify_intermediate_xor(w1, num)
            and verify_carry_bit(y, num)
            or verify_intermediate_xor(y, num)
            and verify_carry_bit(w1, num)
        )

    def verify(num):
        return verify_z(make_wire("z", num), num)

    def progress():
        i = 0
        while True:
            if not verify(i):
                break
            i += 1
        return i

    swaps = []

    for _ in range(4):
        baseline = progress()
        for w1 in connections:
            for w2 in connections:
                if w1 == w2:
                    continue
                connections[w1], connections[w2] = connections[w2], connections[w1]
                if progress() > baseline:
                    break
                connections[w1], connections[w2] = connections[w2], connections[w1]
            else:
                continue
            break
        swaps += [w1, w2]

    return ",".join(sorted(swaps))


print("🎄 Day 0: Crossed Wires")
# print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("task")))
