from utils import get_input_lines

pos_x = 0
pos_y = 0

heading_idx = 0
headings = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

for line in get_input_lines(__file__):
    action = line[0]
    n = int(line[1:])

    # Handle actions
    if action == "N":
        pos_y += n
    elif action == "S":
        pos_y -= n
    elif action == "E":
        pos_x += n
    elif action == "W":
        pos_x -= n
    elif action == "L":
        turns = n // 90
        heading_idx = (heading_idx + turns) % len(headings)
    elif action == "R":
        turns = n // 90
        heading_idx = (heading_idx - turns) % len(headings)
    elif action == "F":
        h = headings[heading_idx]
        pos_x += n * h[0]
        pos_y += n * h[1]
    else:
        raise NotImplementedError(f"Unknown action '{action}'")

print(abs(pos_x) + abs(pos_y))
