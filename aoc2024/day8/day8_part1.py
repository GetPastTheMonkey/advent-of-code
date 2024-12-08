from aoc2024.day8.day8_common import day8_solve, coord


def calc(a1: coord, a2: coord, height: int, width: int, antinodes: set[coord]):
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]

    coord_1_x = a1[0] - dx
    coord_1_y = a1[1] - dy

    coord_2_x = a2[0] + dx
    coord_2_y = a2[1] + dy

    if 0 <= coord_1_x < height and 0 <= coord_1_y < width:
        antinodes.add((coord_1_x, coord_1_y))

    if 0 <= coord_2_x < height and 0 <= coord_2_y < width:
        antinodes.add((coord_2_x, coord_2_y))


if __name__ == '__main__':
    print(day8_solve(calc))
