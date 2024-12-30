from utils import get_input_lines

coord = tuple[int, int]


def day20_input() -> tuple[set[coord], coord, coord]:
    walkable = set()  # set[coord]
    start = (-1, -1)
    end = (-1, -1)

    for x, line in enumerate(get_input_lines(__file__)):
        for y, c in enumerate(line):
            if c == "#":
                continue

            # Tiles of type "S", "E", and "." reach this point

            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)

            walkable.add((x, y))

    return walkable, start, end


def calc_distances() -> dict[coord, int]:
    walkable, start, end = day20_input()
    current = end
    distances = {end: 0}

    while current != start:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            candidate = current[0] + dx, current[1] + dy

            if candidate not in walkable:
                # Would walk into wall
                continue

            if candidate in distances:
                # Would walk backwards
                continue

            distances[candidate] = distances[current] + 1
            current = candidate
            break

    return distances


def day20_solve(*, part_1: bool) -> int:
    cheat = 2 if part_1 else 20
    distances = calc_distances()
    count = 0

    for curr_x, curr_y in distances.keys():
        for cheat_x in range(-cheat, cheat + 1):
            remaining = cheat - abs(cheat_x)

            for cheat_y in range(-remaining, remaining + 1):
                candidate_x = curr_x + cheat_x
                candidate_y = curr_y + cheat_y

                if (candidate_x, candidate_y) not in distances:
                    continue

                new_distance = distances[(candidate_x, candidate_y)] + abs(cheat_x) + abs(cheat_y)
                saved = distances[(curr_x, curr_y)] - new_distance

                if saved >= 100:
                    count += 1

    return count
