from utils import get_input_lines


def day1_input() -> tuple[list[int], list[int]]:
    list_1 = list()
    list_2 = list()

    for line in get_input_lines(__file__):
        str_1, str_2 = line.split("   ")
        list_1.append(int(str_1))
        list_2.append(int(str_2))

    list_1.sort()
    list_2.sort()

    return list_1, list_2
