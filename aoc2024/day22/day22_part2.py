from collections import defaultdict

from aoc2024.day22.day22_common import get_secrets
from utils import get_input_lines


def get_prices(initial: int) -> list[int]:
    prices = [initial % 10]

    for secret in get_secrets(initial):
        prices.append(secret % 10)

    return prices


def get_differences(prices: list[int]) -> list[int]:
    previous = None  # type: int | None
    differences = []  # type: list[int]

    for price in prices:
        if previous is not None:
            differences.append(price - previous)

        previous = price

    return differences


def main():
    sequences = defaultdict(int)

    for line in get_input_lines(__file__):
        seen = set()

        prices = get_prices(int(line))
        diffs = get_differences(prices)

        for idx in range(3, len(diffs)):
            sequence = tuple(diffs[idx - 3:idx + 1])

            # Only look at diff sequence if not previously seen (monkey only sells once)
            if sequence not in seen:
                sequences[sequence] += prices[idx + 1]
                seen.add(sequence)

    print(max(sequences.values()))


if __name__ == '__main__':
    main()
