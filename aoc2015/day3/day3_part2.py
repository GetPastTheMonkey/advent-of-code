from os.path import join, dirname, realpath

DIRECTIONS = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0)
}

santas_position = (0, 0)
robots_position = (0, 0)
santas_turn = True
visited = set()
visited.add(santas_position)

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for direction in f.read():
        position = santas_position if santas_turn else robots_position
        position = (position[0] + DIRECTIONS[direction][0], position[1] + DIRECTIONS[direction][1])
        visited.add(position)
        if santas_turn:
            santas_position = position
        else:
            robots_position = position
        santas_turn = not santas_turn

print(len(visited))
