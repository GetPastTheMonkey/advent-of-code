from os.path import join, dirname, realpath

from aoc2019.day9.intcode import IntcodeComputer

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    instructions = map(int, f.readline().split(","))

cp = IntcodeComputer(inp=1, clear_input=False)
cp.run(instructions)
print(cp.get_output())
