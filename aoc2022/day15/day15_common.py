import re

from utils import get_input_lines


def load_data():
    sensors = []
    beacons = set()

    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue

        m = re.match(r"Sensor at x=(?P<s_x>[-0-9]+), y=(?P<s_y>[-0-9]+): closest beacon is at x=(?P<b_x>[-0-9]+), y=(?P<b_y>[-0-9]+)", line)
        s_x = int(m.group("s_x"))
        s_y = int(m.group("s_y"))
        b_x = int(m.group("b_x"))
        b_y = int(m.group("b_y"))
        sensors.append((s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)))
        beacons.add((b_x, b_y))

    return sensors, beacons
