from utils import get_input_lines


def day6_solve(reverse: bool):
    counters = []

    for line in get_input_lines(__file__):
        for idx, c in enumerate(line):
            if idx >= len(counters):
                counter = dict()
                for i in range(ord("a"), ord("z") + 1):
                    counter[chr(i)] = 0

                counters.append(counter)

            counters[idx][c] += 1

    msg = map(lambda x: sorted(x.items(), key=lambda y: y[1], reverse=reverse)[0][0], counters)
    return "".join(msg)