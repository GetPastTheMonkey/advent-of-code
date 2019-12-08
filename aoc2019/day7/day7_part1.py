from itertools import permutations
from os.path import join, dirname, realpath

from aoc2019.day7.intcode import IntcodeComputer

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    instructions = list(map(int, f.readline().split(",")))

possible_phases = [0, 1, 2, 3, 4]
largest_boost = 0

for permutation in permutations(possible_phases):
    amp0 = IntcodeComputer(phase=permutation[0], clear_input=False)
    amp1 = IntcodeComputer(phase=permutation[1], clear_input=False)
    amp2 = IntcodeComputer(phase=permutation[2], clear_input=False)
    amp3 = IntcodeComputer(phase=permutation[3], clear_input=False)
    amp4 = IntcodeComputer(phase=permutation[4], clear_input=False)

    amp0.set_input(0)
    amp0.run(instructions)
    amp1.set_input(amp0.get_output())
    amp1.run(instructions)
    amp2.set_input(amp1.get_output())
    amp2.run(instructions)
    amp3.set_input(amp2.get_output())
    amp3.run(instructions)
    amp4.set_input(amp3.get_output())
    amp4.run(instructions)

    if amp4.get_output() > largest_boost:
        largest_boost = amp4.get_output()

print("Largest possible boost: {}".format(largest_boost))
