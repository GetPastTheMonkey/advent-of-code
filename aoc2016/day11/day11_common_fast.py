def day11_solve(part_1: bool) -> int:
    elements_layer_1 = 4 if part_1 else 8
    elements_layer_2 = 2
    elements_layer_3 = 4
    result = 0

    for idx, count in enumerate([elements_layer_1, elements_layer_2, elements_layer_3]):
        # Every layer, we use (3-idx) to transport an element to the top floor
        # Multiply by 2 because we have to go up and down that distance for every element
        result += (3 - idx) * count * 2

        # Deduct 3 for every layer because the last two elements can be brought up to the next layer in 1 step
        # (usually it takes 4 steps to bring up a pair of elements by one layer)
        result -= 3

    return result
