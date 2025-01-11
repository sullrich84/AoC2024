def parseData(name="task"):
    left, right = open(f"{name}.txt").read().split("\n\n")

    register = {}
    for line in left.splitlines():
        _, key, val = line.replace(":", "").split()
        register[key] = int(val)
   
    output = right.split()[1].split(",")
    program = list(map(int, output))

    return (register, program)


def solve(register, program):
    print(register)
    print(program)

    return 0


print("🎄 Day 17: Chronospatial Computer")
print("Part 1:", solve(*parseData("sample")))
# print(f"Part 2:", solve(*parseData("sample")))
