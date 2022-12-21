from typing import Tuple, Dict, Callable

from utils import get_input_lines

Complex2to1 = Callable[[complex, complex], complex]


def load_monkeys() -> Tuple[Dict[str, complex], Dict[str, Tuple[str, str, Complex2to1]]]:
    values = dict()  # type: Dict[str, complex]
    requirements = dict()  # type: Dict[str, Tuple[str, str, Complex2to1]]

    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue

        monkey, value = line.split(": ")

        if value.isnumeric():
            values[monkey] = complex(value)
        else:
            left, op, right = value.split(" ")

            if op == "+":
                operator = lambda x, y: x + y
            elif op == "-":
                operator = lambda x, y: x - y
            elif op == "*":
                operator = lambda x, y: x * y
            elif op == "/":
                operator = lambda x, y: x / y
            else:
                raise ValueError(f"Invalid operator for monkey {monkey}: {op}")

            requirements[monkey] = left, right, operator

    return values, requirements


def day21_solve(part_1: bool) -> int:
    values, requirements = load_monkeys()

    def solve_monkey(monkey: str) -> complex:
        if monkey in values:
            return values[monkey]
        elif monkey in requirements:
            left, right, operator = requirements[monkey]
            return operator(solve_monkey(left), solve_monkey(right))
        else:
            ValueError(f"Monkey {monkey} neither in values not in requirements")

    if part_1:
        val = int(solve_monkey("root").real)
    else:
        # Use the imaginary number as a "variable"
        values["humn"] = 1j

        # Solve left and right monkey of root
        root_left, root_right, _ = requirements["root"]
        val_left = solve_monkey(root_left)
        val_right = solve_monkey(root_right)

        # Ensure that the left value holds the imaginary part
        if val_right.imag > 0:
            val_left, val_right = val_right, val_left

        # Solve for the imaginary part and recover the variable
        val = int(round((val_right.real - val_left.real) / val_left.imag))

    return val
