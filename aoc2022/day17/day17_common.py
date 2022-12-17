from typing import Set, Tuple

from utils import get_input_lines

CoordSet = Set[Tuple[int, int]]
HashableCoordSet = frozenset[Tuple[int, int]]


def get_next_rock(t: int, y: int) -> CoordSet:
    if t == 0:
        return {(2, y), (3, y), (4, y), (5, y)}
    elif t == 1:
        return {(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)}
    elif t == 2:
        return {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)}
    elif t == 3:
        return {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)}
    elif t == 4:
        return {(2, y + 1), (2, y), (3, y + 1), (3, y)}
    else:
        raise ValueError(f"Invalid y coordinate: {y}")


def move_sideways(rock: CoordSet, all_rocks: CoordSet, move_left: bool) -> Tuple[bool, CoordSet]:
    """
    Moves a rock sideways. Returns if the move is legal and the new rock coordinates.
    """
    direction = -1 if move_left else 1

    if direction == -1 and any(x == 0 for (x, y) in rock):
        # Want to move left, but can't because rock is touching left wall
        return False, set()
    elif direction == 1 and any(x == 6 for (x, y) in rock):
        # Want to move right, but can't because rock is touching right wall
        return False, set()

    # Simulate move and return if intersection with other rocks is empty or not
    new_rock = set((x + direction, y) for (x, y) in rock)
    return len(new_rock.intersection(all_rocks)) == 0, new_rock


def move_downwards(rock: CoordSet, all_rocks: CoordSet) -> Tuple[bool, CoordSet]:
    """
    Moves a rock downwards. Returns if the move is legal and the new rock coordinates.
    """
    new_rocks = set((x, y - 1) for (x, y) in rock)
    return len(new_rocks.intersection(all_rocks)) == 0, new_rocks


def top_rows(row: CoordSet) -> HashableCoordSet:
    max_y = max(y for (x, y) in row)
    return frozenset((x, max_y - y) for (x, y) in row if max_y - y <= 30)


def day17_solve(max_rock_count: int) -> int:
    moves = next(get_input_lines(__file__))
    next_move = 0

    rock_count = 0
    top_rock = 0
    all_rocks = set((x, 0) for x in range(7))

    cache = dict()
    added = 0

    while rock_count < max_rock_count:
        rock = get_next_rock(rock_count % 5, top_rock + 4)

        while True:
            # PHASE 1: Move sideways (if able)
            next_move = (next_move + 1) % len(moves)
            move_legal, new_rock = move_sideways(rock, all_rocks, moves[next_move] == "<")

            if move_legal:
                rock = new_rock

            # PHASE 2: Move downwards (or continue with next rock)
            move_legal, new_rock = move_downwards(rock, all_rocks)

            if move_legal:
                rock = new_rock
            else:
                all_rocks = all_rocks.union(rock)
                top_rock = max((y for (x, y) in all_rocks))

                # PHASE 3: Cycle detection
                cache_key = (next_move, rock_count % 5, top_rows(all_rocks))

                if cache_key in cache:
                    (old_rock_count, old_top_rock) = cache[cache_key]
                    diff_top_rock = top_rock - old_top_rock
                    diff_rock_count = rock_count - old_rock_count
                    cycles = (max_rock_count - rock_count) // diff_rock_count
                    added += cycles * diff_top_rock
                    rock_count += cycles * diff_rock_count
                    assert rock_count <= max_rock_count
                else:
                    cache[cache_key] = (rock_count, top_rock)

                break

        rock_count += 1

    return top_rock + added
