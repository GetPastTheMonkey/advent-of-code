import re
from typing import Dict, Tuple

from utils import get_input_lines


class Robot:
    def __init__(self):
        self._value_1 = None
        self._value_2 = None
        self._low_to_output = None
        self._low_to_number = None
        self._high_to_output = None
        self._high_to_number = None
        self._finished = False

    def can_proceed(self) -> bool:
        return self._value_1 is not None and self._value_2 is not None and not self._finished

    def set_value(self, val: int) -> None:
        if self._value_1 is None:
            self._value_1 = val
        elif self._value_2 is None:
            self._value_2 = val
        else:
            raise ValueError("I am already full!")

    def get_values(self) -> Tuple[int, int]:
        return self._value_1, self._value_2

    def configure(self, low_to_output, low_to_number, high_to_output, high_to_number) -> None:
        if not all(x is None for x in [self._low_to_output, self._low_to_number, self._high_to_output,
                                       self._high_to_number]):
            raise ValueError("I am already configure")

        self._low_to_output = low_to_output
        self._low_to_number = low_to_number
        self._high_to_output = high_to_output
        self._high_to_number = high_to_number

    def proceed(self) -> Tuple[Dict[int, int], Dict[int, int]]:
        if not self.can_proceed():
            raise ValueError("I am not ready!")

        values = [self._value_1, self._value_2]
        values.sort()

        to_output = dict()
        to_robots = dict()

        if self._low_to_output:
            to_output[self._low_to_number] = values[0]
        else:
            to_robots[self._low_to_number] = values[0]

        if self._high_to_output:
            to_output[self._high_to_number] = values[1]
        else:
            to_robots[self._high_to_number] = values[1]

        self._finished = True

        return to_output, to_robots


def setup_network() -> Dict[int, Robot]:
    robots = dict()

    for line in get_input_lines(__file__):
        if m := re.match(r"value (?P<value>[0-9]+) goes to bot (?P<bot>[0-9]+)", line):
            value = int(m.group("value"))
            bot = int(m.group("bot"))

            if bot not in robots:
                robots[bot] = Robot()

            robots[bot].set_value(value)
        elif m := re.match(
                r"bot (?P<bot>[0-9]+) gives low to (?P<low_target>bot|output) (?P<low_nr>[0-9]+) and high to "
                r"(?P<high_target>bot|output) (?P<high_nr>[0-9]+)", line):
            bot = int(m.group("bot"))
            low_output = m.group("low_target") == "output"
            low_nr = int(m.group("low_nr"))
            high_output = m.group("high_target") == "output"
            high_nr = int(m.group("high_nr"))

            if bot not in robots:
                robots[bot] = Robot()

            robots[bot].configure(low_output, low_nr, high_output, high_nr)
        else:
            raise ValueError(f"Could not match line to any pattern: {line}")

    return robots


def run_network():
    outputs = dict()
    robots = setup_network()

    while True:
        can_proceed = [bot for bot in robots.values() if bot.can_proceed()]

        if len(can_proceed) == 0:
            break

        for bot in can_proceed:
            to_output, to_robots = bot.proceed()

            # Update output
            for k, v in to_output.items():
                outputs[k] = v

            # Output robots
            for k, v in to_robots.items():
                robots[k].set_value(v)

    return outputs, robots
