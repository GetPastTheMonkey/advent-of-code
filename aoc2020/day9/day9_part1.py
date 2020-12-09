from itertools import combinations

from utils import get_input_lines

consider = 25
choose = 2
ints = []

for line in get_input_lines(__file__):
    i = int(line)
    if len(ints) == consider:
        comb = combinations(ints, choose)
        if all([sum(x) != i for x in comb]):
            print(i)
            break
        ints.pop(0)
    ints.append(i)
