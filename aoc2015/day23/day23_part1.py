from os.path import join, dirname, realpath

INSTRUCTION_LIST = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        INSTRUCTION_LIST.append(line.strip())


def run_instructions(instructions):
    regs = {"a": 0, "b": 0}
    ip = 0
    while 0 <= ip < len(instructions):
        instr = instructions[ip][0:3]
        rest = instructions[ip][4:]
        if instr == "hlf":
            regs[rest] //= 2
            ip += 1
        elif instr == "tpl":
            regs[rest] *= 3
            ip += 1
        elif instr == "inc":
            regs[rest] += 1
            ip += 1
        elif instr == "jmp":
            ip += int(rest)
        elif instr == "jie":
            rest = rest.split(", ")
            reg = rest[0]
            offset = int(rest[1])
            if regs[reg] % 2:
                ip += 1
            else:
                ip += offset
        elif instr == "jio":
            rest = rest.split(", ")
            reg = rest[0]
            offset = int(rest[1])
            if regs[reg] == 1:
                ip += offset
            else:
                ip += 1
        else:
            raise ValueError("Unknown instruction: {}".format(instr))
    print(regs)


if __name__ == '__main__':
    run_instructions(INSTRUCTION_LIST)
