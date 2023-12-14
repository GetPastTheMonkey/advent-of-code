from copy import deepcopy

from aoc2023.day13.day13_common import get_grids, find_mirrors, scoring


def main():
    s = 0

    for grid in get_grids():
        old_horizontal, old_vertical = find_mirrors(grid)
        found = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Copy grid and alter position (i, j)
                altered_grid = deepcopy(grid)
                altered_grid[i][j] = not altered_grid[i][j]

                new_horizontal, new_vertical = find_mirrors(altered_grid)
                has_new_horizontal = any(el not in old_horizontal for el in new_horizontal)
                has_new_vertical = any(el not in old_vertical for el in new_vertical)

                if has_new_horizontal or has_new_vertical:
                    h = list(set(new_horizontal).difference(set(old_horizontal)))
                    v = list(set(new_vertical).difference(set(old_vertical)))
                    s += scoring(h, v)
                    found = True
                    break

            if found:
                break

    print(s)


if __name__ == '__main__':
    main()
