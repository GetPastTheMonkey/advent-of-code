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
    visited_by_line_0 = set()
    candidates = set()
    line_nr = 0

    for line in f:
        current_point = (0, 0)
        for instruction in line.split(","):
            direction = DIRECTIONS[instruction[0]]
            moves = int(instruction[1:])

            while moves > 0:
                current_point = tuple_add(current_point, direction)
                if line_nr == 0:
                    # Currently tracing first line
                    visited_by_line_0.add(current_point)
                elif current_point in visited_by_line_0:
                    # Currently tracing second line, collision detected, adding candidate
                    candidates.add(current_point)
                moves -= 1
        line_nr += 1

    print("Minimum distance: {}".format(min(map(manhattan_distance, candidates))))
