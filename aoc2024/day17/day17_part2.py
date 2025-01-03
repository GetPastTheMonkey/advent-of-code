from aoc2024.day17.day17_common import day17_input, day17_run


def main():
    instructions, registers = day17_input()
    a = 0

    for i in range(len(instructions)):
        # The program works with blocks of 3 bits --> Only need to bruteforce 3 bits at a time
        a <<= 3

        while True:
            reg = registers.copy()
            reg["A"] = a

            if day17_run(instructions, reg) == instructions[-i - 1:]:
                break

            a += 1

    print(a)


if __name__ == '__main__':
    main()
