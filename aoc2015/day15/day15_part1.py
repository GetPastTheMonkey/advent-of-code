from collections import namedtuple
from itertools import product, ifilter
from os.path import join, dirname, realpath

Ingredient = namedtuple("Ingredient", ["capacity", "durability", "flavor", "texture"])
ingredients = []

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        line_split = line.strip().split()
        ingredients.append(Ingredient(
            capacity=int(line_split[2][:-1]),
            durability=int(line_split[4][:-1]),
            flavor=int(line_split[6][:-1]),
            texture=int(line_split[8][:-1])
        ))

max_value = 0
candidates = ifilter(lambda x: sum(x) == 100, product(range(101), repeat=len(ingredients)))
for candidate in candidates:
    candidate_cookie = Ingredient(0, 0, 0, 0)
    for i in range(len(candidate)):
        candidate_cookie = Ingredient(
            candidate_cookie.capacity + candidate[i] * ingredients[i].capacity,
            candidate_cookie.durability + candidate[i] * ingredients[i].durability,
            candidate_cookie.flavor + candidate[i] * ingredients[i].flavor,
            candidate_cookie.texture + candidate[i] * ingredients[i].texture
        )

    if any(x <= 0 for x in candidate_cookie):
        continue

    candidate_value = reduce(lambda x, y: x * y, candidate_cookie)
    if candidate_value > max_value:
        max_value = candidate_value

print(max_value)
