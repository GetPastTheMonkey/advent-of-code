from aoc2024.day5.day5_common import day5_input, is_printable


def main():
    s = 0
    preconditions, prints = day5_input()

    for nums in prints:
        if is_printable(preconditions, nums):
            s += nums[len(nums) // 2]

    print(s)


if __name__ == '__main__':
    main()
