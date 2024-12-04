from aoc2024.day4.day4_common import day4_input


def main():
    grid = day4_input()
    word = "XMAS"
    s = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == word[0]:
                for dir_x in [-1, 0, 1]:
                    for dir_y in [-1, 0, 1]:
                        found = True

                        for l in range(1, len(word)):
                            x_coord = x + l * dir_x
                            y_coord = y + l * dir_y

                            valid_x = 0 <= x_coord < len(grid)
                            valid_y = 0 <= y_coord < len(grid[0])

                            if not (valid_x and valid_y) or grid[x_coord][y_coord] != word[l]:
                                found = False
                                break

                        if found:
                            s += 1

    print(s)


if __name__ == '__main__':
    main()
