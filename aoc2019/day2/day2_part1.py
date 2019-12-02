from os.path import join, dirname, realpath


def run_step(ints, opcode_index):
    stop = False
    opcode = ints[opcode_index]

    if len(ints) > opcode_index + 3:
        arg1, arg2, res = ints[opcode_index + 1: opcode_index + 4]
    else:
        arg1, arg2, res = None, None, None

    if opcode == 1:
        ints[res] = ints[arg1] + ints[arg2]
    elif opcode == 2:
        ints[res] = ints[arg1] * ints[arg2]
    elif opcode == 99:
        stop = True
    else:
        raise ValueError("Invalid opcode {}".format(opcode))

    return ints, stop


def run(ints):
    should_stop = False
    opcode_index = 0
    while not should_stop:
        ints, should_stop = run_step(ints, opcode_index)
        opcode_index += 4

    print(ints)
    print("Solution: {}".format(ints[0]))


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    integers = list(map(int, f.readline().split(",")))

    # Modifications for part 1
    integers[1] = 12
    integers[2] = 2

run(integers)
