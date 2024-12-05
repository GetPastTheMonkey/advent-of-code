from aoc2024.day5.day5_common import day5_input, is_printable


def main():
    s = 0
    preconditions, prints = day5_input()

    for nums in prints:
        if not is_printable(preconditions, nums):
            relevant_precon = dict()  # type: dict[int, set[int]]

            for n in nums:
                relevant_precon[n] = set()

                if n in preconditions:
                    relevant_precon[n] = preconditions[n] & set(nums)

            correct_order = list()

            while len(relevant_precon) > 0:
                # Find the single empty set
                key = [k for k, v in relevant_precon.items() if len(v) == 0][0]
                correct_order.append(key)

                # Remove key from other sets
                del relevant_precon[key]

                for k in relevant_precon.keys():
                    relevant_precon[k].discard(key)

            s += correct_order[len(correct_order) // 2]

    print(s)


if __name__ == '__main__':
    main()
