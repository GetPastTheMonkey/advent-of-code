from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    instructions = map(int, f.readline().split(","))

"""
instructions = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
"""


def get_value(instr, address, mode, position):
    mode = map(int, str(mode))
    try:
        if mode[position] == 1:
            return address
    except IndexError:
        pass
    return instr[address]


def get_input():
    return 5


def put_output(o):
    print(o)


def run_step(instr_ptr, instr):
    opcode_mode = instr[instr_ptr]
    opcode = opcode_mode % 100
    mode = opcode_mode // 100

    should_stop = False

    if opcode == 1:
        op1 = get_value(instr, instr[instr_ptr + 1], mode, -1)
        op2 = get_value(instr, instr[instr_ptr + 2], mode, -2)
        instr[instr[instr_ptr + 3]] = op1 + op2
        instr_ptr += 4
    elif opcode == 2:
        op1 = get_value(instr, instr[instr_ptr + 1], mode, -1)
        op2 = get_value(instr, instr[instr_ptr + 2], mode, -2)
        instr[instr[instr_ptr + 3]] = op1 * op2
        instr_ptr += 4
    elif opcode == 3:
        instr[instr[instr_ptr + 1]] = get_input()
        instr_ptr += 2
    elif opcode == 4:
        put_output(get_value(instr, instr[instr_ptr + 1], mode, -1))
        instr_ptr += 2
    elif opcode == 5:
        check = get_value(instr, instr[instr_ptr + 1], mode, -1)
        if check == 0:
            instr_ptr += 3
        else:
            instr_ptr = get_value(instr, instr[instr_ptr + 2], mode, -2)
    elif opcode == 6:
        check = get_value(instr, instr[instr_ptr + 1], mode, -1)
        if check == 0:
            instr_ptr = get_value(instr, instr[instr_ptr + 2], mode, -2)
        else:
            instr_ptr += 3
    elif opcode == 7:
        left = get_value(instr, instr[instr_ptr + 1], mode, -1)
        right = get_value(instr, instr[instr_ptr + 2], mode, -2)
        instr[instr[instr_ptr + 3]] = 1 if left < right else 0
        instr_ptr += 4
    elif opcode == 8:
        left = get_value(instr, instr[instr_ptr + 1], mode, -1)
        right = get_value(instr, instr[instr_ptr + 2], mode, -2)
        instr[instr[instr_ptr + 3]] = 1 if left == right else 0
        instr_ptr += 4
    elif opcode == 99:
        should_stop = True
    else:
        raise ValueError("Encountered unknown opcode {}. Terminating immediately!".format(opcode))

    return instr_ptr, instr, should_stop


def run(instr):
    instruction_pointer = 0
    should_stop = False
    while not should_stop:
        instruction_pointer, instr, should_stop = run_step(instruction_pointer, instr)


run(instructions)
