from itertools import permutations
from os.path import join, dirname, realpath

from aoc2019.day7.intcode import IntcodeComputer

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    instructions = list(map(int, f.readline().split(",")))

possible_phases = [5, 6, 7, 8, 9]
largest_boost = 0

for permutation in permutations(possible_phases):
    amp0 = IntcodeComputer(phase=permutation[0])
    amp1 = IntcodeComputer(phase=permutation[1])
    amp2 = IntcodeComputer(phase=permutation[2])
    amp3 = IntcodeComputer(phase=permutation[3])
    amp4 = IntcodeComputer(phase=permutation[4])

    amps = [amp0, amp1, amp2, amp3, amp4]

    amp0.set_input(0)

    for i in range(len(amps)):
        current_amp = amps[i]
        next_amp = amps[(i + 1) % len(amps)]
        current_amp.run(instructions)
        next_amp.set_input(current_amp.get_output())

    while not all(map(lambda x: x.finished, amps)):
        for i in range(len(amps)):
            current_amp = amps[i]
            next_amp = amps[(i + 1) % len(amps)]

            current_amp.resume()
            next_amp.set_input(current_amp.get_output())

    if amp4.get_output() > largest_boost:
        largest_boost = amp4.get_output()

print("Largest possible boost: {}".format(largest_boost))
