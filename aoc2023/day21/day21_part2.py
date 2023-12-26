import numpy as np

from aoc2023.day21.day21_common import day21_parse_input, day21_reachable

"""
NOTES FOR PART 2

Plotting the number of reachable tiles revealed that it is scaling quadratically to the distance. Thus, the actual goal
is to find a suitable quadratic function and then evaluate it at the final distance. Additionally, it was observed that
there are different quadratic functions depending on the distance modulo size. Thus, only the distances with the same
modulo as the final distance should be considered.

We use numpy for fitting and evaluating the polynomials. The fitting gets more precise with more iterations. To halt the
iterating, three predictions must be the same value. It is possible that this might be off by a little bit, thus the
other predictors are also printed. If the final predictor is wrong, observe the other predictors for other suggestions.

Thanks to the Reddit community of r/adventofcode for the help with this exercise.
"""


def main():
    size, unwalkable, start = day21_parse_input()

    data = []  # type: list[tuple[int, int]]
    predictions = []  # type: list[int]

    final_distance = 26501365
    final_distance_mod = final_distance % size

    for dist, num_reachable in day21_reachable(size, unwalkable, start):
        if dist % size != final_distance_mod:
            # Wrong modulo value --> Wrong quadratic function!
            continue

        data.append((dist, num_reachable))

        if len(data) < 3:
            # Need at least 3 data points to fit a quadratic function!
            continue

        coefficients = np.polyfit(*zip(*data), deg=2)
        func = np.poly1d(coefficients)
        prediction = round(func(final_distance))
        predictions.append(prediction)
        print(f"{prediction = } | {dist = }")

        if len(predictions) >= 3 and len(set(predictions[-3:])) == 1:
            # Predictor seems stable --> stop iterating!
            print(predictions[-1])
            break


if __name__ == '__main__':
    main()
