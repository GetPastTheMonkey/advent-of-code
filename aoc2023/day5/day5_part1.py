from utils import get_input_lines


def main():
    seeds = []
    mappings = []
    current_mapping = []

    for line in get_input_lines(__file__):
        if line.startswith("seeds"):
            seeds = list(map(int, line.split(": ")[1].split(" ")))
        elif line.endswith(":"):
            if current_mapping:
                mappings.append(current_mapping)
                current_mapping = []
        elif len(line) == 0:
            continue
        else:
            current_mapping.append(tuple(map(int, line.split(" "))))

    if current_mapping:
        mappings.append(current_mapping)

    minimum = None

    for seed in seeds:
        current_value = seed

        for mapping in mappings:
            for dst, src, size in mapping:
                if src <= current_value < src + size:
                    current_value = dst + current_value - src
                    break

        minimum = current_value if minimum is None else min(minimum, current_value)

    print(minimum)


if __name__ == '__main__':
    main()
