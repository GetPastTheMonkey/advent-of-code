from typing import Dict, Tuple

from utils import get_input_lines

grid = dict()
FLOOR = 0
FREE = 1
OCCUPIED = 2
x = 0
y = 0

for row in get_input_lines(__file__):
    x = 0
    for char in row:
        grid[(x, y)] = FLOOR if char == "." else FREE
        x += 1
    y += 1

cols = x
rows = y


def count_adjacent_occupied(x_: int, y_: int, grid_: Dict[Tuple[int, int], int]) -> int:
    count = 0
    for x_d in [-1, 0, 1]:
        for y_d in [-1, 0, 1]:
            if x_d == 0 and y_d == 0:
                # Don't count own field, only neighbours
                continue
            if grid_.get((x_ + x_d, y_ + y_d), -1) == OCCUPIED:
                count += 1
    return count


changed = True
while changed:
    new_grid = dict()
    changed = False

    for y in range(rows):
        for x in range(cols):
            if grid[(x, y)] == FREE and count_adjacent_occupied(x, y, grid) == 0:
                new_grid[(x, y)] = OCCUPIED
                changed = True
            elif grid[(x, y)] == OCCUPIED and count_adjacent_occupied(x, y, grid) >= 4:
                new_grid[(x, y)] = FREE
                changed = True
            else:
                new_grid[(x, y)] = grid[(x, y)]

    grid = new_grid

occ = 0
for y in range(rows):
    for x in range(cols):
        if grid[(x, y)] == OCCUPIED:
            occ += 1
print(occ)
