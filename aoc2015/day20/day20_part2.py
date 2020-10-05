from os.path import join, dirname, realpath

import numpy as np

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    max_house_nr = int(f.read())

presents_per_elf = 11
max_visits = 50
max_house_nr //= presents_per_elf
houses = np.zeros(max_house_nr)
house_nr = max_house_nr

for elf in range(1, max_house_nr):
    visits = 0
    for house in range(elf, max_house_nr, elf):
        visits += 1
        houses[house] += elf
        if houses[house] >= max_house_nr and house < house_nr:
            house_nr = house
        if visits >= max_visits:
            break

print(house_nr)
