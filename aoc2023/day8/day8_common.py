import math

from utils import get_input_lines


def day8_parse() -> tuple[list[int], dict[str, tuple[str, str]]]:
    path = []
    graph = dict()

    for line in get_input_lines(__file__):
        if len(path) == 0:
            path = [0 if c == "L" else 1 for c in line]
        elif len(line) > 0:
            node, left_right = line.split(" = ")
            left, right = left_right[1:-1].split(", ")
            graph[node] = (left, right)

    return path, graph


def day8_walk_until(start_cond, stop_cond) -> int:
    path, graph = day8_parse()
    starts = (p for p in graph.keys() if start_cond(p))
    lcm = 1

    for start in starts:
        curr_pos = start
        idx = 0

        while not stop_cond(curr_pos):
            direction = path[idx % len(path)]
            curr_pos = graph[curr_pos][direction]
            idx += 1

        lcm = math.lcm(lcm, idx)

    return lcm
