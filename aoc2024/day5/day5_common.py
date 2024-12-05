from utils import get_input_lines


def day5_input() -> tuple[dict[int, set[int]], list[list[int]]]:
    preconditions = dict()
    prints = []
    first_section = True

    for line in get_input_lines(__file__):
        if len(line) == 0:
            first_section = False
            continue

        if first_section:
            x, y = map(int, line.split("|"))

            if y not in preconditions:
                preconditions[y] = set()

            preconditions[y].add(x)
        else:
            nums = list(map(int, line.split(",")))
            prints.append(nums)

    return preconditions, prints


def is_printable(preconditions: dict[int, set[int]], nums: list[int]) -> bool:
    printed = set()

    for num in nums:
        if num in preconditions:
            precon = preconditions[num] & set(nums)

            if len(precon - printed) > 0:
                return False

        printed.add(num)

    return True
