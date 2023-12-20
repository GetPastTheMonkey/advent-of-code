from queue import Queue

from utils import get_input_lines

Range = tuple[int, int]
XmasRange = tuple[Range, Range, Range, Range]


def parse_rules():
    rules = dict()  # type: dict[str, list[tuple[str, ...]]]

    for line in get_input_lines(__file__):
        if len(line) == 0:
            break
        else:
            name, rule_list = line.split("{")
            rule_list = [r.split(":") for r in rule_list[:-1].split(",")]
            rules[name] = rule_list

    return rules


def main():
    rules = parse_rules()
    minimum = 1
    maximum = 4000

    initial_range = (
        (minimum, maximum),  # Initial range for x
        (minimum, maximum),  # Initial range for m
        (minimum, maximum),  # Initial range for a
        (minimum, maximum),  # Initial range for s
    )

    queue = Queue()  # type: Queue[tuple[str, XmasRange]]
    queue.put(("in", initial_range))

    results = []  # type: list[XmasRange]

    while not queue.empty():
        state, (rx, rm, ra, rs) = queue.get()

        if state == "R":
            # Range rejected, ignore it
            continue
        elif state == "A":
            # Range accepted, save it in results
            results.append((rx, rm, ra, rs))
            continue

        for rule in rules[state]:
            if len(rule) == 1:
                # Put remaining range in queue
                queue.put((rule[0], (rx, rm, ra, rs)))
            elif len(rule) == 2:
                condition, next_rule = rule

                part = condition[0]
                op = condition[1]
                value = int(condition[2:])

                idx_lut = {"x": 0, "m": 1, "a": 2, "s": 3}
                new_ranges = [rx, rm, ra, rs]
                affected_range = new_ranges[idx_lut[part]]

                if op == "<" and affected_range[0] < value:
                    new_range = (affected_range[0], value - 1)

                    copied_range = [rx, rm, ra, rs]
                    copied_range[idx_lut[part]] = new_range
                    queue.put((next_rule, tuple(copied_range)))

                    remaining_range = (value, affected_range[1])

                    if remaining_range[0] > remaining_range[1]:
                        # No remaining range!
                        continue

                    new_ranges[idx_lut[part]] = remaining_range
                    rx, rm, ra, rs = new_ranges
                elif op == ">" and affected_range[1] > value:
                    new_range = (value + 1, affected_range[1])

                    copied_range = [rx, rm, ra, rs]
                    copied_range[idx_lut[part]] = new_range
                    queue.put((next_rule, tuple(copied_range)))

                    remaining_range = (affected_range[0], value)

                    if remaining_range[0] > remaining_range[1]:
                        continue

                    new_ranges[idx_lut[part]] = remaining_range
                    rx, rm, ra, rs = new_ranges
            else:
                raise ValueError("Invalid rule, u wot? 0.o")

    s = 0

    for result in results:
        rx, rm, ra, rs = result
        s += (rx[1] - rx[0] + 1) * (rm[1] - rm[0] + 1) * (ra[1] - ra[0] + 1) * (rs[1] - rs[0] + 1)

    print(s)


if __name__ == '__main__':
    main()
