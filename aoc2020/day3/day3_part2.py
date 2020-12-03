from functools import reduce

from utils import get_input_lines

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

tree_count = [0] * len(slopes)
x_pos = [0] * len(slopes)
line_length = 0

for line_idx, line in enumerate(get_input_lines(__file__)):
    if line_length == 0:
        line_length = len(line)

    for idx, (slope_x, slope_y) in enumerate(slopes):
        if line_idx % slope_y == 0:
            if line[x_pos[idx]] == "#":
                tree_count[idx] += 1
            x_pos[idx] = (x_pos[idx] + slope_x) % line_length

print(reduce(lambda x, y: x * y, tree_count))
