from typing import List, Tuple, Set

from utils import get_input_lines

Coord = Tuple[int, int, int]


def load_data() -> Tuple[Set[Coord], Coord, Coord]:
    droplets = set()
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    min_z = None
    max_z = None

    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue

        x, y, z = map(int, line.split(","))
        droplets.add((x, y, z))

        min_x = x if min_x is None else min(min_x, x)
        max_x = x if max_x is None else max(max_x, x)
        min_y = y if min_y is None else min(min_y, y)
        max_y = y if max_y is None else max(max_y, y)
        min_z = z if min_z is None else min(min_z, z)
        max_z = z if max_z is None else max(max_z, z)

    return droplets, (min_x, min_y, min_z), (max_x, max_y, max_z)


def adjacent(coord: Coord) -> List[Coord]:
    x, y, z = coord
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]
