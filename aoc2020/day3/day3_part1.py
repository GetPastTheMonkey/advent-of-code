from utils import get_input_lines

line_length = 0
x_pos = 0
tree_count = 0

for line in get_input_lines(__file__):
    if line_length == 0:
        line_length = len(line)

    if line[x_pos] == "#":
        tree_count += 1

    x_pos = (x_pos + 3) % line_length

print(tree_count)
