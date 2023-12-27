from utils import get_input_lines

Vector = tuple[int, int, int]


def get_initial_bricks() -> list[set[Vector]]:
    bricks = []  # type: list[set[Vector]]

    for line in get_input_lines(__file__):
        start, end = line.split("~")
        x_s, y_s, z_s = [int(s) for s in start.split(",")]
        x_e, y_e, z_e = [int(e) for e in end.split(",")]

        blocks = set()  # type: set[Vector]

        for x in range(x_s, x_e + 1):
            for y in range(y_s, y_e + 1):
                for z in range(z_s, z_e + 1):
                    blocks.add((x, y, z))

        bricks.append(blocks)

    return bricks


def union(sets: list[set[Vector]]) -> set[Vector]:
    u = set()  # type: set[Vector]

    for s in sets:
        u |= s

    return u


def get_fallen_bricks() -> list[set[Vector]]:
    bricks = get_initial_bricks()
    all_bricks = union(bricks)
    has_moved = True

    while has_moved:
        has_moved = False

        for i in range(len(bricks)):
            brick = bricks[i]

            if any(z <= 1 for _, _, z in brick):
                # This brick is already on the floor!
                continue

            blocked_coords = all_bricks - brick
            new_brick = {(x, y, z - 1) for x, y, z in brick}

            if len(blocked_coords & new_brick) > 0:
                # This brick is blocked by another brick!
                continue

            # Brick is not at the bottom and brick is not blocked by another brick --> Move it!
            bricks[i] = new_brick
            has_moved = True
            all_bricks = blocked_coords | new_brick

    return bricks


def get_dependencies() -> list[set[int]]:
    bricks = get_fallen_bricks()
    dependencies = []  # type: list[set[int]]

    for i in range(len(bricks)):
        brick_i = bricks[i]
        deps = set()  # type: set[int]

        for j in range(len(bricks)):
            if i == j:
                continue

            brick_j = bricks[j]

            if any((x, y, z - 1) in brick_j for (x, y, z) in brick_i):
                deps.add(j)

        dependencies.append(deps)

    return dependencies
