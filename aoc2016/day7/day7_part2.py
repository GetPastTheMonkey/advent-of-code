from aoc2016.day7.day7_common import parse_line_brackets
from utils import get_input_lines


def all_possibilities():
    for a in range(26):
        for b in range(26):
            if a != b:
                chr_a = chr(ord("a") + a)
                chr_b = chr(ord("a") + b)
                yield "".join([chr_a, chr_b, chr_a]), "".join([chr_b, chr_a, chr_b])


def main():
    supports_ssl = 0

    for line in get_input_lines(__file__):
        must_contain_aba, must_contain_bab = parse_line_brackets(line)

        for aba, bab in all_possibilities():
            if any(aba in x for x in must_contain_aba) and any(bab in x for x in must_contain_bab):
                supports_ssl += 1
                break

    print(supports_ssl)


if __name__ == '__main__':
    main()
