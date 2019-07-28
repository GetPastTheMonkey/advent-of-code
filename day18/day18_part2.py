from os.path import join, dirname, realpath

import numpy as np

SIZE = (50, 50)
OPEN_GROUND, TREE, LUMBERYARD = 0, 1, 2
translate = {
    ".": OPEN_GROUND,
    "|": TREE,
    "#": LUMBERYARD
}

simulation = np.zeros(SIZE, dtype="u1")

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    row = 0
    for line in f:
        col = 0
        for char in line:
            if char == '\n':
                break
            simulation[row][col] = translate[char]
            col += 1
        row += 1


def count_elems(center_x, center_y, comp):
    ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in ADJACENTS:
        if 0 <= center_x + dx < SIZE[0] and 0 <= center_y + dy < SIZE[1]:
            if simulation[center_y + dy][center_x + dx] == comp:
                count += 1
    return count


def step():
    new_simulation = np.copy(simulation)

    for y, x in np.ndindex(SIZE):
        if simulation[y][x] == OPEN_GROUND:
            if count_elems(x, y, TREE) >= 3:
                new_simulation[y][x] = TREE
        elif simulation[y][x] == TREE:
            if count_elems(x, y, LUMBERYARD) >= 3:
                new_simulation[y][x] = LUMBERYARD
        elif simulation[y][x] == LUMBERYARD:
            if count_elems(x, y, LUMBERYARD) < 1 or count_elems(x, y, TREE) < 1:
                new_simulation[y][x] = OPEN_GROUND

    return new_simulation


def calculate_value():
    tree_count, lumberyard_count = 0, 0
    for y, x in np.ndindex(SIZE):
        if simulation[y][x] == TREE:
            tree_count += 1
        elif simulation[y][x] == LUMBERYARD:
            lumberyard_count += 1

    return tree_count * lumberyard_count


seen_steps = dict()
prev = None
MAX_ITERATION = 1_000_000_000
i = 0
while i < MAX_ITERATION:
    print("Starting iteration {} or {}".format(i, MAX_ITERATION))

    # Do iteration
    simulation = step()
    value = calculate_value()

    # Check if cycle exists
    cycle = i - seen_steps.get(value, 0)
    if prev == cycle:
        print("Found cycle of length {}".format(cycle))
        i = MAX_ITERATION - ((MAX_ITERATION - i) % cycle)
        print("Increased iteration to {} of {}".format(i, MAX_ITERATION))
        seen_steps = dict()  # Reset seen steps to find new cycles

    # Update for next iteration
    prev = cycle
    seen_steps[value] = i
    i += 1

print("The value of the final iteration is: {}".format(calculate_value()))
