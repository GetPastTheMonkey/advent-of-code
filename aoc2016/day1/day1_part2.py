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
point = (0, 0)
visited = set()
visited.add(point)
solution = None

for instr in instructions:
    if instr[0] == "R":
        direction += 1
    else:
        direction -= 1
    direction %= len(directions)

    for i in range(int(instr[1:])):
        point = tuple(pt_coord + change for pt_coord, change in zip(point, directions[direction]))
        if point in visited:
            solution = sum(map(abs, point))
            break
        visited.add(point)

    if solution is not None:
        break

print(solution)
