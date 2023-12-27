import networkx as nx
from networkx import path_weight

from aoc2023.day23.day23_common import day23_parse_grid, Vector

DIST_KEY = "dist"


def create_graph() -> tuple[nx.Graph, Vector, Vector]:
    grid = day23_parse_grid()

    height = len(grid)
    width = len(grid[0])
    graph = nx.grid_2d_graph(height, width)  # type: nx.Graph

    for i in range(height):
        for j in range(width):
            if grid[i][j] == "#":
                graph.remove_node((i, j))

    start = (0, 1)
    end = (height - 1, width - 2)

    return graph, start, end


def reduce_graph(graph: nx.Graph):
    # Combine all nodes that have only two neighbours
    removable = [node for node in graph.nodes if len(graph.edges(node)) == 2]

    for node in removable:
        n1, n2 = graph.neighbors(node)
        w1 = graph.edges[node, n1].get(DIST_KEY, 1)
        w2 = graph.edges[node, n2].get(DIST_KEY, 1)
        graph.add_edge(n1, n2, dist=w1 + w2)
        graph.remove_node(node)


def main():
    graph, start, end = create_graph()
    print(f"Initial {graph}")

    reduce_graph(graph)
    print(f"Reduced {graph}")

    max_path = max(path_weight(graph, path, DIST_KEY) for path in nx.all_simple_paths(graph, start, end))
    print(max_path)


if __name__ == '__main__':
    main()
