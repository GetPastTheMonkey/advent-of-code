from copy import deepcopy
from os.path import join, dirname, realpath
from re import match

from day16.instruction_set import instruction_list


def parse_file():
    with open(join(dirname(realpath(__file__)), "input.txt")) as f:
        sample_results = []
        operations_results = []
        current_operation = {}
        first_part = True
        for i, line in enumerate(f):
            if first_part:
                if i % 4 == 0:
                    newline_counter = 0
                    # Register values before
                    m = match("Before: \[(?P<a>\d+), (?P<b>\d+), (?P<c>\d+), (?P<d>\d+)\]", line)
                    if not m:
                        first_part = False
                        continue
                    a = int(m.group("a"))
                    b = int(m.group("b"))
                    c = int(m.group("c"))
                    d = int(m.group("d"))
                    current_operation["registers_in"] = [a, b, c, d]
                elif i % 4 == 1:
                    # Machine instruction
                    m = match("(?P<a>\d+) (?P<b>\d+) (?P<c>\d+) (?P<d>\d+)", line)
                    if not m:
                        raise Exception
                    a = int(m.group("a"))
                    b = int(m.group("b"))
                    c = int(m.group("c"))
                    d = int(m.group("d"))
                    current_operation["operation"] = [a, b, c, d]
                elif i % 4 == 2:
                    # Register values after
                    m = match("After:  \[(?P<a>\d+), (?P<b>\d+), (?P<c>\d+), (?P<d>\d+)\]", line)
                    if not m:
                        raise Exception
                    a = int(m.group("a"))
                    b = int(m.group("b"))
                    c = int(m.group("c"))
                    d = int(m.group("d"))
                    current_operation["registers_out"] = [a, b, c, d]
                else:
                    sample_results.append(deepcopy(current_operation))
                    newline_counter += 1
            else:
                if line == "\n":
                    continue
                m = match("(?P<a>\d+) (?P<b>\d+) (?P<c>\d+) (?P<d>\d+)", line)
                if not m:
                    raise Exception
                a = int(m.group("a"))
                b = int(m.group("b"))
                c = int(m.group("c"))
                d = int(m.group("d"))
                operations_results.append([a, b, c, d])
    return sample_results, operations_results


samples, operations = parse_file()

possible_opcodes = dict()
for instruction in instruction_list:
    possible_opcodes[instruction] = set()
    for sample in samples:
        opcode, a, b, c = tuple(sample["operation"])
        test = instruction(sample["registers_in"], a, b, c)
        if test == sample["registers_out"]:
            possible_opcodes[instruction].add(opcode)

solved = False
while not solved:
    for instruction, opcode_set in possible_opcodes.items():
        if len(opcode_set) == 1:
            for instr in possible_opcodes.keys():
                if instr != instruction:
                    possible_opcodes[instr].discard(list(opcode_set)[0])

    if all(map(lambda s: len(s) == 1, possible_opcodes.values())):
        solved = True

opcodes = dict()
for instruction, opcode_set in possible_opcodes.items():
    opcodes[list(opcode_set)[0]] = instruction

registers = [0, 0, 0, 0]

for operation in operations:
    registers = opcodes[operation[0]](registers, operation[1], operation[2], operation[3])

print("The registers have the following values: {}".format(registers))
print("The solution therefore is {}".format(registers[0]))
