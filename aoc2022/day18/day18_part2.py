from queue import Queue
from typing import Set

from aoc2022.day18.day18_common import load_data, adjacent, Coord


def area(droplets: Set[Coord], min_coord: Coord, max_coord: Coord) -> int:
    a = 0

    # Shift min/max coords outside droplets
    min_coord = tuple(map(lambda c: c - 1, min_coord))
    max_coord = tuple(map(lambda c: c + 1, max_coord))

    # BFS outside droplets
    visited = set()
    queue = Queue()
    queue.put(min_coord)

    while not queue.empty():
        coord = queue.get()

        if coord in visited:
            continue

        visited.add(coord)

        for adj in adjacent(coord):
            if adj in droplets:
                a += 1
            elif adj not in visited:
                if all(min_coord[axis] <= adj[axis] <= max_coord[axis] for axis in range(3)):
                    queue.put(adj)

    return a


if __name__ == '__main__':
    print(area(*load_data()))
