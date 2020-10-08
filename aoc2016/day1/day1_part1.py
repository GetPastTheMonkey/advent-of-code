from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    instructions = f.readline().strip().split(", ")

directions = [
    (1, 0),  # Up
    (0, 1),  # Right
    (-1, 0),  # Down
    (0, -1)  # Left
]
direction = 0
point = [0, 0]

for instr in instructions:
    if instr[0] == "R":
        direction += 1
    else:
        direction -= 1
    direction %= len(directions)

    point = tuple(int(instr[1:]) * d + pt for pt, d in zip(point, directions[direction]))

print(sum(map(abs, point)))
