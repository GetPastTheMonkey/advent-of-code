from os.path import join, dirname, realpath

DIRECTIONS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def tuple_add(t1, t2):
    res = (t1[0] + t2[0], t1[1] + t2[1])
    return res


def manhattan_distance(t1):
    return abs(t1[0]) + abs(t1[1])


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    visited_by_line_0 = dict()
    candidates = dict()
    line_nr = 0

    for line in f:
        current_point = (0, 0)
        length = 0
        for instruction in line.split(","):
            direction = DIRECTIONS[instruction[0]]
            moves = int(instruction[1:])

            while moves > 0:
                length += 1
                current_point = tuple_add(current_point, direction)
                if line_nr == 0 and current_point not in visited_by_line_0:
                    # Currently tracing first line, not visited this position
                    visited_by_line_0[current_point] = length
                elif current_point in visited_by_line_0 and current_point not in candidates:
                    candidates[current_point] = length
                moves -= 1
        line_nr += 1

    minimum_length = 1e10
    for pt, dist in candidates.items():
        l = dist + visited_by_line_0[pt]
        if l < minimum_length:
            minimum_length = l
    print("Minimum length: {}".format(minimum_length))
