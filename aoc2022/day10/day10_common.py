from utils import get_input_lines


class Crt:
    SIGNALS = {20, 60, 100, 140, 180, 220}
    WIDTH = 40

    def __init__(self):
        self._cycle = 0
        self._register = 1
        self._strength = 0
        self._display = ""

    def _advance(self, n: int):
        for _ in range(n):
            # For part 2: Add character of this cycle to the display
            pixel = self._cycle % self.WIDTH
            self._display += "█" if abs(pixel - self._register) <= 1 else " "

            # Check if end of line is reached and add newline if needed
            if pixel == self.WIDTH - 1:
                self._display += "\n"

            # Increment cycle counter
            self._cycle += 1

            # For part 1: Cycle is 0-indexed (while description is 1-indexed),
            #             so must check after incrementing
            if self._cycle in self.SIGNALS:
                self._strength += self._cycle * self._register

    def noop(self):
        self._advance(1)

    def add(self, x: int):
        self._advance(2)
        self._register += x

    @property
    def strength(self):
        return self._strength

    @property
    def display(self):
        return self._display


def load_crt() -> Crt:
    crt = Crt()

    for line in get_input_lines(__file__):
        if line.startswith("addx"):
            crt.add(int(line.split(" ")[1]))
        elif line.startswith("noop"):
            crt.noop()

    return crt
