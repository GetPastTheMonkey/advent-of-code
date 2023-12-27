from z3 import IntVector, Solver

from aoc2023.day24.day24_common import day24_get_hailstones


def main():
    hailstones = day24_get_hailstones()

    my_x, my_y, my_z, my_v_x, my_v_y, my_v_z = IntVector("my", 6)
    times = IntVector("t", len(hailstones))

    s = Solver()

    for (x, y, z, v_x, v_y, v_z), t in zip(hailstones, times):
        s.add(x + t * v_x == my_x + t * my_v_x)
        s.add(y + t * v_y == my_y + t * my_v_y)
        s.add(z + t * v_z == my_z + t * my_v_z)

    s.check()
    result = s.model()

    pos_x = result[my_x].as_long()
    pos_y = result[my_y].as_long()
    pos_z = result[my_z].as_long()

    print(pos_x + pos_y + pos_z)


if __name__ == '__main__':
    main()
