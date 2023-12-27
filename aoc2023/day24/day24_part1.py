from aoc2023.day24.day24_common import day24_get_hailstones


def curve_to_function(x: float, y: float, v_x: float, v_y: float) -> tuple[float, float]:
    """
    Transform a line curve ``c(t) = (x, y) + t * (v_x, v_y)`` into a line function ``y = m * x + q``.

    :param x: x-coordinate of the starting point of the line curve.
    :param y: y-coordinate of the starting point of the line curve.
    :param v_x: Velocity in the direction of the x-axis of the curve.
    :param v_y: Velocity in the direction of the y-axis of the curve.
    :return: The function parameters ``(m, q)`` which describe the curve according to ``y = m * x + q``.
    :raises ValueError: If ``v_x`` is zero, no function exists.
    """
    if v_x == 0:
        raise ValueError("Horizontal curve velocity must be different from zero")

    m = v_y / v_x
    q = y - m * x
    return m, q


def line_intersection(m1: float, q1: float, m2: float, q2: float) -> tuple[float, float]:
    """
    Find the intersection point of two linear functions of the form ``m * x + q``.

    :param m1: The slope of the first linear function.
    :param q1: The y-intercept of the first linear function.
    :param m2: The slope of the second linear function.
    :param q2: The y-intercept of the second linear function.
    :return: The ``(x, y)``-coordinates of the intersection point of the two linear functions.
    :raises ValueError: If the slopes are equal, no intersection point exists.
    """
    if m1 == m2:
        raise ValueError("The functions have the same slope: No intersection point exists.")

    x = (q2 - q1) / (m1 - m2)
    y = m1 * x + q1
    return x, y


def main():
    min_val = 200000000000000
    max_val = 400000000000000
    counter = 0

    hailstone_curves = day24_get_hailstones()
    hailstone_funcs = [curve_to_function(x, y, v_x, v_y) for x, y, _, v_x, v_y, _ in hailstone_curves]

    for idx1 in range(len(hailstone_curves)):
        pos_x_1, _, _, vel_x_1, _, _ = hailstone_curves[idx1]
        m1, q1 = hailstone_funcs[idx1]

        for idx2 in range(idx1 + 1, len(hailstone_curves)):
            pos_x_2, _, _, vel_x_2, _, _ = hailstone_curves[idx2]
            m2, q2 = hailstone_funcs[idx2]

            try:
                x, y = line_intersection(m1, q1, m2, q2)
            except ValueError:
                # The hailstones do not collide at all
                continue

            if not (min_val <= x <= max_val and min_val <= y <= max_val):
                # The hailstones collide outside the testing area
                continue

            if (x - pos_x_1) / vel_x_1 < 0 or (x - pos_x_2) / vel_x_2 < 0:
                # The hailstones collide in the past
                continue

            # The hailstones collide inside the testing area and in the future --> Count it!
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
