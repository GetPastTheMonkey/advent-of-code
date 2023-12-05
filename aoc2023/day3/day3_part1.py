from utils import get_input_lines


def is_symbol(grid, i, j) -> bool:
    try:
        char = grid[i][j]
        return not char.isdigit() and char != "."
    except IndexError:
        return False


def check_up_down(grid, i, j) -> bool:
    return is_symbol(grid, i - 1, j) or is_symbol(grid, i + 1, j)


def check_all(grid, i, j) -> bool:
    return check_up_down(grid, i, j) or is_symbol(grid, i, j)


def main():
    s = 0
    grid = []  # type: list[list[str]]

    for line in get_input_lines(__file__):
        grid.append([c for c in line])

    height = len(grid)
    width = len(grid[0])

    in_number = False
    number = 0
    is_part = False

    for i in range(height):
        for j in range(width):
            char = grid[i][j]

            if char.isdigit():
                # Check if a symbol is above or below
                is_part = is_part or check_up_down(grid, i, j)
                number = (10 * number) + int(char)

                if not in_number:
                    # Check if a symbol is to the left of the first number
                    is_part = is_part or check_all(grid, i, j - 1)
                    in_number = True
            else:
                if in_number:
                    # Check if a symbol is to the right of the last number
                    is_part = is_part or check_all(grid, i, j)

                    if is_part:
                        s += number

                    # Reset all state
                    number = 0
                    in_number = False
                    is_part = False

    print(s)


if __name__ == '__main__':
    main()
