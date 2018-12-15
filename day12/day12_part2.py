from os.path import join, dirname, realpath
from re import match


def parse_input():
    planties = set()
    with open(join(dirname(realpath(__file__)), "input.txt")) as f:
        # Parse initial config
        m = match("initial state: (?P<init>[#.]+)", f.readline())
        for i, c in enumerate(m.group("init")):
            if c == '#':
                planties.add(i)

        # Empty line
        f.readline()

        # Rest of the lines are rules
        rule_dict = {}
        for rule in f:
            m = match("(?P<in>[#.]{5}) => (?P<out>[#.])", rule)
            rule_in = [True if c == '#' else False for c in m.group("in")]
            rule_out = True if m.group("out") == '#' else False
            rule_dict[tuple(rule_in)] = rule_out
    return planties, rule_dict


def grow(p):
    new_p = set()
    for i in range(min(p)-2, max(p)+3):
        needed_rule = tuple([True if j in p else False for j in range(i-2, i+3)])
        if rules[needed_rule]:
            new_p.add(i)
    return new_p


plants, rules = parse_input()
nr_of_generations = 50000000000
gen = 0

new_sum = previous_sum = 0
new_delta = previous_delta = 0

while gen < nr_of_generations:
    plants = grow(plants)
    gen += 1

    previous_sum = new_sum
    new_sum = sum(plants)

    previous_delta = new_delta
    new_delta = new_sum - previous_sum

    if previous_delta == new_delta:
        print "[GENERATION {}] Delta stayed the same (at {})".format(gen, new_delta)
        break

final_sum = new_sum + (new_delta * (nr_of_generations - gen))

print "Sum of all plant indices is: {}".format(final_sum)
