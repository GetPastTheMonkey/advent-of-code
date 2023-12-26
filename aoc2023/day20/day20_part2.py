from aoc2023.day20.day20_common import PulsePropagation

"""
NOTES REGARDING PART 2

After manual inspection of the node network, it was observed that the output node "rx" is dependent on a conjunction
which itself is dependent on a list of nodes. Thus, to have a low signal at "rx", all input nodes of the conjunction
must emit a high signal. Luckily, all of the input nodes to the conjunction are on a cycle. Therefore, the minimum
number of button presses to receive a low signal at "rx" is the least common multiple of the cycle lengths.
"""


def main():
    pp = PulsePropagation()

    while not pp.cycles_found:
        pp.push_button()

    print(pp.cycles_lcm)


if __name__ == '__main__':
    main()
