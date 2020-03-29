from os.path import join, dirname, realpath

iterations = 100
grid = set()
grid_size = 100

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    y = 0
    for line in f:
        x = 0
        for char in line.strip():
            if char == "#":
                grid.add((x, y))
            x += 1
        y += 1


def nr_lit_neightbours(g, i, j):
    nr = 0
    if (i - 1, j - 1) in g:
        nr += 1
    if (i - 1, j) in g:
        nr += 1
    if (i - 1, j + 1) in g:
        nr += 1
    if (i, j - 1) in g:
        nr += 1
    if (i, j + 1) in g:
        nr += 1
    if (i + 1, j - 1) in g:
        nr += 1
    if (i + 1, j) in g:
        nr += 1
    if (i + 1, j + 1) in g:
        nr += 1
    return nr


for it in range(iterations):
    new_grid = set()

    for x in range(grid_size):
        for y in range(grid_size):
            neighbours = nr_lit_neightbours(grid, x, y)
            if neighbours == 3 or (neighbours == 2 and (x, y) in grid):
                new_grid.add((x, y))

    grid = new_grid

print(len(grid))
