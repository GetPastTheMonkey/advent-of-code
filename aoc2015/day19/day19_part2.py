import re
from os.path import join, dirname, realpath

replacement_rules = list()
starting_word = ""
new_molecules = set()

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        line_strip = line.strip()
        if "=>" in line_strip:
            line_split = line_strip.split(" => ")
            replacement_rules.append((line_split[0], line_split[1]))
        else:
            starting_word = line_strip

# Greedy replacement, sort rules by longest string
replacement_rules.sort(key=lambda x: len(x[1]), reverse=True)

steps = 0
while starting_word != "e":
    for replace, find in replacement_rules:
        if find in starting_word:
            starting_word = starting_word.replace(find, replace, 1)
            steps += 1
            break

print(steps)
