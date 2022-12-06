import re

from utils import get_input_lines


class TinyScreen:
    WIDTH = 50
    HEIGHT = 6

    def __init__(self):
        self._grid = [[False] * self.WIDTH for _ in range(self.HEIGHT)]

    def __repr__(self):
        ret = ""
        for line in self._grid:
            ret += "".join("█" if x else " " for x in line) + "\n"
        return ret

    @property
    def count(self):
        return sum(sum(1 if x else 0 for x in row) for row in self._grid)

    def rect(self, cols: int, rows: int):
        for i in range(rows):
            for j in range(cols):
                self._grid[i][j] = True

    def rotate_row(self, idx: int, n: int):
        shift = self.WIDTH - n
        row = self._grid[idx]
        row = row[shift:] + row[:shift]
        self._grid[idx] = row

    def rotate_column(self, idx: int, n: int):
        shift = self.HEIGHT - n
        col = [row[idx] for row in self._grid]
        col = col[shift:] + col[:shift]

        for i in range(self.HEIGHT):
            self._grid[i][idx] = col[i]


def day8_solve(print_count):
    screen = TinyScreen()

    for line in get_input_lines(__file__):
        if m := re.match(r"rect (?P<cols>[0-9]+)x(?P<rows>[0-9]+)", line):
            cols = int(m.group("cols"))
            rows = int(m.group("rows"))
            screen.rect(cols, rows)
        elif m := re.match(r"rotate row y=(?P<idx>[0-9]+) by (?P<n>[0-9]+)", line):
            idx = int(m.group("idx"))
            n = int(m.group("n"))
            screen.rotate_row(idx, n)
        elif m := re.match(r"rotate column x=(?P<idx>[0-9]+) by (?P<n>[0-9]+)", line):
            idx = int(m.group("idx"))
            n = int(m.group("n"))
            screen.rotate_column(idx, n)

    if print_count:
        print(screen.count)
    else:
        print(screen)
