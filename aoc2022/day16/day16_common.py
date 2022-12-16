from queue import Queue

from utils import get_input_lines


def load_data():
    flows = dict()
    neighbours = dict()

    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue
        parts = line.split(" ")
        valve = parts[1]
        flow = int(parts[4][5:-1])
        next_valves = dict(map(lambda l: (l[:2], 1), parts[9:]))

        flows[valve] = flow
        neighbours[valve] = next_valves

    return flows, neighbours


def reduce(flows):
    return list(map(lambda x: x[0], (filter(lambda x: x[1] > 0 or x[0] == START, flows.items()))))


def bfs(edges, start) -> dict:
    queue = Queue()
    queue.put((start, 0))
    dist = dict()

    while not queue.empty():
        v, d = queue.get()

        if v in dist:
            continue

        if v != start:
            dist[v] = d

        for k_next in edges[v].keys():
            if k_next in dist:
                continue

            queue.put((k_next, d + 1))

    return dist


def distances(valves, neighbours) -> dict:
    dist_matrix = dict()
    for v in valves:
        dist_matrix[v] = bfs(neighbours, v)

    return dist_matrix


START = "AA"
FLOWS, NEIGHBOURS = load_data()
VALVES = reduce(FLOWS)
DISTANCES = distances(VALVES, NEIGHBOURS)
