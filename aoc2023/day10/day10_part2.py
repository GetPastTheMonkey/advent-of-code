from aoc2023.day10.day10_common import day10_loop_coords


def get_polygon_area(coords: list[tuple[int, int]]) -> int:
    """
    Calculate the area of a polygon using the shoelace formula
    https://en.wikipedia.org/wiki/Shoelace_formula

    :param coords: list of polygon coordinates (vertices)
    :return: the area of the polygon
    """
    area = 0

    for idx in range(len(coords)):
        next_idx = (idx + 1) % len(coords)
        x_i, y_i = coords[idx]
        x_i_next, y_i_next = coords[next_idx]
        area += (y_i + y_i_next) * (x_i - x_i_next)

    return abs(area) // 2


def picks_theorem() -> int:
    """
    Solved using Pick's theorem
    https://en.wikipedia.org/wiki/Pick%27s_theorem

    :return: the number of points with integer coordinates inside the polygon
    """
    loop_coords = day10_loop_coords()
    area = get_polygon_area(loop_coords)
    return area - (len(loop_coords) // 2) + 1


if __name__ == '__main__':
    print(picks_theorem())
