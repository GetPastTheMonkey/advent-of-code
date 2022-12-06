from utils import get_input_lines


def day6_solve(window_size):
    for line in get_input_lines(__file__):
        for i in range(window_size, len(line)):
            window = line[i - window_size:i]

            if len(set(window)) == window_size:
                print(i)
                break
