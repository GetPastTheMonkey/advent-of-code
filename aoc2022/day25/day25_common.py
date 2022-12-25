from utils import get_input_lines


def snafu_to_decimal(snafu: str) -> int:
    result = 0

    lookup = {
        "=": -2,
        "-": -1,
        "0": 0,
        "1": 1,
        "2": 2,
    }

    for digit in snafu:
        result *= 5
        result += lookup[digit]

    return result


def decimal_to_snafu(decimal: int) -> str:
    result = ""

    while decimal > 0:
        remainder = decimal % 5

        if remainder == 3:
            # Case 3: Prepend "minus 2" and add 5 (3 = 5 - 2)
            result = "=" + result
            decimal += 5
        elif remainder == 4:
            # Case 4: Prepend "minus 1" and add 5 (4 = 5 - 1)
            result = "-" + result
            decimal += 5
        else:
            # Case 0, 1, 2 -> Just prepend the remainder
            result = f"{remainder}" + result

        decimal //= 5

    return result


def day25_solve(part_1: bool) -> str:
    if part_1:
        accumulator = sum(map(snafu_to_decimal, get_input_lines(__file__)))
        return decimal_to_snafu(accumulator)
    else:
        return "Merry christmas :)"
