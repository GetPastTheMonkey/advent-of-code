from utils import get_input_lines


def is_int(grid: list[list[str]], i, j) -> bool:
    try:
        return grid[i][j].isdigit()
    except IndexError:
        return False


def get_number(grid: list[list[str]], i, j) -> int:
    number = [grid[i][j]]

    # Explore to the left
    col = j - 1

    while is_int(grid, i, col):
        number = [grid[i][col]] + number
        col -= 1

    # Explore to the right
    col = j + 1

    while is_int(grid, i, col):
        number.append(grid[i][col])
        col += 1

    return int("".join(number))


def main():
    s = 0
    grid = []  # type: list[list[str]]

    for line in get_input_lines(__file__):
        grid.append([c for c in line])

    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        for j in range(width):
            if grid[i][j] != "*":
                continue

            num_numbers = 0
            number = 1

            # Check if number above
            if is_int(grid, i - 1, j):
                num_numbers += 1
                number *= get_number(grid, i - 1, j)
            else:
                if is_int(grid, i - 1, j - 1):
                    num_numbers += 1
                    number *= get_number(grid, i - 1, j - 1)
                if is_int(grid, i - 1, j + 1):
                    num_numbers += 1
                    number *= get_number(grid, i - 1, j + 1)

            # Check if number to the left
            if is_int(grid, i, j - 1):
                num_numbers += 1
                number *= get_number(grid, i, j - 1)

            # Check if number to the right
            if is_int(grid, i, j + 1):
                num_numbers += 1
                number *= get_number(grid, i, j + 1)

            # Check if number below
            if is_int(grid, i + 1, j):
                num_numbers += 1
                number *= get_number(grid, i + 1, j)
            else:
                if is_int(grid, i + 1, j - 1):
                    num_numbers += 1
                    number *= get_number(grid, i + 1, j - 1)
                if is_int(grid, i + 1, j + 1):
                    num_numbers += 1
                    number *= get_number(grid, i + 1, j + 1)

            if num_numbers == 2:
                s += number

    print(s)


if __name__ == '__main__':
    main()
