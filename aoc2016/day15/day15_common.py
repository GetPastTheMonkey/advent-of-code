from utils import get_input_lines, chinese_remainder


def day15_solve(part_2: bool) -> int:
    m = []
    a = []

    for line in get_input_lines(__file__):
        words = line.split(" ")
        disc = int(words[1][1:])
        positions = int(words[3])
        initial = int(words[-1][:-1])

        m.append(positions)
        a.append((0 - initial - disc) % positions)

    if part_2:
        disc = len(a) + 1
        positions = 11
        initial = 0

        m.append(positions)
        a.append((0 - initial - disc) % positions)

    return chinese_remainder(m, a)
