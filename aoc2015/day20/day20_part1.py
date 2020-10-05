from os.path import join, dirname, realpath

import numpy as np

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    max_house_nr = int(f.read())

presents_per_elf = 10
max_house_nr //= presents_per_elf
houses = np.zeros(max_house_nr)
house_nr = max_house_nr

for elf in range(1, max_house_nr):
    for house in range(elf, max_house_nr, elf):
        houses[house] += elf
        if houses[house] >= max_house_nr and house < house_nr:
            house_nr = house

print(house_nr)
