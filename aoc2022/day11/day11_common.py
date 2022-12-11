from typing import List, Callable, Tuple, Dict

from utils import get_input_lines


class Monkey:
    def __init__(self, items: List[int], operator: Callable[[int], int], test: int, monkey_true: int, monkey_false: int,
                 div_by_3: bool):
        self._items = items
        self._op = operator
        self._test = test
        self._monkey_true = monkey_true
        self._monkey_false = monkey_false
        self._counter = 0
        self._div_by_3 = div_by_3
        self._mod = None

    def iterate(self) -> Tuple[int, int]:
        if self._mod is None:
            raise ValueError("Need to set modulo before iterating")

        if len(self._items) == 0:
            return -1, -1

        self._counter += 1
        item = self._items.pop(0)
        item = self._op(item)

        if self._div_by_3:
            item = item // 3

        item = item % self._mod

        if item % self._test == 0:
            return self._monkey_true, item
        else:
            return self._monkey_false, item

    def add_item(self, item: int):
        self._items.append(item)

    def set_mod(self, mod: int):
        self._mod = mod

    @property
    def counter(self) -> int:
        return self._counter


def load_monkeys(div_by_3) -> Dict[int, Monkey]:
    curr_monkey = None
    items = None
    operation = None
    test = None
    monkey_true = None
    monkey_false = None
    monkeys = dict()
    mod = 1

    def op(o: str, i: str) -> Callable[[int], int]:
        if o == "+":
            return lambda x: x + int(i)
        elif i.isnumeric():
            return lambda x: x * int(i)
        return lambda x: x * x

    for line in get_input_lines(__file__):
        if line.startswith("Monkey"):
            curr_monkey = int(line[:-1].split(" ")[1])
        elif line.startswith("Starting"):
            items = list(map(int, line.split(": ")[1].split(", ")))
        elif line.startswith("Operation"):
            operation = op(*line.split(" ")[-2:])
        elif line.startswith("Test"):
            test = int(line.split(" ")[-1])
            mod *= test
        elif line.startswith("If true"):
            monkey_true = int(line.split(" ")[-1])
        elif line.startswith("If false"):
            monkey_false = int(line.split(" ")[-1])
        elif curr_monkey is not None:
            monkeys[curr_monkey] = Monkey(items, operation, test, monkey_true, monkey_false, div_by_3)
            curr_monkey = None

    for m in monkeys.values():
        m.set_mod(mod)

    return monkeys


def day11_solve(part_1: bool) -> int:
    monkeys = load_monkeys(div_by_3=part_1)

    for _ in range(20 if part_1 else 10000):
        for monkey in monkeys.values():
            while True:
                next_monkey, next_item = monkey.iterate()

                if next_monkey not in monkeys:
                    break

                monkeys[next_monkey].add_item(next_item)

    counters = list(map(lambda m: m.counter, monkeys.values()))
    counters.sort()
    return counters[-1] * counters[-2]
