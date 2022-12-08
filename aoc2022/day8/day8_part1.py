from aoc2022.day8.day8_common import load_grid


def main():
    grid, rows, cols = load_grid()

    visible = set()

    for row_idx in range(rows):
        curr_largest = -1
        for col_idx in range(cols):
            if curr_largest < grid[row_idx][col_idx]:
                curr_largest = grid[row_idx][col_idx]
                visible.add((row_idx, col_idx))

    for row_idx in range(rows):
        curr_largest = -1
        for col_idx in range(cols - 1, -1, -1):
            if curr_largest < grid[row_idx][col_idx]:
                curr_largest = grid[row_idx][col_idx]
                visible.add((row_idx, col_idx))

    for col_idx in range(cols):
        curr_largest = -1
        for row_idx in range(rows):
            if curr_largest < grid[row_idx][col_idx]:
                curr_largest = grid[row_idx][col_idx]
                visible.add((row_idx, col_idx))

    for col_idx in range(cols):
        curr_largest = -1
        for row_idx in range(rows - 1, -1, -1):
            if curr_largest < grid[row_idx][col_idx]:
                curr_largest = grid[row_idx][col_idx]
                visible.add((row_idx, col_idx))

    print(len(visible))


if __name__ == '__main__':
    main()
