file = open(0)

for line in file:
    if line.isspace():
        break

connections = {}

for line in file:
    x, op, y, z = line.replace(" -> ", " ").split()
    connections[z] = (x, op, y)


def make_wire(char, num):
    return char + str(num).rjust(2, "0")


def verify_z(wire, num):
    if wire not in connections:
        return False

    x, op, y = connections[wire]
    if op != "XOR":
        return False

    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]

    return (
        verify_intermediate_xor(x, num)
        and verify_carry_bit(y, num)
        or verify_intermediate_xor(y, num)
        and verify_carry_bit(x, num)
    )


def verify_intermediate_xor(wire, num):
    if wire not in connections:
        return False

    x, op, y = connections[wire]
    if op != "XOR":
        return False

    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]


def verify_carry_bit(wire, num):
    if wire not in connections:
        return False

    x, op, y = connections[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]

    if op != "OR":
        return False

    return (
        verify_direct_carry(x, num - 1)
        and verify_recarry(y, num - 1)
        or verify_direct_carry(y, num - 1)
        and verify_recarry(x, num - 1)
    )


def verify_direct_carry(wire, num):
    if wire not in connections:
        return False

    x, op, y = connections[wire]
    if op != "AND":
        return False

    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]


def verify_recarry(wire, num):
    if wire not in connections:
        return False

    x, op, y = connections[wire]
    if op != "AND":
        return False

    return (
        verify_intermediate_xor(x, num)
        and verify_carry_bit(y, num)
        or verify_intermediate_xor(y, num)
        and verify_carry_bit(x, num)
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
    for x in connections:
        for y in connections:
            if x == y:
                continue
            connections[x], connections[y] = connections[y], connections[x]
            if progress() > baseline:
                break
            connections[x], connections[y] = connections[y], connections[x]
        else:
            continue
        break
    swaps += [x, y]

print(",".join(sorted(swaps)))
