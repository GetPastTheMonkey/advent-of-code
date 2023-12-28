import networkx as nx

from utils import get_input_lines


def load_graph() -> nx.Graph:
    graph = nx.Graph()

    for line in get_input_lines(__file__):
        node, others = line.split(": ")

        for other in others.split(" "):
            graph.add_edge(node, other)

    return graph


def day25_solve(*, part_1: bool) -> str:
    if part_1:
        graph = load_graph()

        for edge in nx.minimum_edge_cut(graph):
            graph.remove_edge(*edge)

        prod = 1

        for subgraph in nx.connected_components(graph):
            prod *= len(subgraph)

        return f"{prod}"
    else:
        return "Merry christmas :)"
