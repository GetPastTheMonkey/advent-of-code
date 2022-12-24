from typing import Tuple, Set

from utils import get_input_lines

Elf = Tuple[int, int]


def next_elf_position(elves: Set[Elf], elf: Elf, directions: str) -> Tuple[Elf, bool]:
    assert len(directions) == 4 and set(directions) == {"N", "S", "W", "E"}

    elf_x, elf_y = elf
    elf_nw = elf_x - 1, elf_y - 1
    elf_n = elf_x - 1, elf_y
    elf_ne = elf_x - 1, elf_y + 1
    elf_w = elf_x, elf_y - 1
    elf_e = elf_x, elf_y + 1
    elf_sw = elf_x + 1, elf_y - 1
    elf_s = elf_x + 1, elf_y
    elf_se = elf_x + 1, elf_y + 1

    if not any(x in elves for x in [elf_nw, elf_n, elf_ne, elf_w, elf_e, elf_sw, elf_s, elf_se]):
        # No other elf around, return same position
        return elf, False

    for char in directions:
        if char == "N" and not any(x in elves for x in [elf_nw, elf_n, elf_ne]):
            return elf_n, True
        elif char == "S" and not any(x in elves for x in [elf_sw, elf_s, elf_se]):
            return elf_s, True
        elif char == "W" and not any(x in elves for x in [elf_nw, elf_w, elf_sw]):
            return elf_w, True
        elif char == "E" and not any(x in elves for x in [elf_ne, elf_e, elf_se]):
            return elf_e, True

    # Cannot move in any direction, return same position
    return elf, False


def load_elves() -> Set[Elf]:
    elves = set()

    for line_idx, line in enumerate(get_input_lines(__file__)):
        for char_idx, char in enumerate(line):
            if char == "#":
                elves.add((line_idx, char_idx))

    return elves


def day23_solve(part_1: bool) -> int:
    elves = load_elves()
    directions = "NSWE"
    round_count = 0

    while True:
        if part_1 and round_count == 10:
            height = max(map(lambda x: x[0], elves)) - min(map(lambda x: x[0], elves)) + 1
            width = max(map(lambda x: x[1], elves)) - min(map(lambda x: x[1], elves)) + 1
            return (height * width) - len(elves)

        round_count += 1

        # Calculate new positions and save list of elves that want to move there
        new_positions = dict()
        any_moved = False

        for elf in elves:
            new_elf, moved = next_elf_position(elves, elf, directions)
            any_moved = any_moved or moved

            if new_elf in new_positions:
                new_positions[new_elf].append(elf)
            else:
                new_positions[new_elf] = [elf]

        if not part_1 and not any_moved:
            return round_count

        # Iterate through new positions and move if only single elf wants to move there
        new_elves = set()
        for new_elf, elf_list in new_positions.items():
            if len(elf_list) == 1:
                new_elves.add(new_elf)
            else:
                for old_elf in elf_list:
                    new_elves.add(old_elf)

        assert len(new_elves) == len(elves)

        elves = new_elves
        directions = directions[1:] + directions[0]
