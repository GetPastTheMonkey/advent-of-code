from utils import get_input_lines


def day9_solve(*, part_1: bool) -> int:
    sum_prediction = 0
    sum_history = 0

    for line in get_input_lines(__file__):
        nums = list(map(int, line.split(" ")))
        layers = []

        while not all(n == 0 for n in nums):
            layers.append(nums)
            new_nums = []

            for i in range(len(nums) - 1):
                new_nums.append(nums[i + 1] - nums[i])

            nums = new_nums

        prediction = 0
        history = 0

        for i in range(len(layers) - 1, -1, -1):
            prediction += layers[i][-1]
            history = layers[i][0] - history

        sum_prediction += prediction
        sum_history += history

    return sum_prediction if part_1 else sum_history
