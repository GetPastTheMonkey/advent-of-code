from copy import deepcopy
from os.path import join, dirname, realpath
from re import match

from day16.instruction_set import instruction_list


def parse_file():
    with open(join(dirname(realpath(__file__)), "input.txt")) as f:
        result = []
        current_operation = {}
        for i, line in enumerate(f):
            if i % 4 == 0:
                # Register values before
                m = match("Before: \[(?P<a>\d+), (?P<b>\d+), (?P<c>\d+), (?P<d>\d+)\]", line)
                if not m:
                    break
                a = int(m.group("a"))
                b = int(m.group("b"))
                c = int(m.group("c"))
                d = int(m.group("d"))
                current_operation["registers_in"] = [a, b, c, d]
            elif i % 4 == 1:
                # Machine instruction
                m = match("(?P<a>\d+) (?P<b>\d+) (?P<c>\d+) (?P<d>\d+)", line)
                if not m:
                    break
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
                result.append(deepcopy(current_operation))
    return result


samples = parse_file()

counter = 0

for sample in samples:
    sample_count = 0
    for instruction in instruction_list:
        _, a, b, c = tuple(sample["operation"])
        test = instruction(sample["registers_in"], a, b, c)
        if test == sample["registers_out"]:
            sample_count += 1
    if sample_count >= 3:
        counter += 1

print "There were {} samples with 3 or more opcodes".format(counter)
