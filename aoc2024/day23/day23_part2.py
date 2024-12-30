import networkx as nx

from aoc2024.day23.day23_common import day23_input


def main():
    graph = day23_input()
    max_clique = max(nx.find_cliques(graph), key=len)
    print(",".join(sorted(max_clique)))


if __name__ == '__main__':
    main()
