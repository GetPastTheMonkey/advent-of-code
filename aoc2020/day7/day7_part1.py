from utils import get_input_lines

contained_in = dict()
bags = set()

for line in get_input_lines(__file__):
    lhs, rhs = line.split(" contain ")
    top_bag = " ".join(lhs.split(" ")[:2])

    bags.add(top_bag)

    for r in rhs.split(", "):
        if r[:2] == "no":
            continue

        bottom_bag = " ".join(r.split(" ")[1:3])

        if bottom_bag not in contained_in:
            contained_in[bottom_bag] = set()

        contained_in[bottom_bag].add(top_bag)

for bag in bags.difference(contained_in.keys()):
    contained_in[bag] = set()

bags_iterated = set()
bags_to_iterate = {"shiny gold"}
reachability = 0

while len(bags_to_iterate) > 0:
    bag = bags_to_iterate.pop()
    if bag in bags_iterated:
        continue
    bags_iterated.add(bag)

    for bag2 in contained_in[bag]:
        if bag2 not in bags_iterated.union(bags_to_iterate):
            reachability += 1
            bags_to_iterate.add(bag2)

print(reachability)
