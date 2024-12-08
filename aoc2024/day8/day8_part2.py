from aoc2024.day8.day8_common import day8_solve, coord


def calc(a1: coord, a2: coord, height: int, width: int, antinodes: set[coord]):
    # Each antenna has an antinode
    antinodes.add(a1)
    antinodes.add(a2)

    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]

    # Walk backwards from first tower until border
    current_coord_x = a1[0]
    current_coord_y = a1[1]

    while True:
        current_coord_x -= dx
        current_coord_y -= dy

        if 0 <= current_coord_x < height and 0 <= current_coord_y < width:
            antinodes.add((current_coord_x, current_coord_y))
        else:
            break

    # Walk forward from second tower until border
    current_coord_x = a2[0]
    current_coord_y = a2[1]

    while True:
        current_coord_x += dx
        current_coord_y += dy

        if 0 <= current_coord_x < height and 0 <= current_coord_y < width:
            antinodes.add((current_coord_x, current_coord_y))
        else:
            break


if __name__ == '__main__':
    print(day8_solve(calc))
