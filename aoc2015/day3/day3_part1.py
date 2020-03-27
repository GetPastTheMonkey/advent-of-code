from os.path import join, dirname, realpath

DIRECTIONS = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0)
}

position = (0, 0)
visited = set()
visited.add(position)

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for direction in f.read():
        position = (position[0] + DIRECTIONS[direction][0], position[1] + DIRECTIONS[direction][1])
        visited.add(position)

print(len(visited))
