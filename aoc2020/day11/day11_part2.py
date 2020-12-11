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

            x_d_original = x_d
            while True:
                val = grid_.get((x_ + x_d, y_ + y_d), -1)
                if val == -1 or val == FREE:
                    # Hit a free seat or ran out of grid
                    break
                elif grid_.get((x_ + x_d, y_ + y_d), -1) == OCCUPIED:
                    # Hit an occupied seat
                    count += 1
                    break
                else:
                    # Hit floor
                    if x_d < 0:
                        x_d -= 1
                    elif x_d > 0:
                        x_d += 1

                    if y_d < 0:
                        y_d -= 1
                    elif y_d > 0:
                        y_d += 1

            # Reset changed x_d. No need to reset y_d as it is set by the next for loop iteration
            x_d = x_d_original
    return count


def print_grid(grid_: Dict[Tuple[int, int], int], rows_: int, cols_: int):
    print("-" * cols_)
    for y_ in range(rows_):
        row_str = []
        for x_ in range(cols_):
            if grid_[(x_, y_)] == FLOOR:
                row_str.append(".")
            elif grid_[(x_, y_)] == FREE:
                row_str.append("L")
            else:
                row_str.append("#")
        print("".join(row_str))
    print("-" * cols_)


changed = True
while changed:
    new_grid = dict()
    changed = False

    for y in range(rows):
        for x in range(cols):
            occ = count_adjacent_occupied(x, y, grid)
            if grid[(x, y)] == FREE and occ == 0:
                new_grid[(x, y)] = OCCUPIED
                changed = True
            elif grid[(x, y)] == OCCUPIED and occ >= 5:
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
