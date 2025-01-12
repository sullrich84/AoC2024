def parseData(name="task"):
    left, right = open(f"{name}.txt").read().split("\n\n")

    register = {}
    for line in left.splitlines():
        _, key, val = line.replace(":", "").split()
        register[key] = int(val)

    output = right.split()[1].split(",")
    program = list(map(int, output))

    return (register, program)


def combo(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b

    return c

def solve1(register, program):
    a, b, c = register.values()

    pointer = 0
    output = []

    while pointer < len(program):
        ins = program[pointer]
        operand = program[pointer + 1]
        if ins == 0:
            a = a >> combo(operand, a, b, c)
        elif ins == 1:
            b = b ^ operand
        elif ins == 2:
            b = combo(operand, a, b, c) % 8
        elif ins == 3:
            if a != 0:
                pointer = operand
                continue
        elif ins == 4:
            b = b ^ c
        elif ins == 5:
            output.append(combo(operand, a, b, c) % 8)
        elif ins == 6:
            b = a >> combo(operand, a, b, c)
        elif ins == 7:
            c = a >> combo(operand, a, b, c)
        pointer += 2

    nums = list(map(str, output))
    return ",".join(nums)


def solve2(_, program):
    def find(target, ans):
        if target == []:
            return ans
        for t in range(8):
            a = ans << 3 | t
            b, c = 0, 0
            output = None

            for pointer in range(0, len(program) - 2, 2):
                ins = program[pointer]
                operand = program[pointer + 1]
                if ins == 1:
                    b = b ^ operand
                elif ins == 2:
                    b = combo(operand, a, b, c) % 8
                elif ins == 4:
                    b = b ^ c
                elif ins == 5:
                    output = combo(operand, a, b, c) % 8
                elif ins == 6:
                    b = a >> combo(operand, a, b, c)
                elif ins == 7:
                    c = a >> combo(operand, a, b, c)

                if output == target[-1]:
                    sub = find(target[:-1], a)
                    if sub is not None:
                        return sub

    return find(program, 0)


print("🎄 Day 17: Chronospatial Computer")
print("Part 1:", solve1(*parseData("task")))
print("Part 2:", solve2(*parseData("task")))
