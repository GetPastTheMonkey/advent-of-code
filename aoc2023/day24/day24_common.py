from utils import get_input_lines


def day24_get_hailstones() -> list[tuple[int, int, int, int, int, int]]:
    hailstones = []

    for line in get_input_lines(__file__):
        position, velocity = line.split(" @ ")
        px, py, pz = [int(p) for p in position.split(", ")]
        vx, vy, vz = [int(v) for v in velocity.split(", ")]
        hailstones.append((px, py, pz, vx, vy, vz))

    return hailstones
