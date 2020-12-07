from utils import get_input_lines

contains = dict()

for line in get_input_lines(__file__):
    lhs, rhs = line.split(" contain ")
    top_bag = " ".join(lhs.split(" ")[:2])

    contains[top_bag] = set()

    for r in rhs.split(", "):
        rsplit = r.split(" ")
        if rsplit[0] == "no":
            continue

        bottom_bag = " ".join(rsplit[1:3])
        contains[top_bag].add((int(rsplit[0]), bottom_bag))


def process(bag, rel):
    s = 0
    for count, down_bag in rel[bag]:
        s += count * (1 + process(down_bag, rel))
    return s


print(process("shiny gold", contains))
