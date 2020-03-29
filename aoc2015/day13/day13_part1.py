from itertools import permutations
from os.path import join, dirname, realpath

happiness_map = dict()

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        line_split = line.strip()[:-1].split()
        person_a = line_split[0]
        person_b = line_split[-1]
        happiness_change = int(line_split[3])

        if line_split[2] == "lose":
            happiness_change *= -1

        if person_a not in happiness_map:
            happiness_map[person_a] = dict()

        happiness_map[person_a][person_b] = happiness_change

candidates = permutations(happiness_map.keys())
max_happiness = 0

for candidate in candidates:
    candidate_happiness = 0
    candidate_count = len(candidate)
    for i in range(candidate_count):
        candidate_happiness += happiness_map[candidate[i]][candidate[(i - 1) % candidate_count]] +\
                               happiness_map[candidate[i]][candidate[(i + 1) % candidate_count]]

    if candidate_happiness > max_happiness:
        max_happiness = candidate_happiness

print(max_happiness)
