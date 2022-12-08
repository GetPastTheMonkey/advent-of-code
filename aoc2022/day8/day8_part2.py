from aoc2022.day8.day8_common import load_grid


def main():
    grid, rows, cols = load_grid()

    max_visible = -1

    for row_idx in range(rows):
        for col_idx in range(cols):
            my_tree = grid[row_idx][col_idx]

            visible_down = 0
            for row_idx_look in range(row_idx + 1, rows):
                visible_down += 1
                if grid[row_idx_look][col_idx] >= my_tree:
                    break

            visible_up = 0
            for row_idx_look in range(row_idx - 1, -1, -1):
                visible_up += 1
                if grid[row_idx_look][col_idx] >= my_tree:
                    break

            visible_right = 0
            for col_idx_look in range(col_idx + 1, cols):
                visible_right += 1
                if grid[row_idx][col_idx_look] >= my_tree:
                    break

            visible_left = 0
            for col_idx_look in range(col_idx - 1, -1, -1):
                visible_left += 1
                if grid[row_idx][col_idx_look] >= my_tree:
                    break

            scenic_score = visible_right * visible_left * visible_down * visible_up
            max_visible = max(max_visible, scenic_score)

    print(max_visible)


if __name__ == '__main__':
    main()
