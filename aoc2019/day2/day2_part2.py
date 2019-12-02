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
    return ints[0]


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    original_integers = list(map(int, f.readline().split(",")))


for i in range(100):
    for j in range(100):
        integers = original_integers.copy()
        integers[1] = i
        integers[2] = j

        result = run(integers)

        if result == 19690720:
            print("Solution found for noun={} and verb={}. Solution is therefore: {}".format(i, j, 100*i+j))
