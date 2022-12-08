from utils import get_input_lines


def load_grid():
    grid = []
    for line in get_input_lines(__file__):
        line = list(map(int, (x for x in line)))
        grid.append(line)

    rows = len(grid)
    cols = len(grid[0])
    return grid, rows, cols
