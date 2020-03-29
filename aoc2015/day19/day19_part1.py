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

for find, replace in replacement_rules:
    indices = [m.start() for m in re.finditer(find, starting_word)]
    new_molecules.update([starting_word[:i] + replace + starting_word[i + len(find):] for i in indices])

print(len(new_molecules))
