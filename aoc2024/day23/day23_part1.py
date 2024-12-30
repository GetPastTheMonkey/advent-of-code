import networkx as nx

from aoc2024.day23.day23_common import day23_input


def main():
    s = 0
    graph = day23_input()

    triad_cliques = (c for c in nx.enumerate_all_cliques(graph) if len(c) == 3)

    for clique in triad_cliques:
        if any(v.startswith("t") for v in clique):
            s += 1

    print(s)


if __name__ == '__main__':
    main()
