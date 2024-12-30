import networkx as nx

from utils import get_input_lines


def day23_input() -> nx.Graph:
    graph = nx.Graph()

    for line in get_input_lines(__file__):
        v1, v2 = line.split("-")
        graph.add_edge(v1, v2)

    return graph
