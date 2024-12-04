from aoc2024.day4.day4_common import day4_input


def main():
    grid = day4_input()
    word = "MAS"
    s = 0

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if grid[x][y] == word[1]:
                diag_1 = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
                diag_2 = grid[x + 1][y - 1] + grid[x][y] + grid[x - 1][y + 1]

                if (diag_1 == word or diag_1[::-1] == word) and (diag_2 == word or diag_2[::-1] == word):
                    s += 1

    print(s)


if __name__ == '__main__':
    main()
